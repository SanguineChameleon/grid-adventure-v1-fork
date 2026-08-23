# Grid Adventure

Welcome to **Grid Adventure** — a flexible, grid-based game in which you implement an **agent** that interacts with diverse gameplay mechanics to fulfil objectives.

The world is a 2D grid made up of tiles. The agent can start anywhere on the grid and must collect any gems present, then reach the exit tile.

## Your task

Your job is to implement an agent that plays the game automatically. Concretely, you implement one method:

```python
def step(self, obs) -> Action:
    ...
```

Every turn, your agent receives an **observation** (a snapshot of the game) and must return an **[Action](game/actions-and-movement.md)**. That's the whole loop:

> observation → `step()` → action → new observation → …

Everything in these docs exists to help you (1) understand the game your agent must play, (2) implement `step()`, and (3) test it.

## What to read first

| If you want to… | Read |
|---|---|
| Understand the rules your agent must model | [Playing the Game](game/overview.md) |
| Implement your agent | [Building Your Agent](agent/agent-class.md) |
| Run and debug your agent visually | [Testing in Grid Play](grid-play/index.md) |

!!! tip "What you can safely skip"
    You do **not** need the low-level [State representation](advanced/state.md) to complete the project. It is provided in the **Advanced** section for optional, lower-level access only. Start with [GridState](agent/gridstate.md) or [ImageObservation](agent/image-observation.md) instead.

## Two tools, one project

- **Grid Adventure** is the game and the Python environment your agent plugs into (the [Agent Class](agent/agent-class.md), [Observations](agent/observations.md), and the [Environment](agent/environment.md)).
- **[Grid Play](grid-play/index.md)** is a browser playground for playing levels, configuring them, and running your agent step-by-step so you can *see* what it perceives and does.

Use the tabs above to navigate, and start gridding!
