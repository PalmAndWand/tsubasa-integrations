# Tsubasa in application connectors

These settings use the applications' existing OpenAI-compatible providers. They
create manually configured connections; they do not add Tsubasa to the
applications' stock provider catalogs.

As of September 27, 2026, Tsubasa's public inference service is unavailable. The
public `/v1/models` route returns HTTP 404 in website-only mode, and no live
inference pass is claimed. The settings below are prepared for an enabled
service. A model name appearing in a selector does not establish availability.

Use the public API base URL `https://api.tsubasa.sh/v1` and a Tsubasa API key.
Keep the key in the application's credential field or secret manager. The shell
presets require `TSUBASA_API_KEY` and fail when it is absent.

| Model ID       | Display name | Context window | Maximum output |
| -------------- | ------------ | -------------- | -------------- |
| `tsubasa-fast` | Tsubasa Fast | 32,768 tokens  | 8,192 tokens   |
| `tsubasa-pro`  | Tsubasa Pro  | 32,768 tokens  | 16,384 tokens  |

Start with plain text chat and an output limit of 128 tokens. Leave tools,
vision, embeddings, and structured output disabled until their live behavior has
been qualified. Input and requested output must fit the context window.

## AnythingLLM

In **Settings**, select **Generic OpenAI** in the LLM provider selection and
set:

| Field                | Value                            |
| -------------------- | -------------------------------- |
| Base URL             | `https://api.tsubasa.sh/v1`      |
| API Key              | Your Tsubasa API key             |
| Selected Model       | `tsubasa-pro` or `tsubasa-fast`  |
| Model context window | `32768`                          |
| Max Tokens           | `4096` or a smaller output limit |

If model discovery returns no models, the current interface offers a free-form
**Selected Model** field. Enter one of the public IDs above and save. This is a
configuration fallback; it does not make an unavailable API ready to chat.

For a server configured through environment variables, source
[anythingllm.sh](presets/anythingllm.sh) before starting the server:

```sh
# Set TSUBASA_API_KEY through your shell or secret manager first.
. presets/anythingllm.sh
```

The preset selects `generic-openai`, defaults to Pro, sets a 4,096-token output
limit, and adds `generic-openai` to `PROVIDER_DISABLE_NATIVE_TOOL_CALLING`. To
select Fast, set `GENERIC_OPEN_AI_MODEL_PREF=tsubasa-fast` after sourcing. For
an existing installation, update its saved settings as well; stored
configuration can override the initial environment. Keep the embedding provider
separate and use ordinary workspace chat without agent tools.

