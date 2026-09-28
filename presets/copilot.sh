# Source this file in the shell that starts Copilot CLI.
export COPILOT_PROVIDER_API_KEY="${TSUBASA_API_KEY:?Set TSUBASA_API_KEY first}"
export COPILOT_PROVIDER_BASE_URL=https://api.tsubasa.sh/v1
export COPILOT_PROVIDER_TYPE=openai
export COPILOT_PROVIDER_WIRE_API=completions
export COPILOT_PROVIDER_TRANSPORT=http
export COPILOT_MODEL=tsubasa-fast
export COPILOT_PROVIDER_MAX_PROMPT_TOKENS=31744
export COPILOT_PROVIDER_MAX_OUTPUT_TOKENS=1024
