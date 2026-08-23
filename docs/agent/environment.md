# The Environment

`GridAdventureEnv` is the main environment that runs the game. It implements the Gymnasium API, providing a standard interface for agents to interact with the game.

## Constructor parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `initial_state_fn` | `Callable[..., State]` | required | Function that generates the initial internal game state |
| `render_mode` | `str` | `"rgb_array"` | Rendering mode |
| `observation_type` | `str` | `"image"` or `"gridstate"` | Determines whether observations are returned as [ImageObservation](image-observation.md) or [GridState](gridstate.md) |

For more on the two representations, see [Observations](observations.md).

## Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `GridAdventureEnv.reset(seed, options)` | `tuple[Observation, dict]` | Resets the internal game state and returns the observation |
| `GridAdventureEnv.step(action)` | `tuple[Observation, float, bool, bool, dict]` | Applies one action and returns the resulting observation |
| `GridAdventureEnv.render()` | `PILImage` or `None` | Renders the current state. See [Image Rendering](image-observation.md#image-rendering) |
| `GridAdventureEnv.close()` | `None` | Releases resources |
