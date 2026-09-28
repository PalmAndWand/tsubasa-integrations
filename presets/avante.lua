return {
  provider = "tsubasa",
  providers = {
    tsubasa = {
      __inherited_from = "openai",
      endpoint = "https://api.tsubasa.sh/v1",
      api_key_name = "TSUBASA_API_KEY",
      model = "tsubasa-pro",
      context_window = 32768,
      use_response_api = false,
      disable_tools = true,
      extra_request_body = { max_completion_tokens = 16384 },
    },
  },
}
