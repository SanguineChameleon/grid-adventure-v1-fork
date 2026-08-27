# ImageObservation

The `ImageObservation` representation contains a 3D image array plus additional information in a dictionary.

For details on how the image is rendered, see [Image Rendering](#image-rendering).

## Image Rendering

The rendered image represents the current game state as a 2D grid. Each grid cell may contain multiple entities, which are drawn in order to produce the final image. For the different entities and their appearances, see [Entities](../game/entities.md).

An example of a rendered grid is shown below.

![Grid Example](../assets/grid_example.png)

### Overlapping rules

- At the start of the game, **entities do not overlap**.
- During the gameplay, overlaps may occur when the agent moves onto a tile containing other entities.

### Overlapping entities

#### Agent with collectible items

When the agent occupies the same cell as a collectible item (`Coin`, `Key`, `Gem`):

- The agent is rendered normally.
- The collectible item is **shrunk** and displayed in the **top-left corner** of the cell.

![Agent Overlapping with collectible](../assets/rendering_agent_collectible.png)

#### Agent with background entities

When the agent occupies the same cell as a background entity (`Floor`, `Lava`, `Exit`, and `UnlockedDoor`):

- The background entity remains visible.
- The agent is rendered **in front** of it.

![Agent Overlapping with Background entities](../assets/rendering_agent_background.png)
