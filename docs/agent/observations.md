# Observations

Grid Adventure is a **turn-based** game. Each turn, your agent is given a snapshot of the game, called an **observation**, and returns an [action](../game/actions-and-movement.md). That action is applied to produce the next snapshot, and the loop continues.

Your agent's [`step()`](agent-class.md#step-step) receives the observation in one of two forms. You choose the form when setting up your own [environment](environment.md), while an assessment may specify which form your agent receives.

| Representation | Description |
| --- | --- |
| [GridState](gridstate.md) | A grid-based representation using a 2D array. This is the most intuitive representation and the recommended starting point. |
| [ImageObservation](image-observation.md) | An RGBA image (3D array) of the rendered grid, plus an information dictionary. |

!!! note
    There is no built-in mapping function between `GridState` and `ImageObservation`. If you need to convert an image into a grid (for example, in your agent's [`parse`](agent-class.md#parse-parse-optional) method), you must build that mapping yourself.
