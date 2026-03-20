SYSTEMS_VAULT = {
    "player_base": {"type": "character", "description": "Movimiento básico + cámara"},
    "camera_third_person": {"type": "camera", "description": "Cámara tercera persona"},
    "mission_base": {"type": "mission", "description": "Misión base reutilizable"},
    "ui_base": {"type": "ui", "description": "HUD mínimo"},
    "enemy_base": {"type": "npc", "description": "Enemigo simple"},
    "world_slice_base": {"type": "world", "description": "Slice pequeño"},
    "vehicle_base": {"type": "vehicle", "description": "Movilidad tipo vehículo"},
    "magic_combat_base": {"type": "combat", "description": "Ataque mágico base"},
}

def list_systems():
    return list(SYSTEMS_VAULT.keys())

def get_system(name: str):
    return SYSTEMS_VAULT.get(name)
