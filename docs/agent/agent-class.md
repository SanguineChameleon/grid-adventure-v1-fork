# The Agent Class

The `Agent` class is the API you implement to play Grid Adventure. This is where you start when building your agent.

It has **two required** methods and **two optional** methods (used only for debugging in [Grid Play](../grid-play/index.md)):

| Method | Required? | Description |
| --- | --- | --- |
| `__init__(self, *args, **kwargs) -> None` | Required | Runs once when your agent is created |
| `step(self, obs: GridState \| ImageObservation) -> Action` | Required | Returns the [action](../game/actions-and-movement.md) to take this turn |
| `parse(self, obs: ImageObservation) -> GridState` | Optional | Returns what your agent "sees"; used by Grid Play to visualize the agent's perception |
| `info(self) -> dict[str, Any]` | Optional | Returns debug information; displayed by Grid Play each turn |

A minimal agent looks like this:

```python
from grid_adventure.actions import Action

class Agent:
    def __init__(self, *args, **kwargs) -> None:
        # Declare any internal variables your agent needs.
        ...

    def step(self, obs) -> Action:
        # Decide the next action from the current observation.
        return Action.WAIT
```

## Initialization - `__init__`

> `__init__(self, *args, **kwargs) -> None`

Runs once when the agent is instantiated.

**Tip:** use it to declare any internal variables your agent needs (for example, a plan, a map it builds up, or counters).

## Step - `step`

> `step(self, obs: GridState | ImageObservation) -> Action`

Invoked every turn in the main agent-environment loop. It inspects the current [observation](observations.md) and decides which [Action](../game/actions-and-movement.md) to return.

## Parse - `parse` (optional)

> `parse(self, obs: ImageObservation) -> GridState`

Defining `parse` enables the Vision display in Grid Play. In ImageObservation mode, Grid Play calls this method after each step to render the [GridState](gridstate.md) your agent reconstructs from an [ImageObservation](image-observation.md). This lets you spot and correct errors in how your agent interprets the image. In GridState mode, Grid Play renders the current GridState directly and does not call `parse`.

Your agent's vision appears in the bottom-right corner of the screen.

![Parse Window](../assets/parse.png)

In this example, the actual grid is in the blue square and the agent's vision is in the red square. Here we can see that the agent mistakenly believes there is a box in the grid.

## Info - `info` (optional)

> `info(self) -> dict[str, Any]`

If implemented, Grid Play displays the returned dictionary each turn, letting you inspect your agent's internal variables as it plays.

![Info Window](../assets/info.png)

## A baseline to start from

For a worked starting point, refer to the baseline `Agent` in the main notebook.
