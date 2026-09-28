# Initial settings for a new Open WebUI deployment. Requires TSUBASA_API_KEY.
# Existing deployments: add the connection through Admin Settings instead.
export ENABLE_OPENAI_API=True
export OPENAI_API_BASE_URLS=https://api.tsubasa.sh/v1
export OPENAI_API_KEYS="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY first}"
export OPENAI_API_CONFIGS='{"0":{"enable":true,"auth_type":"bearer","connection_type":"external","tags":["Tsubasa"],"model_ids":["tsubasa-fast","tsubasa-pro"]}}'
