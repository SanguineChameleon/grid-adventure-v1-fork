# Entities

Entities are the objects you encounter in the grid. This page shows each entity's appearance and behavior, and — for agent developers — the class you use to recognize it in an [observation](../agent/observations.md).

Each entity is displayed below in five slightly different visuals. Many other appearances exist that are similar but may differ subtly from those shown.

!!! info "How each entity is labeled"
    Every entity below lists two things:

    - **Class** — the Python class (e.g. `AgentEntity`). This is what you use to identify an entity programmatically, with `isinstance`.
    - **Appearance name** — a string (e.g. `"human"`) used *only* to decide which image to render.

    The appearance name is **not** a constructor argument. Entities are created with no arguments — for example `AgentEntity()`, not `AgentEntity("human")`. The appearance name is exposed as the entity's `appearance.name` attribute.

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

    When rendering the grid, each entity's **appearance name** determines which image is displayed. By default, images are loaded from `DEFAULT_ASSET_ROOT` defined in `grid_adventure.rendering`, which provides the public Grid Adventure assets. A mapping from appearance name to image is defined as `IMAGE_MAP` in the same package.

    There are 14 entity types in total. For the full list of per-entity attributes and components, see the optional [State & Component Reference](../advanced/state.md).

## Floor

![Floor](../assets/floors.png)

Floor is the basic tile of the grid. Other entities can also be present on floor tiles.

*Class:* `FloorEntity` · *Appearance name:* `"floor"`

## Agent

![Agent](../assets/humans.png)

The agent is the character you control and play as. It appears in the grid as a human. You move it around the grid, interact with objects, and aim to complete the objective.

In one turn, the agent can either move to an adjacent tile (up/down/left/right), pick up an item, use a key to unlock a door, or do nothing (wait). The agent starts with some health points (up to 5) and the player loses if HP drops to 0.

*Class:* `AgentEntity` · *Appearance name:* `"human"`

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

*Class:* `WallEntity` · *Appearance name:* `"wall"`

## Exit

![Exit](../assets/exits.png)

The final escape tile that the agent must reach to complete the objective.

*Class:* `ExitEntity` · *Appearance name:* `"exit"`

## Coin

![Coin](../assets/coins.png)

A coin is an **optional** item that can be picked up on the grid. Collecting a coin grants a reward of 5.

*Class:* `CoinEntity` · *Appearance name:* `"coin"`

## Gem

![Gem](../assets/gems.png)

A gem is a **compulsory** item. If any gems are present, the agent must collect all of them before reaching the exit to complete the objective.

*Class:* `GemEntity` · *Appearance name:* `"gem"`

## Key

![Key](../assets/keys.png)

A key is an optional item that can be picked up by the agent. A key is required to unlock a door. Any key can be used to unlock any door, but each key can only be used once.

*Class:* `KeyEntity` · *Appearance name:* `"key"`

## Door

![Locked_Door](../assets/locked_doors.png)

A locked door blocks the agent from moving past it. To unlock a door, the agent must first collect a key. Using the key while standing adjacent to the door unlocks it, turning it into an unlocked door. The agent can then pass freely through unlocked doors. Unlocked doors appear on the grid as shown below.

![Unlocked_Door](../assets/unlocked_doors.png)

*Locked class:* `LockedDoorEntity` · *Unlocked class:* `UnlockedDoorEntity` · *Appearance name (both):* `"door"`

!!! note "Distinguishing door states"
    Both `LockedDoorEntity` and `UnlockedDoorEntity` share the appearance name `"door"`, so you cannot tell them apart by appearance. Use `isinstance` to distinguish them:

    ```python
    from grid_adventure.entities import LockedDoorEntity, UnlockedDoorEntity

    for entity in grid[x][y]:
        if isinstance(entity, LockedDoorEntity):
            print("Locked door")
        elif isinstance(entity, UnlockedDoorEntity):
            print("Unlocked door")
    ```

!!! note "Multiple keys and doors"
    If the agent has multiple keys and there are multiple locked doors on the agent's current tile and/or on adjacent tiles, the Use Key action attempts to unlock doors in this order: current tile, then left, right, up, and down. Each door unlocked consumes one key, and unlocking stops when the agent has no keys remaining. The total number of doors unlocked cannot exceed the number of keys the agent holds.

## Box

![Box](../assets/boxes.png)

A box can be moved by the agent. The agent can push a box in any direction onto a free tile. Boxes cannot be pushed onto walls, doors, or lava.

*Class:* `BoxEntity` · *Appearance name:* `"box"`

## Lava

![Lava](../assets/lavas.png)

Lava tiles inflict damage on the agent. When the agent lands on lava, it takes 2 damage. The player loses if the agent's HP drops to 0.

*Class:* `LavaEntity` · *Appearance name:* `"lava"`

---

Powerups are also entities you can pick up. Because they behave differently from the objects above (they grant temporary effects with turn or usage limits), they have their own page: [Powerups & Effects](powerups.md).
