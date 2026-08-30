# ImageObservation

The `ImageObservation` representation is a dictionary. `obs["image"]` is the rendered RGBA image as a `uint8` NumPy array, and `obs["info"]` contains accompanying information about the agent, game status, and level configuration.

```python
image = obs["image"]
info = obs["info"]
```

For details on how the image is rendered, see [Image Rendering](#image-rendering).

## Image Rendering

The rendered image represents the current game state as a 2D grid. Each grid cell may contain multiple entities, which are drawn in order to produce the final image. For the different entities and their appearances, see [Entities](../game/entities.md).

An example of a rendered grid is shown below.

![Grid Example](../assets/grid_example.png)

### Overlapping rules

- At the start of a capstone level, different visible object types do not share a cell.
- Overlaps may occur during play when the agent moves onto another entity or pushes a box onto a passable entity.

### Overlapping entities

#### Agent with collectible items

When the agent occupies the same cell as a collectible item, including a coin, key, gem, or powerup:

- The agent is rendered normally.
- The collectible item is **shrunk** and displayed in the **top-left corner** of the cell.

![Agent Overlapping with collectible](../assets/rendering_agent_collectible.png)

#### Agent with background entities

When the agent occupies the same cell as lava, an exit, or an unlocked door:

- The background entity remains visible.
- The agent is rendered **in front** of it.

![Agent Overlapping with Background entities](../assets/rendering_agent_background.png)

Other overlaps, including a box and a collectible, follow the same entity draw order. Image-based agents should not assume that only the agent can overlap another entity.