Verified against
[AnythingLLM's generic connector at `128a015`](https://github.com/Mintplex-Labs/anything-llm/blob/128a01575a50f0284aeca75a93399b6fb1db0328/server/utils/AiProviders/genericOpenAi/index.js).
The production provider factory selects this connector for `generic-openai`.

## Open WebUI

In **Settings > Admin > Connections**, add an OpenAI API connection:

| Field          | Value                                           |
| -------------- | ----------------------------------------------- |
| URL            | `https://api.tsubasa.sh/v1`                     |
| API Key        | Your Tsubasa API key                            |
| Authentication | Bearer                                          |
| Provider       | Default                                         |
| API Type       | Chat Completions                                |
| Model IDs      | Add `tsubasa-fast` and `tsubasa-pro` separately |
| Tags           | `Tsubasa` (optional)                            |

Save the connection. The manually supplied IDs can appear in the model selector
without a successful `/models` response. Select one for plain chat only after
the API is enabled. Leave tools, attachments, and other provider capabilities
disabled for this connection's models.

For a new deployment using environment configuration, source
[open-webui.sh](presets/open-webui.sh) before starting Open WebUI. It defines a
single connection at index `0`, so merge it with your existing connection lists
instead of replacing them. For an existing deployment, use the Admin settings:
persisted configuration can take precedence over environment variables.

The route follows
[Open WebUI's OpenAI-compatible setup guide](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible).
The controlled check currently covers the real frontend HTTP helper with an
explicit endpoint. Normal chat also passes through `/api/chat/completions` and
backend middleware; that complete application route remains unverified here.

## Dify

Install the **OpenAI-API-compatible** plugin by `langgenius` from Dify's plugin
marketplace. In **Settings > Model Providers**, open that provider and add an
LLM model for each public ID.

[dify.json](presets/dify.json) is a field reference, not an importable Dify app
DSL. Copy each model's credential values into the provider form, and enter your
API key separately. The reference contains no secret.

| Setting                          | Value                            |
| -------------------------------- | -------------------------------- |
| Model name / endpoint model name | `tsubasa-fast` or `tsubasa-pro`  |
| Display name                     | Tsubasa Fast or Tsubasa Pro      |
| API endpoint URL                 | `https://api.tsubasa.sh/v1`      |
| Mode                             | Chat                             |
| Context size                     | `32768`                          |
| Maximum tokens                   | `8192` for Fast; `16384` for Pro |
| Token parameter name             | `max_tokens`                     |
| User identity support            | Not supported (`no_support`)     |
| Stream usage                     | Enabled                          |
| Function calling                 | No call                          |
| Streaming function calling       | Not supported                    |
| Vision                           | Not supported                    |
| Structured output                | Not supported                    |
| Compatibility mode               | Strict                           |

Keep the default Chat Completions API type. User identity must be disabled:
otherwise the plugin can send a `user` field that Tsubasa's strict request
schema rejects. Use the configured model in a text LLM node and set a small
output limit for the first request. Provider validation requires an enabled
endpoint; it cannot succeed against the current public website-only service.

Verified against the official plugin
[version 0.0.68 at `f6b4a6a`](https://github.com/langgenius/dify-official-plugins/tree/f6b4a6a945b4e5909d7c9ceb4c593505f1a3238d/models/openai_api_compatible).

## Langflow

The **OpenAI Compatible** provider is included with current Langflow. In
**Settings > Model Providers**, select it and set:

| Field    | Value                       |
| -------- | --------------------------- |
| Base URL | `https://api.tsubasa.sh/v1` |
| API Key  | Your Tsubasa API key        |

Save, then enable the Tsubasa models under **Language Models**. In a **Language
Model** component, select **OpenAI Compatible** and `tsubasa-pro` or
`tsubasa-fast`. Set the component's output token limit to 128 for an initial
plain text request.

Model discovery requires a successful `/v1/models` response, so this setup
cannot populate the live selector while the public service is unavailable.
Langflow's generic discovery also offers every returned model as an embedding
model and assumes chat models support tools. Those generic flags do not qualify
Tsubasa: leave embedding entries disabled and avoid Agent/tool usage.

For a process configured through environment variables, source
[langflow.sh](presets/langflow.sh) before starting Langflow or LFX. It sets
`OPENAI_COMPATIBLE_BASE_URL` and `OPENAI_COMPATIBLE_API_KEY`. Existing per-user
provider settings take precedence; update them in the UI when applicable.

The steps follow the
[upstream bundle documentation at `df9711c`](https://github.com/langflow-ai/langflow/blob/df9711c952a8e798e8fbbad8f25fe60be5ff6018/docs/docs/Components/bundles-openai-compatible.mdx).

## Controlled verification

The checks summarized below ran against pinned upstream sources with synthetic
keys and a local HTTP responder. Captured requests were validated against
Tsubasa's request schema and context/output limits; the checks also decoded
responses and rejected a wrong key. This public catalog contains the settings
and results, not the private API implementation or its verification scripts.

| App                  | Source tested                              | Verified path                                                                                | Remaining scope                                           |
| -------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| AnythingLLM          | `128a01575a50f0284aeca75a93399b6fb1db0328` | Real generic provider, both models, text/SSE, 401 and key isolation                          | Full app UI, retrieval, and live inference                |
| Open WebUI           | `8bd8b4fac5e059578ac0c74b3c18d11139f88b7d` | Real frontend helper, both models, decoded JSON, 401                                         | Backend chat middleware, full UI, SSE, and live inference |
| Dify official plugin | `f6b4a6a945b4e5909d7c9ceb4c593505f1a3238d` | Real model schema/provider, both models, text/SSE, 401 and key isolation                     | Plugin installation UI, full Dify app, and live inference |
| Langflow             | `df9711c952a8e798e8fbbad8f25fe60be5ff6018` | Real extension loader, discovery, environment credentials, model construction, text/SSE, 401 | Full server/UI and live inference                         |

The Python apps were checked in separate environments because Dify and LFX
require incompatible versions of `packaging`. No package constraint was
overridden.

The checked Dify runtime uses Python 3.12 and `dify-plugin==0.10.2`; Langflow
uses its source LFX 1.12.3 and OpenAI Compatible bundle 0.1.5 with
`langchain-openai==1.6.6`. The Node check uses AnythingLLM's `openai==4.95.1`,
`mock-require`, and `esbuild`. The AnythingLLM fixture replaces only unused
embedding, user persistence, and application-shell dependencies.
