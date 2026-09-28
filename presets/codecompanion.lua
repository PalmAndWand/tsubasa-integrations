return {
  adapters = {
    http = {
      tsubasa = function()
        return require("codecompanion.adapters").extend("openai_compatible", {
          name = "tsubasa",
          formatted_name = "Tsubasa",
          opts = { tools = false, vision = false },
          env = {
            url = "https://api.tsubasa.sh/v1",
            chat_url = "/chat/completions",
            models_endpoint = "/models",
            api_key = "TSUBASA_API_KEY",
          },
          schema = { model = { default = "tsubasa-pro", choices = { "tsubasa-fast", "tsubasa-pro" } } },
        })
      end,
    },
  },
  interactions = { chat = { adapter = "tsubasa" }, inline = { adapter = "tsubasa" } },
}
