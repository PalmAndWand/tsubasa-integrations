return {
  providers = {
    tsubasa = {
      name = "tsubasa",
      endpoint = "https://api.tsubasa.sh/v1/chat/completions",
      api_key = os.getenv("TSUBASA_API_KEY"),
      models = { "tsubasa-pro", "tsubasa-fast" },
      params = {
        chat = { max_tokens = 4096 },
        command = { max_tokens = 4096 },
      },
      topic = { model = "tsubasa-fast", params = { max_tokens = 64 } },
    },
  },
}
