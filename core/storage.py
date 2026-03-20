import json
import os

WORKSPACE_DIR = "workspace"
JOURNAL_PATH = os.path.join(WORKSPACE_DIR, "journal.json")
SIGNALS_PATH = os.path.join(WORKSPACE_DIR, "signals.json")
MEMORY_PATH = os.path.join(WORKSPACE_DIR, "cell_memory.json")

os.makedirs(WORKSPACE_DIR, exist_ok=True)

def _load_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def _save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return True

def load_journal():
    return _load_json(JOURNAL_PATH, [])

def save_journal(data):
    return _save_json(JOURNAL_PATH, data)

def load_signals():
    return _load_json(SIGNALS_PATH, [])

def save_signal(signal):
    signals = load_signals()
    signals.append(signal)
    return _save_json(SIGNALS_PATH, signals)

def load_cell_memory():
    return _load_json(MEMORY_PATH, {})

def save_cell_memory(memory):
    return _save_json(MEMORY_PATH, memory)
