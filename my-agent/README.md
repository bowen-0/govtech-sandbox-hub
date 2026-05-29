# Sandbox Hub Agent

LangGraph agent for AI projects in the Canton of Zürich AI Innovation Sandbox. Two capabilities in one graph:

1. **Risk assessment** — gathers a project profile through conversation, then runs an automated risk-selection + mitigation lookup against an internal risk database, and renders the result as a `risk_accordion` UI component.
2. **Wiki-grounded Q&A** — reads the `wiki/` corpus (prior sandbox projects, concepts, regulations, lessons) to answer questions and ground risk discussions in real prior cases.

## Architecture

`src/simple_agent/graph.py` builds a `StateGraph` with:

- A **chat node** that handles both modes (profile-gathering and wiki Q&A), choosing between five tools:
  - `update_project_field` — store one piece of project info.
  - `start_risk_analysis` — trigger the risk pipeline (routes to `get_risks`).
  - `list_wiki_pages`, `read_wiki_page`, `search_wiki` — query the wiki.
- A **risk pipeline** (`get_risks → filter_risks → assess_risks → push_ui`) that runs when the chat node calls `start_risk_analysis`.
- A `risks_db.py` module with the internal risk catalogue + mitigation lookups.

The wiki tools resolve `WIKI_ROOT` (default `../wiki` relative to the package) and are path-traversal-guarded. The agent has no write access to the wiki.

The wiki's own answering procedure (`wiki/QUERY.md`) is the contract for the Q&A mode; the system prompt summarises it and instructs the chat node to load the full procedure on demand.

## Quickstart (local demo)

1. Sync the project with `uv`:

```bash
uv sync --dev
```

2. Configure environment:

```bash
cp .env.example .env
# edit .env — set OPENAI_API_KEY (or ANTHROPIC_API_KEY) at minimum.
# WIKI_ROOT defaults to ../wiki; override only if running from elsewhere.
```

3. Run the agent locally:

```bash
uv run langgraph dev          # serves on http://localhost:2024
```

4. In a second terminal, start the chat UI (sibling `agent-chat-ui/` package):

```bash
cd ../agent-chat-ui && pnpm dev   # serves on http://localhost:3000
```

The chat UI's `.env.example` already points at `localhost:2024` with assistant ID `agent`, so no extra wiring is needed.

Optional `make` wrappers (agent only):

```bash
make dev
make run
```

## Tests and lint

```bash
make test
make integration-tests
make lint
make format
```

Integration tests are skipped unless `ANTHROPIC_API_KEY` is set.

## Deploy

A Cloudflare Container deployment path exists (`Dockerfile`, `worker/`, `wrangler.jsonc`) and is currently dormant. For the local demo it can be ignored.

## Reference docs

- LangChain quickstart: https://docs.langchain.com/oss/python/langchain/quickstart
- LangChain deployment: https://docs.langchain.com/oss/python/langchain/deploy
