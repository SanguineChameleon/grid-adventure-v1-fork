# Overview

This section explains the rules of Grid Adventure - the mechanics your agent must understand in order to play well.

## Objective 
Grid Adventure is a **turn-based** game played on a 2D grid made up of tiles. The agent starts at any location on the grid. Its objective is to **collect all gems on th grid (if any)** and **reach the exit tile with the lowest cost possible**.

## Mechanics
Each turn, the agent takes exactly one [action](actions-and-movement.md): move to an adjacent tile, pick up an item, use a key, or wait. The agent starts with some health points and loses if its HP drops to 0.

Read the rest of this section to master the game:

* [Entities](entities.md) - the objects you will encounter in the grid
* [Actions & Movement](actions-and-movement.md) - how the agent moves and interacts with objects
* [Objectives & Rewards](objectives-and-rewards.md) - what you must accomplish to win, and how score works
* [Powerups & Effects](powerups.md) - temporary boosts and how their limits work
