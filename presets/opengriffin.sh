# Source this file after setting TSUBASA_API_KEY in your shell or secret manager.
# Chat only; this upstream connector does not return tool-call results.
export OPENGRIFFIN_PROVIDER=custom
export OPENGRIFFIN_MODEL=tsubasa-pro
export CUSTOM_BASE_URL=https://api.tsubasa.sh/v1
export CUSTOM_API_KEY="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY before loading this preset}"
