from dataclasses import dataclass, field

from grid_universe.components.effects.immunity import Immunity
from grid_universe.components.effects.phasing import Phasing
from grid_universe.components.effects.speed import Speed
from grid_universe.components.effects.time_limit import TimeLimit
from grid_universe.components.effects.usage_limit import UsageLimit
from grid_universe.components.properties.agent import Agent
from grid_universe.components.properties.appearance import Appearance
from grid_universe.components.properties.blocking import Blocking
from grid_universe.components.properties.collectible import Collectible
from grid_universe.components.properties.collidable import Collidable
from grid_universe.components.properties.damage import Damage
from grid_universe.components.properties.exit import Exit
from grid_universe.components.properties.health import Health
from grid_universe.components.properties.inventory import Inventory
from grid_universe.components.properties.key import Key
from grid_universe.components.properties.locked import Locked
from grid_universe.components.properties.pushable import Pushable
from grid_universe.components.properties.requirable import Requirable
from grid_universe.components.properties.rewardable import Rewardable
from grid_universe.components.properties.status import Status
from grid_universe.grid.entity import BaseEntity

from grid_adventure.constants import (
    COIN_REWARD,
    DEFAULT_AGENT_HEALTH,
    HAZARD_DAMAGE,
    KEY_DOOR_ID,
    PHASING_POWERUP_DURATION,
    SHIELD_POWERUP_USAGE,
    SPEED_POWERUP_DURATION,
    SPEED_POWERUP_MULTIPLIER,
)

# Base entity classes with common components.


@dataclass(repr=False)
class CollidableEntity(BaseEntity):
    collidable: Collidable = field(default_factory=Collidable)


@dataclass(repr=False)
class BlockingEntity(BaseEntity):
    blocking: Blocking = field(default_factory=Blocking)


@dataclass(repr=False)
class PushableEntity(BaseEntity):
    pushable: Pushable = field(default_factory=Pushable)


@dataclass(repr=False)
class CollectibleEntity(BaseEntity):
    collectible: Collectible = field(default_factory=Collectible)


# Entity definitions.


@dataclass(repr=False)
class AgentEntity(CollidableEntity):
    agent: Agent = field(default_factory=Agent)
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="human", priority=0)
    )
    health: Health = field(
        default_factory=lambda: Health(
            current_health=DEFAULT_AGENT_HEALTH, max_health=DEFAULT_AGENT_HEALTH
        )
    )
    inventory: Inventory = field(default_factory=lambda: Inventory(set()))
    status: Status = field(default_factory=lambda: Status(set()))
    inventory_list: list[BaseEntity] = field(default_factory=list[BaseEntity])
    status_list: list[BaseEntity] = field(default_factory=list[BaseEntity])

    def set_health(self, health: int) -> None:
        """Set the health of the agent."""
        assert self.health is not None, (
            "AgentEntity must have a Health component to set health."
        )
        self.health = Health(current_health=health, max_health=health)


@dataclass(repr=False)
class WallEntity(BlockingEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="wall", background=True, priority=9)
    )


@dataclass(repr=False)
class ExitEntity(BaseEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="exit", priority=9)
    )
    exit: Exit = field(default_factory=Exit)


@dataclass(repr=False)
class CoinEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="coin", icon=True, priority=4)
    )
    rewardable: Rewardable = field(
        default_factory=lambda: Rewardable(amount=COIN_REWARD)
    )


@dataclass(repr=False)
class GemEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="gem", icon=True, priority=4)
    )
    requirable: Requirable = field(default_factory=Requirable)


@dataclass(repr=False)
class KeyEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="key", icon=True, priority=4)
    )
    key: Key = field(default_factory=lambda: Key(key_id=KEY_DOOR_ID))


@dataclass(repr=False)
class LockedDoorEntity(BlockingEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="door", priority=6)
    )
    locked: Locked = field(default_factory=lambda: Locked(key_id=KEY_DOOR_ID))


@dataclass(repr=False)
class UnlockedDoorEntity(BaseEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="door", priority=6)
    )


@dataclass(repr=False)
class BoxEntity(BlockingEntity, PushableEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="box", priority=2)
    )


@dataclass(repr=False)
class LavaEntity(CollidableEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="lava", priority=7)
    )
    damage: Damage = field(default_factory=lambda: Damage(amount=HAZARD_DAMAGE))


@dataclass(repr=False)
class SpeedPowerUpEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="boots", icon=True, priority=4)
    )
    speed: Speed = field(
        default_factory=lambda: Speed(multiplier=SPEED_POWERUP_MULTIPLIER)
    )
    time_limit: TimeLimit = field(
        default_factory=lambda: TimeLimit(amount=SPEED_POWERUP_DURATION)
    )


@dataclass(repr=False)
class ShieldPowerUpEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="shield", icon=True, priority=4)
    )
    immunity: Immunity = field(default_factory=Immunity)
    usage_limit: UsageLimit = field(
        default_factory=lambda: UsageLimit(amount=SHIELD_POWERUP_USAGE)
    )


@dataclass(repr=False)
class PhasingPowerUpEntity(CollectibleEntity):
    appearance: Appearance = field(
        default_factory=lambda: Appearance(name="ghost", icon=True, priority=4)
    )
    phasing: Phasing = field(default_factory=Phasing)
    time_limit: TimeLimit = field(
        default_factory=lambda: TimeLimit(amount=PHASING_POWERUP_DURATION)
    )


# Helper functions to create entities with specific configurations.


def create_agent_entity(health: int = DEFAULT_AGENT_HEALTH) -> AgentEntity:
    """Helper to create an agent entity with specified health."""
    agent = AgentEntity()
    agent.set_health(health)
    return agent
