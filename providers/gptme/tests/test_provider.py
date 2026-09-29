"""Installed native entry-point and credential-isolation checks; no live calls."""

from importlib.metadata import entry_points

import pytest

from gptme.config import Config, UserConfig, set_config
from gptme.llm.llm_openai import clients, init
from gptme.llm.models import get_model
from gptme.llm.provider_plugins import clear_plugin_cache, get_provider_plugin
from gptme_provider_tsubasa import provider


def test_installed_entry_point_resolves_both_model_budgets():
    entry = next(
        ep for ep in entry_points(group="gptme.providers") if ep.name == "tsubasa"
    )
    assert entry.load() is provider
    clear_plugin_cache()
    set_config(Config(user=UserConfig()))
    assert get_provider_plugin("tsubasa") is provider
    for alias, limit in (("tsubasa-fast", 8192), ("tsubasa-pro", 16384)):
        model = get_model(f"tsubasa/{alias}")
        assert model.context == 32768
        assert model.max_output == limit
        assert not any(
            (
                model.supports_vision,
                model.supports_reasoning,
                model.supports_responses_api,
                model.supports_parallel_tool_calls,
                model.supports_strict_tools,
                model.supports_streaming,
            )
        )


def test_missing_key_does_not_reuse_openai_credential(monkeypatch):
    clients.pop("tsubasa", None)
    monkeypatch.delenv("TSUBASA_API_KEY", raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "unrelated-provider-fixture")
    config = Config(user=UserConfig())
    set_config(config)
    with pytest.raises(KeyError, match="TSUBASA_API_KEY"):
        init("tsubasa", config)
    assert "tsubasa" not in clients
