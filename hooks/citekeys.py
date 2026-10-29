"""
Hook do MkDocs para citações do Zotero.

1. on_pre_build: lê o refs.bib (exportação automática do Better BibTeX) e
   COPIA para docs/papers/<citekey>.pdf o PDF guardado no Zotero.
   - O Zotero mantém os nomes que quiseres no seu armazenamento.
   - O projeto fica com ficheiros reais (não links), por isso funciona noutro
     computador, num backup ou num repositório, mesmo sem o Zotero.
   - Só recopia quando o PDF no Zotero muda (tamanho ou data).
   - Só apaga ficheiros que ele próprio criou (registados em
     docs/papers/.citekeys.json); nunca toca noutros ficheiros.
2. on_page_markdown: converte [@chave] e [@a; @b] em links para esses PDFs.

Ativar no mkdocs.yml:

    hooks:
      - hooks/citekeys.py
    watch:
      - refs.bib
"""

import json
import logging
import os
import posixpath
import re
import shutil
from pathlib import Path

BIB_FILE = "refs.bib"  # relativo à pasta do mkdocs.yml
PAPERS_DIR = "papers"  # relativo à pasta docs/
MANIFEST = ".citekeys.json"

log = logging.getLogger("mkdocs.hooks.citekeys")

KEY = r"@[\w:.\-]+"
GROUP_RE = re.compile(rf"\[({KEY}(?:\s*;\s*{KEY})*)\]")
ENTRY_RE = re.compile(r"^@\w+\s*\{\s*([^,\s]+)\s*,", re.M)
FILE_RE = re.compile(r"^\s*file\s*=\s*\{(.*?)\}\s*,?\s*$", re.M | re.S | re.I)
PDF_RE = re.compile(r"(/[^;{}]+?\.pdf)", re.I)


def _parse_bib(text):
    """Devolve {citekey: caminho do primeiro PDF existente}."""
    result = {}
    starts = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        field = FILE_RE.search(text, m.end(), end)
        if not field:
            continue
        for path in PDF_RE.findall(field.group(1)):
            path = path.strip()
            if os.path.isfile(path):
                result[m.group(1)] = path
                break
    return result


def _load_manifest(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _same(src, dst):
    a, b = os.stat(src), os.stat(dst)
    return a.st_size == b.st_size and int(a.st_mtime) == int(b.st_mtime)


def on_pre_build(config, **kwargs):
    root = Path(config["config_file_path"]).parent
    bib = root / BIB_FILE
    papers = Path(config["docs_dir"]) / PAPERS_DIR
    manifest_path = papers / MANIFEST

    if not bib.is_file():
        log.warning("citekeys: %s não encontrado; nada copiado.", bib)
        return

    if not papers.is_dir():
        papers.mkdir(parents=True)
    wanted = _parse_bib(bib.read_text(encoding="utf-8"))
    managed = _load_manifest(manifest_path)  # {ficheiro: origem}

    # Remove cópias feitas por este hook que já não estão no refs.bib.
    for name in list(managed):
        if name[:-4] not in wanted:
            (papers / name).unlink(missing_ok=True)
            del managed[name]

    copied = skipped = 0
    for key, src in wanted.items():
        name = f"{key}.pdf"
        dst = papers / name
        if dst.is_symlink():  # resto da versão antiga com symlinks
            dst.unlink()
        if dst.exists():
            if name not in managed:
                log.warning(
                    "citekeys: %s já existe e não foi criado por este "
                    "hook; não lhe toco.",
                    dst,
                )
                skipped += 1
                continue
            if managed[name] == src and _same(src, dst):
                continue
        shutil.copy2(src, dst)
        managed[name] = src
        copied += 1

    # Só grava o registo se mudou. Gravar sempre fazia o `mkdocs serve`
    # detetar uma alteração em docs/ e recompilar em ciclo infinito.
    new_manifest = json.dumps(managed, indent=1, sort_keys=True)
    try:
        old_manifest = manifest_path.read_text(encoding="utf-8")
    except OSError:
        old_manifest = None
    if new_manifest != old_manifest:
        manifest_path.write_text(new_manifest, encoding="utf-8")

    log.info(
        "citekeys: %d PDFs no projeto (%d copiados/atualizados, " "%d ignorados).",
        len(wanted) - skipped,
        copied,
        skipped,
    )


def on_page_markdown(markdown, page, config, files, **kwargs):
    page_dir = posixpath.dirname(page.file.src_uri) or "."

    def link(key):
        target = posixpath.relpath(f"{PAPERS_DIR}/{key}.pdf", page_dir)
        return f"[{key}]({target})"

    def repl(m):
        keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
        return "; ".join(link(k) for k in keys)

    return GROUP_RE.sub(repl, markdown)
