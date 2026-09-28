// PRELAUNCH: agent use is blocked pending tool and context-budget qualification.
// Letta 0.33.2 sends tool schemas even with --toolset none. Its mod API has no
// provider-request interception; this distribution gate is not a runtime guard.
export default function activate(letta) {
  if (!letta.capabilities.providers) return
  return letta.providers.register("tsubasa", {
  "name": "Tsubasa",
  "description": "Prelaunch: agent use is blocked pending tool and context-budget qualification.",
  "api": "openai-completions",
  "baseUrl": "https://api.tsubasa.sh/v1",
  "apiKey": "TSUBASA_API_KEY",
  "authHeader": true,
  "models": [
    {
      "id": "tsubasa-fast",
      "name": "Tsubasa Fast",
      "reasoning": false,
      "input": [
        "text"
      ],
      "cost": {
        "input": 0.2,
        "output": 1,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 32768,
      "maxTokens": 8192,
      "compat": {
        "supportsStore": false,
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false,
        "supportsLongCacheRetention": false
      }
    },
    {
      "id": "tsubasa-pro",
      "name": "Tsubasa Pro",
      "reasoning": false,
      "input": [
        "text"
      ],
      "cost": {
        "input": 0.5,
        "output": 4,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 32768,
      "maxTokens": 16384,
      "compat": {
        "supportsStore": false,
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false,
        "supportsLongCacheRetention": false
      }
    }
  ],
  "connect": {
    "fields": [
      {
        "key": "apiKey",
        "label": "Tsubasa API Key",
        "secret": true
      }
    ]
  }
})
}
