# Notes: `Agents Course` Hugging Face


## Thought-Action-Observation Cycle

```mermaid
flowchart TD

    Tho[Thought:\nThe LLM part of the Agent decides what the next step should be]
    Act[Action:\nThe agent takes an action by calling the tools with the associated arguments]
    Obs[Observation:\nThe model reflects on the response from the tool]
    
    Start([User Query]) --> Tho
    Tho --> Act
    Act --> Obs
    Obs -- loop --> Tho
    Obs -- end --> End[End]
```

## Thoughts

### Chain-of-Thought (CoT) 

### ReAct: Reasoning + Acting

## Actions

### Stop and Parse Approach

### Code Agents

## Observations

