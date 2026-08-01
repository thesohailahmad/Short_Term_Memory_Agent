# LangGraph Memory Agent Demo

A minimal LangChain/LangGraph agent that demonstrates **short-term (thread-scoped) memory**
using `InMemorySaver` as a checkpointer. The agent remembers earlier turns in the same
conversation thread (`thread_id`) — ask it your name in one turn, ask "what's my name?"
in the next, and it answers correctly, because LangGraph replays the checkpointed
message history for that thread on every `invoke`.

Model: Gemini 2.5 Flash (via `init_chat_model`)
Tool: Tavily web search

## Setup

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # then fill in your real API keys
```

## Run

```bash
python agent.py
```

## Notes

- Memory is **in-memory only** — it resets every time the process restarts.
  Swap `InMemorySaver()` for a persistent checkpointer (e.g. `SqliteSaver`,
  `PostgresSaver`) to keep memory across runs.
- Memory is scoped to `thread_id`. Different `thread_id` values = separate,
  unrelated conversations even within the same process.
