# library-demo
# Sidekick

Multi-agent teammate that checks project requirements against repository evidence.
This is step 1: the Monitor Agent plus a Telegram bot (Communication + Helper commands).

## Setup

1. **Demo repo.** Create a GitHub repo for the project Sidekick will watch. Copy
   `demo/requirements.yaml` to its root, and add a CI workflow that runs pytest.
2. **Telegram bot.** In Telegram, talk to @BotFather, send /newbot, and copy the token.
   Send any message to your new bot, then open
   `https://api.telegram.org/bot<TOKEN>/getUpdates` and copy `chat.id`.
3. **GitHub token.** Settings > Developer settings > Fine-grained tokens, limited to the
   demo repo. Read-only for warn-only mode: Contents, Actions, Metadata.
   For assisted mode also give Contents write.
4. **Configure and run.**
   ```bash
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env        # fill it in
   pytest -q                   # should pass
   python -m sidekick.bot
   ```

## Using it

| Command | What it does |
|---|---|
| /status | One line per requirement |
| /gaps | What is missing, with evidence |
| /propose R3 | (assisted mode) Helper proposes a contract; Confirm or Reject buttons |

The bot also checks the repo every `POLL_SECONDS` and messages you only when a
requirement changes status. It uses long polling, so it needs no domain, open port or webhook.

## Known limits in this version

- `tests_pass` uses the latest CI result for the whole suite, not per test file yet.
- Contracts live in memory; a restart forgets pending proposals.
- On Confirm the Helper creates the branch only. Writing tests then code is the next step.
