import os
from pathlib import Path
from typing import Any

from grid_universe.renderer.image import ImageMap
from grid_universe.renderer.image import ImageRenderer as BaseImageRenderer

# Default asset root directory.
DEFAULT_ASSET_ROOT = os.path.join(Path(__file__).parent.resolve(), "assets")

# Mapping from (appearance name, properties) to image file/directory names.
IMAGE_MAP: ImageMap = ImageMap(
    {
        ("human", ()): "human",
        ("human", ("dead",)): "sleeping",
        ("coin", ()): "coin",
        ("gem", ("requirable",)): "gem",
        ("metalbox", ()): "metalbox",
        ("box", ("pushable",)): "box",
        ("robot", ()): "robot",
        ("key", ()): "key",
        ("portal", ()): "portal",
        ("door", ("locked",)): "locked",
        ("door", ()): "opened",
        ("shield", ("immunity",)): "shield",
        ("ghost", ("phasing",)): "ghost",
        ("boots", ("speed",)): "boots",
        ("lava", ()): "lava",
        ("exit", ()): "exit",
        ("wall", ()): "wall",
        ("floor", ()): "floor",
    }
)


class ImageRenderer(BaseImageRenderer):
    """Image renderer for the Grid Adventure environment."""

    def __init__(
        self,
        asset_root: str = DEFAULT_ASSET_ROOT,
        image_map: ImageMap = IMAGE_MAP,
        **kwargs: Any,
    ):
        super().__init__(asset_root=asset_root, image_map=image_map, **kwargs)
