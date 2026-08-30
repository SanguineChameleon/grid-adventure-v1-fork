# Grid Play

**Grid Play** is a browser-based playground for Grid Adventure. You can use it to run and debug your agent, play levels yourself, and design new ones.

Grid Play lets you:

- **Play** levels with keyboard or button controls
- **Configure** levels with adjustable parameters, or build your own
- **Test your agent** one step at a time and inspect its chosen action and optional debugging output

## Launch Grid Play

From the repository root, install Grid Adventure with the Grid Play dependency:

```bash
pip install -e ".[play]"
```

Then launch the intro levels and level editor:

```bash
grid-play --plugin grid_adventure.play.intro --plugin grid_adventure.play.editor
```

## The three tabs

Grid Play is organized into three tabs:

| Tab | Purpose |
|-----|---------|
| [**Game**](game.md) | Play with buttons or keyboard, or run your agent one step at a time |
| [**Config**](config.md) | Choose and configure the level |
| [**State**](state.md) | Inspect the available internal state data for debugging |

## Quick start

1. Open the **[Config](config.md)** tab and select a level source.
2. Adjust the parameters as desired and click **Save**.
3. Switch to the **[Game](game.md)** tab to start playing.
4. Use the keyboard or buttons to move and interact. To test your own agent, open the **AI Agent** tab, load it in **Settings**, and click **Step**.
