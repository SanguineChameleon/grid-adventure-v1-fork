# GridState

The `GridState` representation is grid-centric and provides methods that you can use to directly manipulate the grid. It is the recommended starting point for most agents.

## Attributes

`GridState` has three categories of attributes.

### Overall configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| `width` | `int` | Grid width in tiles |
| `height` | `int` | Grid height in tiles |
| `movement` | `BaseMovement` | Movement function configuration |
| `objective` | `BaseObjective` | Win/lose condition configuration |
| `step_cost` | `int` | Reward cost applied to each non-terminal turn. The constructor default is `0`; Grid Adventure levels configure it as `3` |
| `seed` | `int` or `None` | RNG seed for deterministic behavior |

### Grid structure

| Attribute | Type | Description |
|-----------|------|-------------|
| `grid` | `list[list[list[BaseEntity]]]` | Grid representation where `grid[x][y]` is a list of entities at that cell |

### Game status

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `turn` | `int` | `0` | Current turn number |
| `score` | `int` | `0` | Cumulative score |
| `win` | `bool` | `False` | `True` if the objective is met |
| `lose` | `bool` | `False` | `True` if the losing condition is met |
| `message` | `str` or `None` | `None` | Optional status message for display |
| `turn_limit` | `int` or `None` | `None` | Maximum turns allowed |

## Instance methods

| Method | Returns | Description |
|--------|---------|-------------|
| `GridState.add(pos, obj)` | `None` | Place an entity at position `(x, y)` |
| `GridState.add_many(items)` | `None` | Place multiple entities from a list of `(pos, obj)` tuples |
| `GridState.remove(pos, obj)` | `bool` | Remove a specific entity by identity; returns `True` if found |
| `GridState.remove_if(pos, predicate)` | `int` | Remove entities where `predicate(obj)` is `True`; returns the number removed |
| `GridState.move_obj(from_pos, obj, to_pos)` | `bool` | Move an entity between cells; returns `True` if successful |
| `GridState.clear_cell(pos)` | `int` | Remove all entities from a cell; returns the count |
| `GridState.objects_at(pos)` | `list[BaseEntity]` | Return a shallow copy of the entities at a position |

## Conversion and simulation helpers

| Function | Returns | Description |
|----------|---------|-------------|
| `from_state(state)` | `GridState` | Convert a [`State`](../advanced/state.md) to a specialised Grid Adventure `GridState` |
| `to_state(grid_state)` | `State` | Convert a `GridState` to [`State`](../advanced/state.md) |
| `step(grid_state, action)` | `GridState` | Return a new `GridState` after applying an `Action` |

- `pos` is a position tuple represented as `(int, int)`.
- `obj` is a `BaseEntity`, the parent class of all entities. For the list of entities, their appearances, and how to identify them, see [Entities](../game/entities.md).
