# Tsubasa in Deep Agents Code

Use [deepagents-code.toml](../presets/deepagents-code.toml) with
[Deep Agents Code](https://github.com/langchain-ai/deepagents/tree/main/libs/code)
for a bounded headless text turn. The named provider loads the existing
`langchain_openai:ChatOpenAI` class. It uses Chat Completions, reads
`TSUBASA_API_KEY`, and sends the key and prompts to `api.tsubasa.sh`.

Validation used `deepagents-code==0.1.77`. Install that official package in your
usual isolated Python environment. From the directory containing the downloaded
preset, create a separate native profile:

```sh
export DEEPAGENTS_HOME="$PWD/.deepagents-tsubasa"
mkdir -p "$DEEPAGENTS_HOME"
cp deepagents-code.toml "$DEEPAGENTS_HOME/config.toml"
export DEEPAGENTS_CODE_AUTO_UPDATE=false
```

Set `TSUBASA_API_KEY` using your normal secret-management method. Run the
bounded profile with these native flags:

```sh
dcode --model tsubasa:tsubasa-pro \
  --no-mcp --no-interpreter --allow-fs-tools read_file \
  --max-retries 0 --max-turns 1 --timeout 35 \
  -n 'Reply briefly with a greeting.'
```

Use `tsubasa:tsubasa-fast` for Fast. Keep the three tool-control flags: the
stock headless request was too large for Tsubasa's context admission check.
The bounded profile still declares six tools: `read_file`, `task`,
`compact_conversation`, `update_goal`, `fetch_url`, and
`get_current_thread_id`. This profile limits filesystem tools to reading;
headless mode can execute other enabled tools without interactive approvals.
The qualification below covers text responses, with no tool calls requested.

The preset caps each response at 2,048 tokens and declares a 30,720-token input
budget, reserving the rest of the combined 32,768-token context for output.
It selects Tsubasa Fast for the compaction helper and restricts model selection
to the two Tsubasa aliases. Long-session compaction was not exercised.

Keep `openai_prompt_cache_key = false`. Deep Agents Code otherwise adds a
per-thread `prompt_cache_key`, which Tsubasa's request schema rejects. This is
the client's supported opt-out; the transport does not edit outgoing bodies.
Keep `use_responses_api = false` so the shared class uses Chat Completions.

The released client's model loader completed eight controlled JSON/SSE calls
covering both aliases and HTTP 401 errors. It also rejected a missing Tsubasa
credential before HTTP, despite an unrelated OpenAI key being present.
The actual bounded `dcode` command completed a text turn on both aliases.
With an invalid key, both commands exited unsuccessfully and displayed
`OpenAIAuthenticationError`; the CLI replaced the original 401 message with
its generic internal-error message.
Its initial request was estimated at no more than 22,840 input tokens plus
2,048 output, leaving at least 7,880 tokens. These are Tsubasa's conservative
admission estimates; added instructions, history, or tool results consume the
remaining budget.

Every successful-profile serialized request passed Tsubasa's actual schema
and context check before the fixture replied. Verification used synthetic
keys, an inherited HOME, native `DEEPAGENTS_HOME`, and sandbox restrictions on
personal files and external network. Installed loader/configuration files
matched the inspected source at
[`40873baa880133ae19ea921239ad9142c1972f4f`](https://github.com/langchain-ai/deepagents/tree/40873baa880133ae19ea921239ad9142c1972f4f).

Live inference, tools, the interactive UI, unrestricted agent tasks, and
long-session behavior have not been qualified. With the cache-key opt-out but
without the tool-control flags, the stock request still exceeded the budget
at about 45,688 input tokens plus 2,048 output.
