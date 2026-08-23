# Observations

Grid Adventure is a **turn-based** game. Each turn, your agent is given a snapshot of the game — an **observation** — and returns an [action](../game/actions-and-movement.md). That action is applied to produce the next snapshot, and the loop continues.

Your agent's [`step()`](agent-class.md#step-step) receives the observation in one of two forms, which you choose when setting up the [environment](environment.md):

| Representation | Description |
| --- | --- |
| [GridState](gridstate.md) | A grid-based representation using a 2D array. This is the most intuitive representation and the recommended starting point. |
| [ImageObservation](image-observation.md) | An RGBA image (3D array) of the rendered grid, plus an information dictionary. |

!!! note
    There is no built-in mapping function between `GridState` and `ImageObservation`. If you need to convert an image into a grid (for example, in your agent's [`parse`](agent-class.md#parse-parse-optional) method), you must build that mapping yourself.

!!! tip "A third, optional representation"
    A lower-level [State](../advanced/state.md) representation also exists. It is the most comprehensive but also the most complex, and **is not required** to complete the project. Reach for it only if you specifically need low-level access. See the optional [State & Component Reference](../advanced/state.md).
