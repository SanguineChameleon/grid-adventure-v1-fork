# Game Tab

The Game tab is where you play and interact with levels. It provides real-time visual feedback, player status, and controls for playing manually or running your own agent.

![Grid-play-game-tab](../assets/grid-play-game-tab-l.png)

## Interface layout

The tab is divided into three columns:

| Column | Purpose |
| -- | -- |
| Left | Player status |
| Middle | Rendered game and observation information |
| Right | Level info and agent controls |

### Left column: player status

Displays your current status:

| Indicator | Description |
|-----------|-------------|
| **Total Reward** | Your accumulated score / reward points |
| **Health Points** | Current HP, with damage notifications |
| **PowerUp Status** | Active temporary effects |
| **Inventory** | Items you have collected |

### Middle column: game view

The central area shows:

- **Game visualisation:** real-time rendering of the grid world
- **Observation info:** a JSON display of the current ImageObservation's `info` dictionary

### Right column: level information and controls

Provides context about the current level and how to control the agent:

| Section | Description |
|---------|-------------|
| **New Level** | Rebuild the current level with a new seed |
| **Level Rules** | Movement type (e.g. cardinal directions) |
| **Objective** | What you need to do to win |
| **Turn Counter** | Current turn and turn limit |
| **Controls** | Switch between the Human and AI Agent tabs |

## Human mode

Use the on-screen buttons or the keyboard to play. The arrow keys and WASD move the agent. Press E to pick up items, F to use a key, and Q to wait.

## AI Agent Mode

Open the **AI Agent** tab to test your own [agent](../agent/agent-class.md).

### Loading an agent

1. Click the **Settings** button to open the agent dialog.
2. Paste your agent code, or use the provided template.
3. Choose whether `Agent.step` receives ImageObservation or GridState.
4. Click **Load** to compile and initialize the agent.

### Running the agent

- Click **Step** to execute one action from your agent.
- The **Vision** display is enabled when the agent defines a callable [`parse`](../agent/agent-class.md#parse-parse-optional) method.
- In ImageObservation mode, the **Vision** display renders the GridState returned by [`parse`](../agent/agent-class.md#parse-parse-optional).
- In GridState mode, **Vision** renders the current GridState directly and does not call `parse`.
- The **Info** display shows debug information from your agent's [`info`](../agent/agent-class.md#info-info-optional) method.

![Grid-play-game-tab-vision](../assets/grid-play-game-tab-vision.png)
