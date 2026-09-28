-- These environment variables override this plugin's host/key commands.
for _, name in ipairs({ "OPENAI_API_KEY", "OPENAI_API_HOST", "OPENAI_API_TYPE" }) do
  assert(not os.getenv(name), "Unset " .. name .. " before loading the Tsubasa ChatGPT.nvim preset")
end

return {
  api_key_cmd = "printenv TSUBASA_API_KEY",
  api_host_cmd = "printf https://api.tsubasa.sh",
  openai_params = { model = "tsubasa-pro", max_tokens = 4096 },
  openai_edit_params = { model = "tsubasa-pro" },
}
