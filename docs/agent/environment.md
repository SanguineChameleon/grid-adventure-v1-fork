# The Environment

`GridAdventureEnv` is the main environment that runs the game. It implements the Gymnasium API, providing a standard interface for agents to interact with the game.

## Constructor parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `initial_state_fn` | `Callable[..., State]` | required | Function that generates the initial internal game state |
| `render_mode` | `str` | `"rgb_array"` | Rendering mode: `"rgb_array"` or `"human"` |
| `render_resolution` | `int` | `640` | Width of the rendered image in pixels |
| `render_image_map` | `ImageMap` | `IMAGE_MAP` | Mapping from entity appearances to image assets |
| `render_asset_root` | `str` | `DEFAULT_ASSET_ROOT` | Root directory containing image assets |
| `observation_type` | `str` | `"image"` | Observation format: `"image"` for [ImageObservation](image-observation.md) or `"gridstate"` for [GridState](gridstate.md) |

For more on the two representations, see [Observations](observations.md).

## Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `GridAdventureEnv.reset(seed, options)` | `tuple[Observation, dict]` | Resets the internal game state and returns the observation |
| `GridAdventureEnv.step(action)` | `tuple[Observation, float, bool, bool, dict]` | Applies one action and returns the resulting observation |
| `GridAdventureEnv.render()` | `PILImage` or `None` | Renders the current state. See [Image Rendering](image-observation.md#image-rendering) |
| `GridAdventureEnv.close()` | `None` | Releases resources |

## Properties

| Property | Returns | Description |
|----------|---------|-------------|
| `GridAdventureEnv.gridstate` | `GridState` | Current internal state converted to the Grid Adventure `GridState` representation |
