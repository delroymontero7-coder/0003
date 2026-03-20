import random
from typing import Dict, Any

def tick_world(state: Dict[str, Any], hours: int = 1) -> Dict[str, Any]:
    state["world"]["hour"] += hours
    while state["world"]["hour"] >= 24:
        state["world"]["hour"] -= 24
        state["world"]["day"] += 1
    state["world"]["weather"] = random.choice(["clear", "rain", "fog", "storm"])
    for zone in state["zones"].values():
        zone["chaos"] = max(0.0, zone["chaos"] + random.uniform(-1.0, 2.0))
        zone["economy"] = max(0.0, zone["economy"] + random.uniform(-2.0, 3.0))
    state["world"]["global_chaos"] = round(sum(z["chaos"] for z in state["zones"].values()) / len(state["zones"]), 2)
    state["world"]["global_economy"] = round(sum(z["economy"] for z in state["zones"].values()) / len(state["zones"]), 2)
    return state
