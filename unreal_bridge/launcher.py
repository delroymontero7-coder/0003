import json, os, subprocess

CONFIG_PATH = os.path.join("config", "unreal_config.json")

def unreal_available():
    return os.path.exists(CONFIG_PATH)

def load_config():
    if not unreal_available():
        return None
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def open_unreal():
    cfg = load_config()
    if not cfg:
        return {"status": "disabled", "message": "Unreal local no configurado en este entorno"}
    editor = cfg["unreal_editor"]
    project = cfg["project_path"]
    if not os.path.exists(editor):
        return {"status": "error", "message": f"No existe UnrealEditor.exe: {editor}"}
    if not os.path.exists(project):
        return {"status": "error", "message": f"No existe el proyecto: {project}"}
    try:
        subprocess.Popen([editor, project])
        return {"status": "ok", "message": "Unreal abierto correctamente"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
