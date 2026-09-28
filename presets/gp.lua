return {
  default_chat_agent = "Tsubasa Pro",
  default_command_agent = "Tsubasa Pro",
  providers = {
    tsubasa = {
      endpoint = "https://api.tsubasa.sh/v1/chat/completions",
      secret = os.getenv("TSUBASA_API_KEY"),
    },
  },
  agents = {
    {
      name = "Tsubasa Pro",
      provider = "tsubasa",
      chat = true,
      command = true,
      model = { model = "tsubasa-pro", max_completion_tokens = 4096 },
      system_prompt = "You are a helpful coding assistant.",
    },
    {
      name = "Tsubasa Fast",
      provider = "tsubasa",
      chat = true,
      command = true,
      model = { model = "tsubasa-fast", max_completion_tokens = 4096 },
      system_prompt = "You are a helpful coding assistant.",
    },
  },
}
