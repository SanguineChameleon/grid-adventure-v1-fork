# Objectives & Rewards

The objective in Grid Adventure is to complete the following tasks:

- Collect all gems present (if any).
- Move to the exit tile.

## Reward

- Most actions incur a reward of **-3**. The final action that wins the game does not.
- Each coin collected provides a reward of **+5**.

An action that reduces the agent's HP to 0 also ends the game before this turn cost is applied.

A non-terminal `PICK_UP` action used only to collect one coin therefore changes the score by **+2**: +5 for the coin and -3 for the turn.

## Optimal solution

An optimal solution achieves all objectives while maximising the total reward. There is no requirement to finish with non-negative reward or maximum HP. Collecting a coin is worthwhile only when its reward outweighs the cost of the pickup action and any detour needed to reach it.
