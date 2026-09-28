return {
  provider = "openai_compatible",
  n_completions = 1,
  provider_options = {
    openai_compatible = {
      name = "Tsubasa",
      model = "tsubasa-fast",
      api_key = "TSUBASA_API_KEY",
      end_point = "https://api.tsubasa.sh/v1/chat/completions",
      stream = true,
      optional = { max_tokens = 256 },
    },
  },
}
