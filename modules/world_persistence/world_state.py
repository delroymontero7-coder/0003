import json, os, time
from typing import Any, Dict

SAVE_DIR = "workspace"
SAVE_PATH = os.path.join(SAVE_DIR, "world_state.json")

def ensure_save_dir() -> None:
    os.makedirs(SAVE_DIR, exist_ok=True)

def create_world() -> Dict[str, Any]:
    now = time.time()
    return {
        "meta": {"created_at": now, "updated_at": now, "version": "v165-unified"},
        "world": {"day": 1, "hour": 8, "weather": "clear", "global_chaos": 0.0, "global_economy": 100.0},
        "zones": {
            "miami": {"economy": 150.0, "chaos": 6.0, "population": 5000, "events": []},
            "havana": {"economy": 90.0, "chaos": 9.0, "population": 4200, "events": []},
            "capital": {"economy": 120.0, "chaos": 5.0, "population": 1200, "events": []}
        },
        "npcs": [
            {"id": "npc_001", "name": "Guardia Kael", "zone": "capital", "role": "guard", "mood": "calm", "status": "alive"},
            {"id": "npc_002", "name": "Mercader Nira", "zone": "miami", "role": "merchant", "mood": "focused", "status": "alive"}
        ],
        "missions": [{"id": "mission_001", "title": "Slice base", "status": "active", "zone": "miami"}]
    }

def save_world(state: Dict[str, Any]) -> None:
    ensure_save_dir()
    state["meta"]["updated_at"] = time.time()
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def load_world() -> Dict[str, Any]:
    ensure_save_dir()
    if not os.path.exists(SAVE_PATH):
        state = create_world()
        save_world(state)
        return state
    with open(SAVE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
