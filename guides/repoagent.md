# RepoAgent

Use RepoAgent's existing OpenAI-compatible client with a custom model name.
This is a manual configuration, not a built-in Tsubasa provider listing.
The checked client is `repoagent==0.2.0`, whose relevant source matches
[`825d988`](https://github.com/OpenBMB/RepoAgent/tree/825d988127d7bfd757237d9c4e8678d9104030f0).

Install RepoAgent in its own Python environment following its upstream setup.
Set `TSUBASA_API_KEY` to your key, then run against a Git repository:

```sh
: "${TSUBASA_API_KEY:?Set TSUBASA_API_KEY}"
OPENAI_API_KEY="$TSUBASA_API_KEY" repoagent run \
  --model tsubasa-fast \
  --base-url https://api.tsubasa.sh/v1 \
  --target-repo-path /path/to/your/repository \
  --max-thread-count 1
```

Use `--model tsubasa-pro` for Pro. RepoAgent reads `OPENAI_API_KEY`; the command
above supplies the Tsubasa key only to that invocation. RepoAgent generates
documentation and stages generated files in the target repository. Review its
changes before committing.

RepoAgent 0.2.0 exposes neither an output-token option nor a context limit for
this route. Its request omits `max_tokens`, so Tsubasa's current API default of
512 output tokens applies. Both aliases have a 32,768-token total context limit.
Large functions and caller/callee descriptions can exceed that limit; the
single-thread setting controls concurrency, not prompt size.

A controlled local HTTP fixture verified both aliases, Bearer authentication,
401 propagation from `ChatEngine.generate_doc`, and native prompt generation.
The real CLI also generated Markdown from a one-function Git repository for
each alias. The unchanged CLI requests passed Tsubasa's schema and budget check
at an estimated 2,193 input tokens plus 512 output tokens. This covers the
documentation path on that small repository; it does not qualify repository
chat, embeddings, large repositories, or live model responses.
