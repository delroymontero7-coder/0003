# OmniCore V1–V165 Unified — Streamlit Ready

Base unificada desde V1 hasta V165, preparada para desplegar en Streamlit sin romper por imports faltantes.

## Incluye
- Base unificada V001–V165 como estructura modular
- Dashboard central
- Core mínimo funcional y estable
- Persistencia de mundo
- Factory overview (routing, templates, mission patterns, presets)
- Bridge de Unreal en modo seguro (no rompe en Streamlit Cloud)

## Qué significa "ready for deploy en Streamlit"
- La app sí corre en Streamlit Cloud
- No depende de Unreal para arrancar
- Si no existe `config/unreal_config.json`, simplemente muestra el estado local desactivado
- El control real de Unreal sigue siendo para local/Windows con Unreal instalado

## Deploy
1. Sube esta carpeta a GitHub
2. En Streamlit, selecciona `app.py`
3. Deploy

## Si quieres usar Unreal local
Crea `config/unreal_config.json` con:
```json
{
  "unreal_editor": "D:\\UE_5.7\\Engine\\Binaries\\Win64\\UnrealEditor.exe",
  "project_path": "D:\\UnrealProjects\\OmniGame\\OmniGame.uproject",
  "project_name": "OmniGame"
}
```
