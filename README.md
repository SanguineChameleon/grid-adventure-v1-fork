# Grid Adventure: Variant 1

A gridworld puzzle-adventure game built on the Grid Universe engine.

Navigate grid-based levels, collect coins and keys, avoid hazards, and find the exit. Features powerups (speed, phasing, shields), and unlockable doors.

Comprehensive documentation is available at the [Grid Adventure V1 Docs](https://grid-universe.github.io/grid-adventure-v1/): 

- **Player Guide**: entities, movements, objectives, and examples.
- **Agent developer docs**: environment API, representations, actions, and examples.

## Install

```bash
pip install -e .
pip install -e ".[play]"  # Includes grid-play for playing the game
```

Requires Python 3.13+.

## Play

**Intro Levels:**
```bash
grid-play --plugin grid_adventure.play.intro
```
Play through pre-built levels with varying difficulty.

**Level Editor:**
```bash
grid-play --plugin grid_adventure.play.editor
```
Create custom levels with drag-and-drop entity placement.

Use the Config tab to change levels or customize settings.

## Features

- **Entities:** Player, walls, floors, exits, coins, keys, doors, hazards
- **Powerups:** Speed boost, phasing (walk through walls), damage immunity shield
- **Mechanics:** Health system, inventory, time limits, pushable blocks
- **Editor:** Visual level design with real-time testing

## Development

Run tests:
```bash
pip install -e ".[dev]"
pytest
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
