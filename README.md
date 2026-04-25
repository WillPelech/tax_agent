# tax_agent
An AI agent to do your taxes using a ReAct (Reason + Act) loop.

## Setup

```bash
git clone <repo>
cd tax_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env` and add your API key:
```bash
cp .env .env.local
```

## Configuration

Edit `config.yaml` to switch providers:

```yaml
provider:
  name: "Gemini"
  model: "Flash"
  version: "2.0"
```

## Local Development (no API key needed)

Install [Ollama](https://ollama.com) and pull a small model:

```bash
ollama pull qwen2.5:0.5b
```

Then update `config.yaml`:
```yaml
provider:
  name: "Qwen"
  model: "qwen2.5:0.5b"
```

## Project Structure

```
agent/
  agent.py      # buildClient factory + ReAct loop
  client.py     # LLMClient base class + provider implementations
  prompt.py     # system and user prompts
  config.yaml   # model/provider config (moved to root)
tools/          # tool definitions for the agent
strategy/       # agent loop design docs
main.py         # entrypoint
```

## Adding a New Provider

1. Add a new class in `agent/client.py` that extends `LLMClient`
2. Implement the `chat(self, message: str) -> str` method
3. Add a new `elif` branch in `buildClient` in `agent/agent.py`
4. Update `config.yaml` to use the new provider name
