# ImageObservation

The `ImageObservation` representation contains a 3D image array plus additional information in a dictionary.

For details on how the image is rendered, see [Image Rendering](#image-rendering).

## Attribute hierarchy

The `ImageObservation` class represents a game snapshot as a dictionary with the following hierarchy:

```
ImageObservation: TypedDict
├── image: ndarray[H, W, 4] (uint8)
│   └── RGBA pixel data for the rendered grid
│
└── info: InfoDict # Dictionary subclass
    │
    ├── agent: AgentInfo # Dictionary subclass
    │   │
    │   ├── health: HealthInfo # Dictionary subclass
    │   │   ├── current_health: int (-1 if missing)
    │   │   └── max_health: int (-1 if missing)
    │   │
    │   ├── effects: list[EffectEntry]
    │   │   └── [each entry]
    │   │       ├── id: int
    │   │       ├── type: str ("" | "IMMUNITY" | "PHASING" | "SPEED")
    │   │       ├── limit_type: str ("" | "TIME" | "USAGE")
    │   │       ├── limit_amount: int (-1 if unlimited)
    │   │       └── multiplier: int (-1 if not SPEED)
    │   │
    │   └── inventory: list[InventoryItem]
    │       └── [each item]
    │           ├── id: int
    │           ├── type: str ("key" | "gem" | "coin" | "item")
    │           └── appearance_name: str ("" if unknown)
    │
    ├── status: StatusInfo # Dictionary subclass
    │   ├── score: int
    │   ├── phase: str ("ongoing" | "win" | "lose")
    │   └── turn: int
    │
    ├── config: ConfigInfo # Dictionary subclass
    │   ├── movement: str (movement function name)
    │   ├── objective: str (objective function name)
    │   ├── seed: int (-1 if None)
    │   ├── width: int
    │   ├── height: int
    │   └── turn_limit: int (-1 if unlimited)
    │
    └── message: str ("" if None)
```

## Image usage example

```python
from grid_adventure.env import GridAdventureEnv
from grid_adventure.levels import intro
from grid_universe.grid.convert import grid_state_fn_to_initial_state_fn

env = GridAdventureEnv(
    initial_state_fn=grid_state_fn_to_initial_state_fn(intro.build_level_basic_movement),
    observation_type="image",
)
obs, info = env.reset()

image = obs["image"]  # Shape: (H, W, 4), dtype: uint8

# Get image dimensions
height, width, channels = image.shape

# Save as PNG
from PIL import Image
pil_image = Image.fromarray(image)
pil_image.save("screenshot.png")

# Display with matplotlib
import matplotlib.pyplot as plt
plt.imshow(image)
plt.axis("off")
plt.show()
```

## InfoDict usage example

```python
from grid_adventure.env import GridAdventureEnv
from grid_adventure.levels import intro
from grid_universe.grid.convert import grid_state_fn_to_initial_state_fn

env = GridAdventureEnv(
    initial_state_fn=grid_state_fn_to_initial_state_fn(intro.build_level_basic_movement),
    observation_type="image",
)
obs, info = env.reset()

# Access the rendered image data
image = obs["image"]  # shape: (H, W, 4), dtype: uint8

# Access agent health
current_health = obs["info"]["agent"]["health"]["current_health"]
max_hp = obs["info"]["agent"]["health"]["max_health"]

# Check game phase
phase = obs["info"]["status"]["phase"]  # "ongoing", "win", or "lose"

# Get active effects
for effect in obs["info"]["agent"]["effects"]:
    print(f"Effect {effect['type']}: {effect['limit_amount']} remaining")

# Check inventory
for item in obs["info"]["agent"]["inventory"]:
    print(f"Item: {item['type']} (id={item['id']})")
```

## Image Rendering

The rendered image represents the current game state as a 2D grid. Each grid cell may contain multiple entities, which are drawn in order to produce the final image. For the different entities and their appearances, see [Entities](../game/entities.md).

An example of a rendered grid is shown below.

![Grid Example](../assets/grid_example.png)

### Overlapping rules

#### Initial state

- At the start of the game, **entities do not overlap**.
- The only exception is **Floor**, which may exist beneath any entity.

#### During gameplay

Overlaps may occur when the agent moves onto a tile containing other entities.

### Overlapping entities

#### Agent with collectible items

When the agent occupies the same cell as a collectible item:

- The agent is rendered normally.
- The collectible item is **shrunk** and displayed in the **top-left corner** of the cell.

![Agent Overlapping with collectible](../assets/rendering_agent_collectible.png)

#### Agent with background entities

`Floor`, `Lava`, `Exit`, and `UnlockedDoor` are background entities.

When the agent occupies the same cell as a background entity:

- The background entity remains visible.
- The agent is rendered **in front** of it.

![Agent Overlapping with Background entities](../assets/rendering_agent_background.png)
