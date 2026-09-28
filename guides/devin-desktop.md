# Devin Desktop / Windsurf through OpenCode

Devin Desktop can launch OpenCode through ACP. Configure Tsubasa in that agent
using [opencode.json](../presets/opencode.json), then select
`tsubasa/tsubasa-fast` or `tsubasa/tsubasa-pro` in OpenCode. Install OpenCode
separately; the desktop registry does not install the executable for you.

Follow the official
[OpenCode ACP registry example](https://docs.devin.ai/desktop/acp#sample-config-for-opencode).
Point its launch command at your installed executable and retain the `acp`
argument. Merge the entry with your existing registry rather than replacing it.
Use **Open Local ACP Registry Config** from the Command Palette to find the
correct file for your platform.

Enable OpenCode under **Devin User Settings → Agents**. Supply `TSUBASA_API_KEY`
through that agent's environment settings. Restart or reload ACP connections as
directed by the desktop. Prompts and the key are then handled by OpenCode and
sent to `api.tsubasa.sh`; inference billing belongs to that provider.

The official ACP feature has account-tier requirements. This is an external
agent route, not a Tsubasa option in Devin's own model catalog. OpenCode's
controlled transport checks do not qualify a complete desktop ACP conversation;
that UI path and live inference remain untested.
