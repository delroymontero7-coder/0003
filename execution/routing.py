GAME_PROFILES = {
    "gta_like": ["player_base", "camera_third_person", "mission_base", "ui_base", "enemy_base", "world_slice_base", "vehicle_base"],
    "magic_open_world": ["player_base", "camera_third_person", "mission_base", "ui_base", "enemy_base", "world_slice_base", "magic_combat_base"],
    "default": ["player_base", "camera_third_person", "mission_base", "ui_base", "enemy_base", "world_slice_base"],
}

def detect_profile(goal: str) -> str:
    g = goal.lower()
    if "gta" in g or "carro" in g or "vehiculo" in g or "vehículo" in g:
        return "gta_like"
    if "magia" in g or "medieval" in g:
        return "magic_open_world"
    return "default"

def route_systems(goal: str):
    profile = detect_profile(goal)
    return {"profile": profile, "systems": GAME_PROFILES[profile]}
