import os
import json
import streamlit as st
from core.style import inject_style
from core.security import login_gate
from core.scanner import run_scan, download_symbol
from core.storage import load_journal, save_journal, load_signals, save_signal, load_cell_memory, save_cell_memory
from modules.world_persistence.world_state import load_world, save_world
from modules.world_persistence.world_engine import tick_world
from systems_vault.vault import list_systems
from execution.factory import assemble_fast
from business.monetization import estimate_mode_cost
from unreal_bridge.launcher import unreal_available, open_unreal
from unreal_bridge.runner import run_unreal_python

st.set_page_config(page_title="OmniCore Unified V1–V165", layout="wide")
st.markdown(inject_style(), unsafe_allow_html=True)

if not login_gate():
    st.stop()

st.title("💀 OmniCore Unified V1–V165 · Streamlit Ready")
st.caption("Base unificada, estable para Streamlit, con Unreal en modo seguro.")

cfg_path = os.path.join("config", "unreal_config.json")
with st.sidebar:
    st.header("Estado")
    st.write("Unreal local configurado:", "Sí" if unreal_available() else "No")
    if os.path.exists(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            st.json(json.load(f))
    st.write("Systems Vault:", len(list_systems()))
    st.write("Costo modo normal:", estimate_mode_cost("normal"))

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Dashboard", "Factory", "World", "Unreal", "Deploy"
])

with tab1:
    st.subheader("Dashboard central")
    goal = st.text_area("Objetivo", placeholder="Ej: crear slice GTA-like Miami con misión inicial")
    if st.button("Escanear sistema"):
        st.json(run_scan())
    if st.button("Descargar símbolo demo"):
        st.json(download_symbol("BTC"))
    journal = load_journal()
    st.write("Journal entries:", len(journal))
    if st.button("Guardar nota rápida"):
        journal.append({"note": goal or "sin nota"})
        save_journal(journal)
        save_signal({"event": "note_saved", "value": goal or "sin nota"})
        mem = load_cell_memory()
        mem["last_goal"] = goal or "sin nota"
        save_cell_memory(mem)
        st.success("Nota guardada.")

with tab2:
    st.subheader("Factory")
    goal2 = st.text_input("Objetivo de ensamblaje", value="slice gta_like miami")
    if st.button("Ensamblar rápido"):
        st.json(assemble_fast(goal2))
    st.write("Systems Vault")
    st.json(list_systems())

with tab3:
    st.subheader("Persistencia de mundo")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Cargar mundo"):
            st.session_state["world"] = load_world()
            st.success("Mundo cargado")
    with c2:
        if st.button("Tick +1h"):
            world = st.session_state.get("world", load_world())
            world = tick_world(world, hours=1)
            save_world(world)
            st.session_state["world"] = world
            st.success("Mundo actualizado")
    with c3:
        if st.button("Guardar mundo"):
            world = st.session_state.get("world", load_world())
            save_world(world)
            st.success("Mundo guardado")
    if "world" in st.session_state:
        st.json(st.session_state["world"])

with tab4:
    st.subheader("Unreal 5")
    if unreal_available():
        if st.button("Abrir Unreal"):
            st.json(open_unreal())
        if st.button("Ejecutar script Unreal (seguro)"):
            st.json(run_unreal_python("unreal_bridge/ue_python/create_test_actor.py"))
    else:
        st.info("En Streamlit Cloud esta parte queda en modo seguro. Para control real de Unreal usa tu PC/Windows con config local.")

with tab5:
    st.subheader("Ready for Streamlit")
    st.markdown("""
- Esta base está preparada para deploy en Streamlit
- No depende de Unreal para arrancar
- Los módulos faltantes de `core` ya están cubiertos
- El bridge de Unreal no rompe en cloud
- La ejecución real de Unreal sigue siendo local
""")
