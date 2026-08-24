# Actions & Movement

Each turn, the agent takes exactly one **action**. This page covers the actions available and shows how the agent moves and interacts with objects.

## The `Action` enum

Your agent's `step()` returns one of these actions. The `Action` enum defines all of them:

| Index | Action | Description |
|-------|--------|-------------|
| 0 | `UP` | Move up |
| 1 | `DOWN` | Move down |
| 2 | `LEFT` | Move left |
| 3 | `RIGHT` | Move right |
| 4 | `USE_KEY` | Unlock an adjacent locked entity with a matching key |
| 5 | `PICK_UP` | Collect items at the current tile |
| 6 | `WAIT` | Do nothing (advance the turn) |

```python
from grid_adventure.actions import Action
from grid_adventure.grid import GridState, step

state = GridState(...)

# Using the Action enum with the environment
obs, reward, terminated, truncated, info = step(state, Action.UP)

# Using the integer index
obs, reward, terminated, truncated, info = step(state, 0)  # UP
```

Actions are primarily used with the `step` function of the [environment](../agent/environment.md#methods).

## Basic movements

In a turn, the agent can move to an adjacent tile (Up / Down / Left / Right).

The example shows the agent performing basic movements.

!!! warning "Redundant actions"
    Moving into a blocking entity (a wall or a locked door) also counts as a turn!

![Basic_Movement](../assets/basic_movement.gif)

## Collecting items

If the agent is on the same tile as any collectible items, it can use a turn (`PICK_UP`) to pick them up.

The example shows the agent picking up items such as keys, gems, and coins.

!!! warning "Redundant actions"
    Picking up on a tile with nothing to collect also counts as a turn!

![Collect_items](../assets/collect_items.gif)

## Key and door

To unlock a door, the agent must first collect a key, then move adjacent to the door and unlock it (`USE_KEY`).

The example shows the agent collecting the key, then unlocking the door to pass through.

!!! warning "Redundant actions"
    Using a key when there are no doors nearby does not consume the key, but it also counts as a turn!

![Key_Door](../assets/key_and_door.gif)

## Pushing a box

To push a box, the agent must stand adjacent to it and move in the direction of the push.

The example shows the agent pushing the box aside to reach the exit tile.

![Push_Box](../assets/push_box.gif)

---

Powerups change how the agent moves (moving multiple tiles, passing through walls, ignoring lava). Those are covered in [Powerups & Effects](powerups.md).
