# A Baseline Agent

This page presents a simple baseline agent for Grid Adventure. It illustrates a complete agent from end to end, and it is the same starter provided in the capstone notebook. It is **not** an optimal solution, so treat it as a starting point that you can modify or replace.

The baseline handles every task with a single agent by separating two responsibilities:

- **Planning.** Search for a sequence of actions that wins the level, using breadth-first search (BFS) over `GridState`.
- **Perception.** When the observation is an `ImageObservation`, rebuild a `GridState` from the image before planning.

## The code

```python
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

from grid_adventure.grid import GridState, step as grid_step
from grid_adventure.env import ImageObservation
from grid_adventure.constants import STEP_COST
from grid_adventure.entities import (
    AgentEntity,
    BoxEntity,
    CoinEntity,
    ExitEntity,
    GemEntity,
    KeyEntity,
    LavaEntity,
    LockedDoorEntity,
    PhasingPowerUpEntity,
    ShieldPowerUpEntity,
    SpeedPowerUpEntity,
    UnlockedDoorEntity,
    WallEntity,
)
from grid_adventure.movements import MOVEMENTS
from grid_adventure.objectives import OBJECTIVES
from grid_adventure.rendering import DEFAULT_ASSET_ROOT
from grid_adventure.step import Action
from grid_universe.grid.entity import BaseEntity


class Agent:
    def __init__(self):
        pass

    def step(self, state: GridState | ImageObservation) -> Action:
        # Tasks 2 and 3: rebuild a GridState from the image before planning.
        if not isinstance(state, GridState):
            state = self.parse(state)
            has_agent = any(
                isinstance(entity, AgentEntity)
                for column in state.grid
                for cell in column
                for entity in cell
            )
            if not has_agent:
                return Action.WAIT

        # BFS over game states: return the first action of the first winning path.
        frontier = deque([(state, [])])
        visited = {str(state.grid)}

        while frontier:
            current_state, path = frontier.popleft()

            for action in Action:
                next_state = grid_step(current_state, action)
                if next_state.lose:
                    continue

                next_path = path + [action]
                if next_state.win:
                    return next_path[0]

                key = str(next_state.grid)
                if key in visited:
                    continue

                visited.add(key)
                frontier.append((next_state, next_path))

        return Action.WAIT

    def parse(self, observation: ImageObservation) -> GridState:
        # Rebuild a GridState from an image observation.
        info = observation["info"]
        config = info["config"]
        status = info["status"]

        gridstate = GridState(
            width=config["width"],
            height=config["height"],
            movement=MOVEMENTS["cardinal"],
            objective=OBJECTIVES["collect_gems_and_exit"],
            step_cost=STEP_COST,
            seed=None if config["seed"] == -1 else config["seed"],
            turn=status["turn"],
            score=status["score"],
            win=status["phase"] == "win",
            lose=status["phase"] == "lose",
            message=info["message"] or None,
            turn_limit=None if config["turn_limit"] == -1 else config["turn_limit"],
        )

        for y, row in enumerate(self.split_cells(observation)):
            for x, cell_image in enumerate(row):
                entity = self.predict(cell_image)
                if entity is not None:
                    if isinstance(entity, AgentEntity):
                        entity.set_health(info["agent"]["health"]["current_health"])
                    gridstate.add((x, y), entity)

        return gridstate

    def split_cells(self, observation: ImageObservation) -> list[list[np.ndarray]]:
        # Split the RGBA image into a grid of per-cell images.
        image = observation["image"]
        config = observation["info"]["config"]
        width = config["width"]
        height = config["height"]
        image_height, image_width = image.shape[:2]
        cells = []

        for y in range(height):
            y_start = y * image_height // height
            y_end = (y + 1) * image_height // height
            row = []
            for x in range(width):
                x_start = x * image_width // width
                x_end = (x + 1) * image_width // width
                row.append(image[y_start:y_end, x_start:x_end, :])
            cells.append(row)

        return cells

    def predict(self, cell_image: np.ndarray) -> BaseEntity | None:
        # Classify one cell by nearest match against the public asset for each entity.
        entity_types = {
            "boots": SpeedPowerUpEntity,
            "box": BoxEntity,
            "coin": CoinEntity,
            "exit": ExitEntity,
            "gem": GemEntity,
            "ghost": PhasingPowerUpEntity,
            "human": AgentEntity,
            "key": KeyEntity,
            "lava": LavaEntity,
            "locked": LockedDoorEntity,
            "opened": UnlockedDoorEntity,
            "shield": ShieldPowerUpEntity,
            "wall": WallEntity,
        }
        image_size = (cell_image.shape[1], cell_image.shape[0])
        asset_root = Path(DEFAULT_ASSET_ROOT)

        with Image.open(asset_root / "floor" / "floor_1.png") as image:
            floor = image.convert("RGBA").resize(image_size)

        observed = cell_image.astype(np.int16)
        best_entity = None
        best_error = np.abs(observed - np.asarray(floor)).mean()

        for asset_name, entity_type in entity_types.items():
            asset_path = asset_root / asset_name / f"{asset_name}_1.png"
            with Image.open(asset_path) as image:
                asset = image.convert("RGBA").resize(image_size)

            candidate = np.asarray(Image.alpha_composite(floor, asset))
            error = np.abs(observed - candidate).mean()
            if error < best_error:
                best_error = error
                best_entity = entity_type

        return None if best_entity is None else best_entity()

    def info(self) -> dict[str, str]:
        return {"name": "BFS Agent"}
```

## How it works

### Planning (`step`)

When the agent receives a `GridState`, it runs BFS directly. Each node in the search is a game state together with the path of actions taken to reach it. For each state, the agent tries every [Action](../game/actions-and-movement.md), simulates the result with `grid.step`, and then:

- skips any action that leads to a losing state,
- returns the first action of the path as soon as a winning state is reached,
- otherwise records the new state (keyed by `str(state.grid)`) and keeps searching.

If the search finds no winning path, the agent returns `Action.WAIT`.

### Perception (`parse`, `split_cells`, `predict`)

When the observation is an `ImageObservation`, the agent first rebuilds a `GridState`:

1. `split_cells` divides the rendered RGBA image into one image per grid cell.
2. `predict` classifies each cell by comparing it against the public asset image for each entity and keeping the closest match. An empty cell is read as floor.
3. `parse` assembles these entities, together with the agent health and status from the observation's `info` dictionary, into a `GridState`.

Grid Play also calls `parse` to display the agent's reconstructed view, so you can see what it perceives. See [The Agent Class](agent-class.md) for the optional `parse` and `info` methods, and [Observations](observations.md) for the two observation types.

## Limitations and where to go next

This baseline is intentionally simple, and it has two clear weaknesses:

- **Search cost.** BFS explores game states exhaustively and grows quickly on larger grids. Under a turn or time limit, it may not finish. Consider a cost-aware search such as uniform-cost search or A\*, and a state key that captures only what matters for planning.
- **Perception.** Matching each cell against a single reference image per entity is brittle, and graded image levels use unseen visual variants of the same entities. Consider a more robust or learned parser that generalizes beyond the provided assets.

Use [Grid Play](../grid-play/index.md) to run the agent step by step and inspect its vision (`parse`) and debug information (`info`).
