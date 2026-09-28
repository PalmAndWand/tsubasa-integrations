# Tabnine BYOAI configuration reference

For an Enterprise deployment that exposes **Models → Self-Managed → Add model**,
select the OpenAI-compatible provider and use these values:

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| Endpoint               | `https://api.tsubasa.sh/v1`                           |
| Model name             | `tsubasa-fast` or `tsubasa-pro`                       |
| Key                    | Your Tsubasa API key, entered in the credential field |
| Max Tokens Per Request | `32768`                                               |
| Max Response Tokens    | `512`                                                 |

Keep normal TLS certificate verification enabled; the public endpoint does not
require a private CA. Preserve other models and team defaults when adding this
entry. Requests go from your Tabnine deployment to `api.tsubasa.sh`.

This is a field reference, not an importable configuration or verified Tabnine
agent workflow. It follows the
[official BYOAI documentation](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/models-settings)
and
[release notes](https://docs.tabnine.com/main/administering-tabnine/release-notes).
The indexed BYOAI section and current rendered page differ; availability and
field names must be confirmed in your deployment. No administrator UI or live
inference check was performed. Code completion uses Tabnine's own model.
