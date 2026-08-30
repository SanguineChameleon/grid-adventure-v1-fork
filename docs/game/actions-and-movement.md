# Actions & Movement

Each turn, the agent takes exactly one **action**. This page covers the actions available and shows how the agent moves and interacts with objects.

## The `Action` enum

Your agent's `step()` returns one of these actions. The `Action` enum defines all of them:

| Environment index | Action | Description |
|-------|--------|-------------|
| 0 | `UP` | Move up |
| 1 | `DOWN` | Move down |
| 2 | `LEFT` | Move left |
| 3 | `RIGHT` | Move right |
| 4 | `USE_KEY` | Unlock a locked door on the current or an adjacent tile |
| 5 | `PICK_UP` | Collect items at the current tile |
| 6 | `WAIT` | Do nothing (advance the turn) |

```python
from grid_adventure.actions import Action

# Using the Action enum with the environment
obs, reward, terminated, truncated, info = env.step(Action.UP)

# The environment also accepts the corresponding integer index
obs, reward, terminated, truncated, info = env.step(0)  # UP
```

Integer indices are accepted by `GridAdventureEnv.step` only. The lower-level `grid_adventure.grid.step(state, action)` function requires an `Action` and returns one new [`GridState`](../agent/gridstate.md).

## Basic movements

In a turn, the agent can move to an adjacent tile (Up / Down / Left / Right).

The example shows the agent performing basic movements.

![Basic_Movement](../assets/basic_movement.gif)

## Collecting items

If the agent is on the same tile as any collectible items, it can use a turn (`PICK_UP`) to pick them up.

The example shows the agent picking up items such as keys, gems, and coins.

![Collect_items](../assets/collect_items.gif)

## Key and door

To unlock a door, the agent must first collect a key, then stand adjacent to the door and use `USE_KEY`. If phasing places the agent on the locked door's tile, `USE_KEY` also unlocks it there.

The example shows the agent collecting the key, then unlocking the door to pass through.

![Key_Door](../assets/key_and_door.gif)

## Pushing a box

To push a box, the agent must stand adjacent to it and move in the direction of the push.

The example shows the agent pushing the box aside to reach the exit tile.

![Push_Box](../assets/push_box.gif)

## Redundant actions

Some actions have no useful effect in certain situations, but they still take a turn and incur the turn cost. For example:

- Moving into a blocking entity, such as a wall or a locked door, leaves the agent in place.
- Picking up on a tile with nothing to collect does nothing.
- Using a key when there is no locked door on the current or an adjacent tile does nothing and does not consume the key.

When planning, remember that a wasted action is still a turn.

---

Powerups change how the agent moves (moving multiple tiles, passing through walls, ignoring lava). Those are covered in [Powerups & Effects](powerups.md).
