from collections.abc import Callable
from typing import Any

from grid_universe.state import State
from grid_universe.env import GridUniverseEnv
from grid_universe.renderer.image import ImageMap, DEFAULT_RESOLUTION
from grid_universe.grid.gridstate import GridState

from grid_adventure.grid import from_state
from grid_adventure.rendering import DEFAULT_ASSET_ROOT, IMAGE_MAP


class GridAdventureEnv(GridUniverseEnv):
    """Grid Adventure environment class.

    This class extends the base `GridUniverseEnv` to incorporate
    Grid Adventure-specific configurations, entities, and objectives.
    """

    def __init__(
        self,
        initial_state_fn: Callable[..., State],
        render_mode: str = "rgb_array",
        render_resolution: int = DEFAULT_RESOLUTION,
        render_image_map: ImageMap = IMAGE_MAP,
        render_asset_root: str = DEFAULT_ASSET_ROOT,
        observation_type: str = "image",
        **kwargs: Any,
    ) -> None:
        super().__init__(
            initial_state_fn=initial_state_fn,
            render_mode=render_mode,
            render_resolution=render_resolution,
            render_image_map=render_image_map,
            render_asset_root=render_asset_root,
            observation_type=observation_type,
            **kwargs,
        )

    @property
    def gridstate(self) -> GridState:
        """Return the current state as a GridState dataclass"""
        assert self.state is not None, (
            "Environment state is not initialized. Call reset() to initialize."
        )
        return from_state(self.state)
