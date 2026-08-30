# State & Component Reference

!!! warning "Optional: not required for the project"
    This page documents the low-level `State` representation. **The project can be solved without it.** It is included only for lower-level access to the game representation. If you are just getting started, use [GridState](../agent/gridstate.md) or [ImageObservation](../agent/image-observation.md) instead.

The `State` representation is the internal representation used by Grid Adventure. It stores information in component dictionaries indexed by the `EntityID` of each entity. It is used to generate the `GridState` and `ImageObservation` representations.

## State attributes

The `State` class represents a game snapshot with four categories of attributes.

- Grid Configuration
- Effect Components
- Property Components
- Game Status

### Grid configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| `width` | `int` | Grid width in tiles |
| `height` | `int` | Grid height in tiles |
| `movement` | `BaseMovement` | Movement functions allowed |
| `objective` | `BaseObjective` | Objective of the grid |

### Effect components

All effect stores are dictionaries of type `dict[EntityID, Component]`.

| Attribute | Mapped Component | Description |
|-----------|-----------|-------------|
| `immunity` | `Immunity` | Damage immunity effects |
| `phasing` | `Phasing` | Pass-through-walls effects |
| `speed` | `Speed` | Movement multiplier effects |
| `time_limit` | `TimeLimit` | Effect duration (remaining steps) |
| `usage_limit` | `UsageLimit` | Effect uses (remaining count) |

### Property components

All property stores are dictionaries of type `dict[EntityID, Component]`.

