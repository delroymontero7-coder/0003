from execution.routing import route_systems
from execution.templates import get_template
from execution.missions import get_pattern

def assemble_fast(goal: str):
    routed = route_systems(goal)
    template = get_template(routed["profile"])
    mission_flow = get_pattern(template["mission"])
    return {
        "profile": routed["profile"],
        "systems": routed["systems"],
        "template": template,
        "mission_flow": mission_flow,
        "status": "assembled_fast"
    }
