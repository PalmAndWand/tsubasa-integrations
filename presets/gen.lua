return {
  model = "tsubasa-pro",
  body = { stream = true, max_tokens = 4096 },
  -- Disable Ollama startup and use inline JSON; the file path doubles '%' in prompts.
  init = function(options) options.file = nil end,
  list_models = function() return { "tsubasa-pro", "tsubasa-fast" } end,
  command = 'curl -q --silent --show-error --fail-with-body --no-buffer'
    .. ' https://api.tsubasa.sh/v1/chat/completions'
    .. ' -H "Content-Type: application/json"'
    .. ' -H "Authorization: Bearer $TSUBASA_API_KEY" -d $body',
}
