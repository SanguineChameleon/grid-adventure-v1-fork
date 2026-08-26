# Grid Adventure

Welcome to **Grid Adventure**, a flexible, grid-based game in which you implement an **agent** that interacts with diverse gameplay mechanics to fulfil objectives.

## Objective

Grid Adventure is a **turn-based** game played on a 2D grid of tiles. The agent can start at any location on the grid. To win, it must **collect all gems** on the grid (if any) and **reach the exit tile** with the lowest cost possible. The agent starts with some health points and loses if its HP drops to **0**. Some levels also limit the number of turns.

![A Grid Adventure level](assets/grid_example.png)

## Mechanics

In one turn, the agent takes exactly one **action**: move to an adjacent tile (up/down/left/right), pick up an item, use a key, or wait.

Scoring works as follows:

- Each turn taken by the agent gives a reward of **-3**, except a turn that ends on the exit tile.
- Each coin collected gives a reward of **+5**.

## The objects

| Object | Role |
|---|---|
| **Agent** | The character you control. It starts with up to 5 health. |
| **Wall** | Blocks the agent from moving past. |
| **Exit** | The tile the agent must reach to finish. |
| **Gem** | Must be collected. All gems are required before exiting. |
| **Coin** | Optional. Collecting one gives a reward of 5. |
| **Key and Door** | A key unlocks a door. Any key works, but each key is used only once. |
| **Box** | Can be pushed onto a free tile. |
| **Lava** | Deals 2 damage when the agent steps on it. |
| **Powerups** | Speed, Shield, and Phasing. They give temporary boosts. |

See [Entities](game/entities.md) for the appearance and behavior of each object, and [Powerups & Effects](game/powerups.md) for how powerup limits work.

## Your task

You implement one method, `step`, that returns an **[Action](game/actions-and-movement.md)** each turn:

```python
def step(self, obs) -> Action:
    ...
```

Each turn your agent receives an **observation** (a snapshot of the game) and returns an action:

> observation → step() → action → new observation → …

## Where to go next

Read these sections to learn the details and build your agent:

- [Entities](game/entities.md): the objects you will encounter in the grid
- [Actions & Movement](game/actions-and-movement.md): how the agent moves and interacts with objects
- [Objectives & Rewards](game/objectives-and-rewards.md): what you must accomplish to win, and how score works
- [Powerups & Effects](game/powerups.md): temporary boosts and how their limits work
- [Building Your Agent](agent/agent-class.md): the Agent class, observations, and the environment
- [Testing in Grid Play](grid-play/index.md): run and debug your agent in the browser

## Two tools, one project

**Grid Adventure** is the game and the Python environment your agent plugs into (the [Agent Class](agent/agent-class.md), [Observations](agent/observations.md), and the [Environment](agent/environment.md)).

**[Grid Play](grid-play/index.md)** is a browser playground for playing levels and running your agent step by step, so you can see what it perceives and does.

Use the tabs above to navigate and start gridding!
