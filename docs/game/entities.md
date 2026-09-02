# Entities

Entities are the objects you encounter in the grid. This page shows each entity's appearance and behavior and, for agent developers, the class used to recognise it in an [observation](../agent/observations.md).

!!! note "Identifying and rendering entities"
    Use `isinstance` to check an entity's type:

    ```python
    from grid_adventure.entities import WallEntity, CoinEntity, GemEntity, KeyEntity

    for entity in grid[x][y]:
        if isinstance(entity, WallEntity):
            print("Wall")
        elif isinstance(entity, CoinEntity):
            print("Coin")
        elif isinstance(entity, GemEntity):
            print("Gem")
        elif isinstance(entity, KeyEntity):
            print("Key")
    ```

    Each entity has several appearances. The images below show some of them and are not exhaustive.

## Floor

![Floor](../assets/floors.png)

Floor is the background rendered for every grid cell. It is implicit and does not appear as an entity in `GridState` or `State`.

## Agent

![Agent](../assets/humans.png)

The agent is the character you control and play as. It appears in the grid as a human. You move it around the grid, interact with objects, and aim to complete the objective.

In one turn, the agent can either move to an adjacent tile (up/down/left/right), pick up an item, use a key to unlock a door, or do nothing (wait). The agent has 5 health by default, but a level can configure a different amount. The player loses if HP drops to 0.

*Class:* `AgentEntity`

The agent carries additional attributes and methods:

| Attribute | Type | Description |
|---|---|---|
| `health` | `Health` | The agent's max and current health |
| `inventory_list` | `list[BaseEntity]` | Entities in the agent's inventory |
| `status_list` | `list[BaseEntity]` | Statuses (effects) active on the agent |

| Method | Inputs | Description |
|---|---|---|
| `set_health` | `health: int` | Sets the agent's health |

## Wall

![Wall](../assets/walls.png)

Walls block the agent from moving past them.

*Class:* `WallEntity`

## Exit

![Exit](../assets/exits.png)

The final escape tile that the agent must reach to complete the objective.

*Class:* `ExitEntity`

## Coin

![Coin](../assets/coins.png)

A coin is an **optional** item that can be picked up on the grid. Collecting a coin grants a reward of 5.

*Class:* `CoinEntity`

## Gem

![Gem](../assets/gems.png)

A gem is a **compulsory** item. If any gems are present, the agent must collect all of them before it can win at the exit.

*Class:* `GemEntity`

## Key

![Key](../assets/keys.png)

A key is an optional item that can be picked up by the agent. Any key can unlock any locked door, but each key can only be used once.

*Class:* `KeyEntity`

## Door

![Locked_Door](../assets/locked_doors.png)

A locked door blocks the agent from moving past it. To unlock a door, the agent must first collect a key. Using the key while standing adjacent to the door unlocks it, turning it into an unlocked door. A phased agent can also unlock a locked door while occupying its tile. The agent can then pass freely through unlocked doors. Unlocked doors appear on the grid as shown below.

![Unlocked_Door](../assets/unlocked_doors.png)

*Locked class:* `LockedDoorEntity`

*Unlocked class:* `UnlockedDoorEntity`

## Box

![Box](../assets/boxes.png)

A box can be moved by the agent. The agent pushes a box by moving into it. A box cannot be pushed onto a wall, locked door, another box, agent, or lava. It can share a tile with passable entities such as collectibles, exits, and unlocked doors.

*Class:* `BoxEntity`

## Lava

![Lava](../assets/lavas.png)

Lava inflicts 2 damage whenever an action processes the agent on the same tile. This includes moving onto or through lava and taking another action while still on it. The player loses if the agent's HP drops to 0.

*Class:* `LavaEntity`

---

Powerups are also entities you can pick up. Because they behave differently from the objects above (they grant temporary effects with turn or usage limits), they have their own page: [Powerups & Effects](powerups.md).