| Attribute | Mapped Component | Description |
|-----------|-----------|-------------|
| `agent` | [`Agent`](#agententity) | Player-controlled entities |
| `appearance` | `Appearance` | Visual rendering properties |
| `blocking` | [`Blocking`](#blockingentity) | Obstacles that block movement |
| `collectible` | [`Collectible`](#collectibleentity) | Items that can be picked up |
| `collidable` | [`Collidable`](#collidable-entities) | Entities triggering collision events |
| `cost` | `Cost` | Entities that inflict movement cost |
| `damage` | [`Damage`](#lavaentity) | Entities that deal damage on contact |
| `dead` | `Dead` | Dead/incapacitated entities |
| `exit` | [`Exit`](#exitentity) | Grid exit points |
| `health` | `Health` | Entity health (current/max) |
| `inventory` | `Inventory` | Items held by entities |
| `key` | [`Key`](#keyentity) | Keys that unlock `Locked` entities |
| `locked` | [`Locked`](#lockeddoorentity) | Locked doors/entities |
| `position` | `Position` | Entity grid positions |
| `pushable` | [`Pushable`](#pushableentity) | Entities that can be pushed |
| `requirable` | [`Requirable`](#gementity) | Must-collect items for objectives |
| `rewardable` | [`Rewardable`](#coinentity) | Entities granting score rewards |
| `status` | `Status` | Active status effects on entities |

### Game status

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `step_cost` | `int` | `0` | Score cost applied to each non-terminal action. Grid Adventure levels configure it as `3` |
| `turn` | `int` | `0` | Current turn number |
| `score` | `int` | `0` | Cumulative score |
| `win` | `bool` | `False` | `True` if the objective is met |
| `lose` | `bool` | `False` | `True` if the losing condition is met |
| `message` | `str` or `None` | `None` | Optional status message for display |
| `turn_limit` | `int` or `None` | `None` | Maximum turns allowed |
| `seed` | `int` or `None` | `None` | RNG seed for deterministic behavior |

## Useful methods

| Method | Description |
|--------|-------------|
| `state.description` | Property returning a dictionary of public state fields and non-empty component stores |
| `state.clone()` | Returns a separate copy of the state |
| `from_state(state)` | Converts `State` to [`GridState`](../agent/gridstate.md) |

## Entities

Each entity is assigned a unique `EntityID` at creation. Component stores map these IDs to the components held by each entity.

### Entity types

There are, in general, five types of entities:

| Entity Type | Description |
|---|---|
| CollidableEntity | Recognisable by possession of a `collidable` attribute of the `Collidable` class |
| BlockingEntity | Recognisable by possession of a `blocking` attribute of the `Blocking` class |
| PushableEntity | Recognisable by possession of a `pushable` attribute of the `Pushable` class |
| CollectibleEntity | Recognisable by possession of a `collectible` attribute of the `Collectible` class |
| Others | All other entities |

### Collidable Entities

These entities can pass through each other but trigger interactions when they do. They are recognisable by possession of a `collidable` attribute of the `Collidable` class.

There are 2 relevant collidable entities:

- AgentEntity
- LavaEntity

#### [AgentEntity](../game/entities.md#agent)

This is the entity controlled by the user.

| Attribute | Type | Description |
|---|---|---|
| health | `Health` | Maximum and current health of the agent |
| inventory_list | `list[BaseEntity]` | Entities in the agent's inventory |
| status_list | `list[BaseEntity]` | Effects active on the agent |

| Available Method | Inputs | Description |
|---|---|---|
| set_health | health: int | Sets the agent's health |

#### [LavaEntity](../game/entities.md#lava)

This is a damaging entity that the agent can walk through.

### BlockingEntity

These entities cannot be passed through by collidable entities. They are recognisable by possession of a `blocking` attribute of the `Blocking` class.

There are 3 relevant blocking entities:

- WallEntity
- LockedDoorEntity
- BoxEntity

### PushableEntity

These entities are pushable by the agent. They are recognisable by possession of a `pushable` attribute of the `Pushable` class.

There is 1 relevant pushable entity: [BoxEntity](#boxentity).

#### [WallEntity](../game/entities.md#wall)

A wall entity that the agent cannot walk through or push. The wall entity has no attributes.

#### [BoxEntity](../game/entities.md#box)

A pushable blocking entity that the agent can push but not walk through. The box entity has no attributes.

Note: the box is both a [Blocking](#blockingentity) and a [Pushable](#pushableentity) entity.

#### [LockedDoorEntity](../game/entities.md#door)

A blocking entity that the agent cannot walk or push through. It becomes an [UnlockedDoorEntity](#unlockeddoorentity) when a [KeyEntity](#keyentity) is used on it.

| Attribute | Type | Description |
|---|---|---|
| locked | Locked Class | Locked door that can be unlocked by a key |

Note: Each grid can have multiple keys and locked doors. Any key can unlock any locked door, but each key can only be used once.

### CollectibleEntity

These entities are collectible by the agent. They are recognisable by possession of a `collectible` attribute of the `Collectible` class.

There are 6 relevant collectible entities:

- CoinEntity
- GemEntity
- KeyEntity
- SpeedPowerUpEntity
- ShieldPowerUpEntity
- PhasingPowerUpEntity

#### [CoinEntity](../game/entities.md#coin)

An **optional** collectible that provides a score when collected by the agent.

| Attribute | Type | Description |
|---|---|---|
| rewardable | Rewardable Class | The score provided for picking up the coin |

Note: The score received for collecting a coin is fixed at 5.

#### [GemEntity](../game/entities.md#gem)

A **compulsory** collectible that must be collected before the agent can win at the exit. The gem entity has no additional attributes.

#### [KeyEntity](../game/entities.md#key)

A collectible required to unlock a [LockedDoorEntity](#lockeddoorentity).

| Attribute | Type | Description |
|---|---|---|
| key | Key Class | Key that can be used to unlock a LockedDoorEntity |

Note: Any key present in the grid can be used to unlock a door, but each key can only be used once.

#### [SpeedPowerUpEntity](../game/powerups.md#speed)

A collectible power-up granting the agent the ability to walk 2 tiles in 1 turn for a duration.

| Attribute | Type | Description |
|---|---|---|
| speed | Speed Class | Saves the multiplier, indicating the speed-up provided |
| time_limit | TimeLimit Class | Saves the amount, indicating the number of turns the powerup is active |

Note: The time limit is a constant 5 steps.

#### [ShieldPowerUpEntity](../game/powerups.md#shield)

A collectible power-up granting the agent immunity while walking on damaging tiles, for 5 uses.

| Attribute | Type | Description |
|---|---|---|
| immunity | `Immunity` | Prevents damage to the agent |
| usage_limit | UsageLimit Class | Shows the remaining durability of the shield |

Note: The usage limit is a constant 5 uses.

#### [PhasingPowerUpEntity](../game/powerups.md#phasing)

A collectible power-up granting the agent the ability to walk through [BlockingEntity](#blockingentity) objects for a duration.

| Attribute | Type | Description |
|---|---|---|
| phasing | `Phasing` | Allows the agent to pass through blocking entities and avoid damage |
| time_limit | TimeLimit Class | Saves the amount, indicating the number of turns the powerup is active |

Note: The time limit is a constant 5 steps.

### Other entities

These entities extend directly from `BaseEntity`.

#### [ExitEntity](../game/entities.md#exit)

The final tile the agent must reach to complete the objective. The exit entity has no other attributes.

#### [UnlockedDoorEntity](../game/entities.md#door)

Not interactable with the agent and serves only an aesthetic purpose. It is the unlocked version of the [LockedDoorEntity](#lockeddoorentity). The unlocked door entity has no attributes.

## Usage example

Use the code below to familiarise yourself with the `State` representation and explore its components.

### Useful operations

- **Get agent ID**
  ```python
  next(iter(state.agent.keys()), None)
  ```

- **Look up components by EntityID**
  ```python
  state.position.get(eid)
  eid in state.blocking
  ```

- **Iterate entities in a cell**
  Invert `state.position` to obtain a mapping of:
  ```text
  Position -> [EntityID]
  ```

- **Sparse debug view**
  ```python
  state.description
  ```
  Returns a dictionary containing public state fields and populated component stores.

- **Apply an action**
  ```python
  step(state, Action.RIGHT) -> State
  ```

### Full example

```python
from grid_adventure.actions import Action
from grid_adventure.constants import STEP_COST
from grid_adventure.entities import AgentEntity, BoxEntity, ExitEntity
from grid_adventure.grid import GridState, to_state
from grid_adventure.movements import MOVEMENTS
from grid_adventure.objectives import OBJECTIVES
from grid_adventure.step import step

# Creating the grid still requires GridState
gridstate = GridState(
    width=4,
    height=3,
    movement=MOVEMENTS["cardinal"],
    objective=OBJECTIVES["collect_gems_and_exit"],
    seed=0,
    step_cost=STEP_COST,
)

# Add an agent, a box, and an exit to the grid
gridstate.add((0, 1), AgentEntity())
gridstate.add((1, 1), BoxEntity())
gridstate.add((3, 1), ExitEntity())

# Convert GridState to the low-level State representation
state = to_state(gridstate)

# state.description contains only populated component stores
# (e.g. position, agent, blocking, etc.)

# state.position maps EntityID to Position objects

# Retrieve the agent's EntityID
agent_id = next(iter(state.agent.keys()))

# Find all pushable entities. Since only 1 box was added, this holds the box's EntityID
box_entity_ids = list(state.pushable.keys())
box_id = box_entity_ids[0]

# Look up current positions
agent_position = state.position[agent_id]
box_position = state.position[box_id]
agent_coordinates = (agent_position.x, agent_position.y)  # (0, 1)
box_coordinates = (box_position.x, box_position.y)  # (1, 1)

# Check whether an entity is considered blocking
is_agent_blocking = agent_id in state.blocking  # False
is_box_blocking = box_id in state.blocking       # True

# Apply an action using step. step returns a new State
state = step(state, Action.RIGHT)

# After stepping, the agent's position is updated
new_agent_position = state.position[agent_id]
new_agent_coordinates = (new_agent_position.x, new_agent_position.y)  # (1, 1)
```
