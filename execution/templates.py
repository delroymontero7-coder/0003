TEMPLATES = {
    "gta_like": {"world": "urban_slice", "mission": "drive_to_point_then_trigger", "ui": "mini_hud"},
    "magic_open_world": {"world": "fantasy_slice", "mission": "reach_ruins_and_defeat_enemy", "ui": "magic_hud"},
    "default": {"world": "base_slice", "mission": "simple_delivery", "ui": "mini_hud"},
}

def get_template(name: str):
    return TEMPLATES.get(name, TEMPLATES["default"])
