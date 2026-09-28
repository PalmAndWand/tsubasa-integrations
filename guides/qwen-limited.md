# Tsubasa in Qwen Code

Use [qwen-limited.json](../presets/qwen-limited.json) with
[Qwen Code 0.24.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)
for bounded headless text or local file-reading turns. It uses Qwen's existing
OpenAI-compatible custom-provider transport, a 32,768-token context, and a
2,048-token output ceiling for both Tsubasa aliases.

From the directory containing the downloaded preset, create a dedicated
profile. This leaves your home directory setting unchanged:

```sh
export QWEN_HOME="$PWD/.qwen-tsubasa"
mkdir -p "$QWEN_HOME"
cp qwen-limited.json "$QWEN_HOME/settings.json"
export QWEN_CODE_DISABLE_AUTO_UPDATE=1
```

Set `TSUBASA_API_KEY` using your normal secret-management method. The preset
reads that variable and sends prompts and the key to `api.tsubasa.sh`.

The following CLI exclusion list is required. Keep `--safe-mode` enabled:
settings such as `tools.eager` and `tools.exclude` are ignored in safe mode,
while CLI `--exclude-tools` remains effective. Excluding only the initially
visible tools can expose deferred tools and increase the request size. This
list is specific to the tested release; recheck it after upgrading Qwen Code.

```sh
qwen_excluded_tools='agent,cron_create,cron_delete,cron_list,enter_worktree,exit_worktree,get_goal,glob,grep_search,list_agents,loop_wakeup,read_mcp_resource,record_artifact,report_findings,send_message,skill,task_stop,tool_call,tool_search,update_goal,web_fetch,zoom_image'

qwen --safe-mode --model tsubasa-pro \
  --exclude-tools "$qwen_excluded_tools,read_file" \
  --max-session-turns 1 --max-tool-calls 0 --output-format json \
  --prompt 'Reply briefly with a greeting.'
```

This exact headless profile sends no tool schemas. Use `--model tsubasa-fast`
for Fast. The execution cap alone does not remove schemas; keep the exclusion
list. For a short follow-up, use the same command with `--continue` and raise
`--max-session-turns` to `2`.

For a bounded local file-reading turn, keep `read_file` out of the exclusions
and allow a small number of tool calls. Run in the directory containing the
file you want to read:

```sh
qwen --safe-mode --model tsubasa-pro \
  --exclude-tools "$qwen_excluded_tools" \
  --max-session-turns 2 --max-tool-calls 2 --output-format json \
  --prompt "Read $PWD/example.txt and summarize it briefly."
```

This profile declares only `read_file` in the tested headless release. It does
not enable automatic approval, shell execution, editing, subagents, or web
access. The file's contents, tool result, and conversation history consume the
remaining context budget; start with a small text file.

Controlled checks used the installed 0.24.6 CLI, its native configuration and
serializer, and a loopback endpoint. Both aliases decoded streamed text and
reported invalid-key errors. A text follow-up retained the assistant history.
Each alias also decoded a fragmented tool call, read a synthetic local file
through Qwen's real `read_file` implementation, sent its result back, and
decoded the final response. No request-body filtering was used. HOME remained
inherited; the fixture blocked personal-file access and external network.

All successful-profile requests passed Tsubasa's actual request schema and
context-budget check before the fixture responded. The largest captured text
request was below 21,000 estimated input tokens; the file-read round trip was
below 24,000. With 2,048 output tokens reserved, those checks left more than
9,700 and 6,700 tokens respectively. These are Tsubasa's conservative byte-based
admission estimates, not Qwen tokenizer counts or long-conversation limits.
Additional input can exhaust the remaining budget.

Live model behavior, the interactive UI, larger files, long-session compaction,
and unrestricted agent workflows have not been qualified. The original
safe-mode profile with its default tools still exceeds the service's context
preflight. See the [upstream configuration discussion](https://github.com/QwenLM/qwen-code/issues/12886)
and the [release's context-cost guidance](https://github.com/QwenLM/qwen-code/blob/753bd075a24ca886b7d0119ca53d97bd65c09e4a/docs/users/features/context-cost.md).
