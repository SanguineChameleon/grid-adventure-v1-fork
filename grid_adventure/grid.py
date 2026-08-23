from __future__ import annotations

from grid_universe.actions import Action
from grid_universe.grid.convert import from_state as base_from_state
from grid_universe.grid.convert import to_state as base_to_state
from grid_universe.grid.entity import BaseEntity, copy_entity_components
from grid_universe.grid.gridstate import GridState
from grid_universe.grid.step import step as base_step
from grid_universe.state import State

# Specialized entity classes from Grid Adventure
from grid_adventure.entities import (
    AgentEntity,
    BoxEntity,
    CoinEntity,
    ExitEntity,
    GemEntity,
    KeyEntity,
    LavaEntity,
    LockedDoorEntity,
    MovingBoxEntity,
    PhasingPowerUpEntity,
    PortalEntity,
    RobotEntity,
    ShieldPowerUpEntity,
    SpeedPowerUpEntity,
    UnlockedDoorEntity,
    WallEntity,
)

SpecializedTypes = (
    AgentEntity,
    WallEntity,
    ExitEntity,
    CoinEntity,
    GemEntity,
    KeyEntity,
    LockedDoorEntity,
    UnlockedDoorEntity,
    PortalEntity,
    BoxEntity,
    MovingBoxEntity,
    RobotEntity,
    LavaEntity,
    SpeedPowerUpEntity,
    ShieldPowerUpEntity,
    PhasingPowerUpEntity,
)


def _specialize_single(obj: BaseEntity) -> BaseEntity:
    """
    Return a specialized Grid Adventure entity based on components/appearance.
    Keeps obj unchanged if it is already specialized.
    """
    if isinstance(obj, SpecializedTypes):
        return obj

    def has(name: str) -> bool:
        return getattr(obj, name, None) is not None

    app_name: str | None = getattr(getattr(obj, "appearance", None), "name", None)

    # Agent
    if has("agent"):
        return copy_entity_components(obj, AgentEntity(), preserve_entity_id=True)

    # Exit
    if has("exit"):
        return copy_entity_components(obj, ExitEntity(), preserve_entity_id=True)
    # Doors (Locked vs Unlocked)
    if app_name == "door":
        if has("locked"):
            return copy_entity_components(
                obj, LockedDoorEntity(), preserve_entity_id=True
            )
        return copy_entity_components(
            obj, UnlockedDoorEntity(), preserve_entity_id=True
        )

    # Key
    if has("key"):
        return copy_entity_components(obj, KeyEntity(), preserve_entity_id=True)

    # Portal
    if has("portal"):
        return copy_entity_components(obj, PortalEntity(), preserve_entity_id=True)
    # Collectibles
    if has("collectible"):
        # Power-ups first
        if has("speed"):
            return copy_entity_components(
                obj, SpeedPowerUpEntity(), preserve_entity_id=True
            )
        if has("immunity"):
            return copy_entity_components(
                obj, ShieldPowerUpEntity(), preserve_entity_id=True
            )
        if has("phasing"):
            return copy_entity_components(
                obj, PhasingPowerUpEntity(), preserve_entity_id=True
            )
        # Gem vs coin
        if app_name == "core" or has("requirable"):
            return copy_entity_components(obj, GemEntity(), preserve_entity_id=True)
        return copy_entity_components(obj, CoinEntity(), preserve_entity_id=True)
    # Boxes: moving vs static
    if app_name == "box":
        if has("moving"):
            return copy_entity_components(
                obj, MovingBoxEntity(), preserve_entity_id=True
            )
        return copy_entity_components(obj, BoxEntity(), preserve_entity_id=True)

    # Hazards / monsters
    if app_name == "lava":
        return copy_entity_components(obj, LavaEntity(), preserve_entity_id=True)
    if app_name == "monster" or app_name == "robot":
        return copy_entity_components(obj, RobotEntity(), preserve_entity_id=True)

    if app_name == "wall":
        return copy_entity_components(obj, WallEntity(), preserve_entity_id=True)

    # Fallback
    return obj


def _specialize_nested_list(items: list[BaseEntity] | None) -> list[BaseEntity]:
    """Specialize nested inventory/status entity lists."""
    if not items:
        return []
    return [_specialize_single(item) for item in items]


def specialize_entities(gridstate: GridState) -> GridState:
    """
    Returns a new GridState with entities replaced by specialized Grid Adventure subclasses.
    Also remaps cross-entity references to the new instances.
    """
    new_grid_state = GridState(
        width=gridstate.width,
        height=gridstate.height,
        movement=gridstate.movement,
        objective=gridstate.objective,
        seed=gridstate.seed,
        step_cost=gridstate.step_cost,
        turn=gridstate.turn,
        score=gridstate.score,
        win=gridstate.win,
        lose=gridstate.lose,
        message=gridstate.message,
        turn_limit=gridstate.turn_limit,
    )

    # First pass: specialize and map original object id -> new specialized object
    obj_map: dict[int, BaseEntity] = {}
    for x in range(gridstate.width):
        for y in range(gridstate.height):
            specialized_cell: list[BaseEntity] = []
            for orig_obj in gridstate.grid[x][y]:
                spec_obj = _specialize_single(orig_obj)

                # Specialize nested lists if attributes exist (inventory_list, status_list)
                if hasattr(spec_obj, "inventory_list"):
                    inv_list = getattr(spec_obj, "inventory_list", None)
                    if inv_list:
                        spec_obj.inventory_list = _specialize_nested_list(inv_list)
                if hasattr(spec_obj, "status_list"):
                    st_list = getattr(spec_obj, "status_list", None)
                    if st_list:
                        spec_obj.status_list = _specialize_nested_list(st_list)

                obj_map[id(orig_obj)] = spec_obj
                specialized_cell.append(spec_obj)
            for spec_obj in specialized_cell:
                new_grid_state.add((x, y), spec_obj)

    # Second pass: remap cross-entity references to specialized targets/pairs
    for x in range(new_grid_state.width):
        for y in range(new_grid_state.height):
            for spec_obj in new_grid_state.grid[x][y]:
                # pathfind_target_ref
                if hasattr(spec_obj, "pathfind_target_ref"):
                    old_ref = getattr(spec_obj, "pathfind_target_ref", None)
                    if old_ref is not None:
                        new_ref = obj_map.get(id(old_ref))
                        if new_ref is not None:
                            spec_obj.pathfind_target_ref = new_ref
                # portal_pair_ref (ensure bidirectional)
                if isinstance(spec_obj, PortalEntity):
                    old_mate = spec_obj.portal_pair_ref
                    if old_mate is not None:
                        new_mate = obj_map.get(id(old_mate))
                        if isinstance(new_mate, PortalEntity):
                            spec_obj.portal_pair_ref = new_mate
                            if new_mate.portal_pair_ref is None:
                                new_mate.portal_pair_ref = spec_obj

    return new_grid_state


def from_state(state: State) -> GridState:
    """Convert a State to a specialized GridState using Grid Adventure entity subclasses."""
    base_grid_state = base_from_state(state)
    return specialize_entities(base_grid_state)


def to_state(gridstate: GridState) -> State:
    """Convert a GridState (with specialized Grid Adventure entities) to a State."""
    return base_to_state(gridstate)


def step(gridstate: GridState, action: Action) -> GridState:
    """Perform one step in the GridState using the base step function."""
    return specialize_entities(base_step(gridstate, action))


__all__ = ["GridState", "from_state", "specialize_entities", "step", "to_state"]
