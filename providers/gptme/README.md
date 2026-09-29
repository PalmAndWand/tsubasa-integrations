# Tsubasa provider for gptme

This package registers Tsubasa through gptme's native provider entry point. It
reuses the existing OpenAI-compatible client and supplies the two public model
names, 32,768-token context budgets, output limits, and published prices. It
reads only `TSUBASA_API_KEY` for Tsubasa authentication.

The provider uses Chat Completions and advertises text-only models. Vision,
reasoning, parallel tools, strict tools and Responses API flags are disabled.
gptme can still request streaming through its existing transport.

From a checkout of this repository, install into the same Python environment as
gptme:

```sh
python -m pip install ./providers/gptme
```

Set `TSUBASA_API_KEY` securely in your environment, then choose either model:

```sh
gptme -m tsubasa/tsubasa-fast
gptme -m tsubasa/tsubasa-pro
```

Fast allows 8,192 output tokens and Pro allows 16,384, within each model's combined
32,768-token input/output budget. The listed USD prices per million input/output
tokens are $0.20/$1.00 for Fast and $0.50/$4.00 for Pro. Check
[Tsubasa's documentation](https://tsubasa.sh/docs) for current availability and
pricing. Conversation history and tool definitions consume the context budget.

To test the installed entry point without live inference:

```sh
python -m pip install -e './providers/gptme[test]'
python -m pytest providers/gptme/tests
```

Before publishing a package release, run a live smoke test as described in
[gptme's provider integration guide](https://github.com/gptme/gptme/blob/f7bb34871442bb69d3cbecde49c7ce1f2e22517a/docs/providers-integration.rst).
