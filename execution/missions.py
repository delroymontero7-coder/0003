MISSION_PATTERNS = {
    "drive_to_point_then_trigger": ["spawn_player", "spawn_vehicle", "set_destination", "trigger_contact", "complete"],
    "reach_ruins_and_defeat_enemy": ["spawn_player", "equip_magic", "reach_area", "defeat_enemy", "complete"],
    "simple_delivery": ["pickup", "travel", "dropoff", "complete"],
}

def get_pattern(name: str):
    return MISSION_PATTERNS.get(name, MISSION_PATTERNS["simple_delivery"])
