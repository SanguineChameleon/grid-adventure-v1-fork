# Powerups & Effects

Powerups are collectible entities that provide **temporary boosts**. The agent can pick up and hold multiple powerups at once, including duplicates.

Every powerup expires according to one of two limit types: a **turn limit** or a **usage limit**.

## Limit types

### Turn limit

A powerup with a **turn limit** counts down by 1 after every turn, and expires when its counter reaches 0.

If the agent holds several instances of the same powerup, each instance counts down independently on every turn.

### Usage limit

A powerup with a **usage limit** counts down only when the effect is actually used, and expires when its counter reaches 0.

If the agent holds several instances of the same powerup, only one instance is used at a time.

## Speed

![Speed](../assets/boots.png)

The speed powerup lets the agent move 2 tiles in a single turn. The agent can still be blocked by objects in its path. After the effect expires, the agent returns to moving 1 tile per turn.

- **Limit:** turn limit of 5
- **Class:** `SpeedPowerUpEntity` · **Appearance name:** `"boots"`

The example shows the agent's movement once the boots are picked up. Note that walls can still restrict the agent from moving 2 tiles.

![Speed_Movement](../assets/boots_movement.gif)

!!! note "Stacking"
    Even if the agent holds multiple active speed powerups, it is still limited to moving two tiles in a single turn.

## Shield

![Shield](../assets/shields.png)

The shield protects the agent from damage. One use is consumed each time the agent lands on lava, letting it pass through unharmed.

- **Limit:** usage limit of 5
- **Class:** `ShieldPowerUpEntity` · **Appearance name:** `"shield"`

In this example the agent's health is set to 1, so it dies when stepping on lava without a shield:

![Lava_death](../assets/lava_1.gif)

By collecting the shield powerup, the agent can safely pass through the lava:

![Shield_movement](../assets/lava_2.gif)

## Phasing

![Phasing](../assets/ghosts.png)

Phasing lets the agent move through objects — walls, doors, and boxes. While it is active, the agent also takes no damage from lava.

- **Limit:** turn limit of 5
- **Class:** `PhasingPowerUpEntity` · **Appearance name:** `"ghost"`

The example shows the agent collecting the phasing powerup to pass through walls and reach the exit tile.

![Phasing_Movement](../assets/ghost_movement.gif)
