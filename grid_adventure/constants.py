from grid_universe.components.properties.moving import CollisionBehavior, Direction

# Default settings
DEFAULT_AGENT_HEALTH = 5
DEFAULT_DIRECTION: Direction = "down"

# Entity movement settings
ENTITY_MOVE_SPEED = 1
ENTITY_MOVE_DIRECTION: list[Direction] = ["down", "up", "left", "right"]
ENTITY_MOVE_ON_COLLISION: CollisionBehavior = "bounce"

# Reward and cost values
COIN_REWARD = 5
STEP_COST = 3

# Damage values
HAZARD_DAMAGE = 2
ENEMY_DAMAGE = 1

# Portal and key/door settings
NUM_PORTAL_PAIRS = 1
KEY_DOOR_ID = "A"

# Power-up configurations
SPEED_POWERUP_MULTIPLIER = 2
SPEED_POWERUP_DURATION = 5  # in steps
PHASING_POWERUP_DURATION = 5  # in steps
SHIELD_POWERUP_USAGE = 5  # number of hits absorbed
