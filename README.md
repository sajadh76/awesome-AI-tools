# Awesome AI Tools

A curated list of AI tools worth your time. Coding agents, local LLMs, RAG,
evals, MCP servers, voice, and the rest of the stack people actually use.

Every link is checked by CI. If something is dead or outdated, open a PR.

## Contents

- [Coding Agents](#coding-agents)
- [AI Code Editors](#ai-code-editors)
- [Agent Frameworks](#agent-frameworks)
- [Running LLMs Locally](#running-llms-locally)
- [RAG and Knowledge](#rag-and-knowledge)
- [Vector Databases](#vector-databases)
- [Agent Memory](#agent-memory)
- [Evals and Observability](#evals-and-observability)
- [MCP](#mcp)
- [Voice and Audio](#voice-and-audio)
- [Image and Video](#image-and-video)
- [Workflow Automation](#workflow-automation)
- [Web Search and Scraping for Agents](#web-search-and-scraping-for-agents)

## Coding Agents

Terminal-first agents that read your repo, edit files, and run commands.

- [Claude Code](https://github.com/anthropics/claude-code) - Anthropic's terminal coding agent. Reads the codebase, edits files, runs commands, handles git. The one most people compare everything else to.
- [OpenAI Codex](https://github.com/openai/codex) - OpenAI's coding agent that runs locally in your terminal, with IDE extension and cloud options.
- [OpenCode](https://github.com/sst/opencode) - Open source coding agent with a terminal UI and desktop app. Works with any model provider.
- [Aider](https://github.com/Aider-AI/aider) - Pair programming in the terminal. Maps your repo into the model's context and applies diffs you review. Free, bring your own key.
- [Cline](https://github.com/cline/cline) - Autonomous coding agent as a VS Code extension. Free, pay only for the model API you use.
- [Google Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's open source terminal agent for Gemini models, with search, file and shell tools plus MCP support.
- [Pi](https://github.com/earendil-works/pi) - Toolkit with a unified multi-provider LLM API, an agent runtime, a terminal UI, and an extensible coding agent CLI.
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - DeepSeek's official plugin-based agent harness, run through npx with a web UI.
- [OpenHands](https://github.com/OpenHands/OpenHands) - Self-hosted control center that runs OpenHands or other agents locally, in Docker, or in the cloud.

## AI Code Editors

Editors with AI built into the editing experience, not bolted on.

- [Cursor](https://cursor.com) - AI-native code editor (VS Code fork) with agent mode for multi-file work. The most widely adopted one in 2026.
- [Windsurf](https://windsurf.com) - AI IDE with an agent that tracks your actions and codebase context as you work.
- [Zed](https://github.com/zed-industries/zed) - Fast multiplayer code editor in Rust, with a built-in agent panel that also hosts external agents.

## Agent Frameworks

Libraries for building agents with tools, memory, and multi-step workflows.

- [LangChain](https://github.com/langchain-ai/langchain) - The original LLM app framework. Chains, tools, and agents; huge ecosystem.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Build agents as stateful graphs. Good when your workflow has branches, loops, and human-in-the-loop steps.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Lightweight library for teams of agents with roles, tasks, and delegation.
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's framework for multi-agent conversation. Agents talk to each other and to humans to get work done.
- [SmolAgents](https://github.com/huggingface/smolagents) - Hugging Face's minimal agent library. Code-first agents in a few lines.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe agent framework from the Pydantic team. Structured outputs without the guessing.

## Running LLMs Locally

Run open models on your own hardware. No API bills, no data leaving the machine.

- [Ollama](https://github.com/ollama/ollama) - The easiest way to run LLMs locally. One command to pull and serve a model with an OpenAI-compatible API.
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - The engine under most local LLM tools. Plain C/C++, runs everywhere including phones and Raspberry Pis.
- [LM Studio](https://lmstudio.ai) - Desktop app for running local models with a chat UI and local server mode. Good first stop if you don't live in the terminal.
- [Open WebUI](https://github.com/open-webui/open-webui) - Self-hosted ChatGPT-style UI for local and remote models. Works offline.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput serving engine for LLMs. What you reach for when Ollama is not fast enough.
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) - Gradio-based UI for running lots of model backends with extensions.

## RAG and Knowledge

Give models access to your documents instead of hoping they memorized them.

- [RAGFlow](https://github.com/infiniflow/ragflow) - Open source RAG engine with deep document understanding. Handles messy PDFs and tables better than most.
- [Pathway](https://github.com/pathwaycom/pathway) - Live data RAG with real-time streaming, for agents that need up-to-the-second knowledge.
- [Firecrawl](https://github.com/firecrawl/firecrawl) - Turn any website into clean markdown or structured data. The fastest way to feed the web into a RAG pipeline.
- [Exa](https://exa.ai) - Search API built for AI. Semantic search over the web with clean results made for retrieval, not humans.

## Vector Databases

Where the embeddings live.

- [Qdrant](https://github.com/qdrant/qdrant) - High-performance vector search in Rust, with payload filtering that actually works.
- [Chroma](https://github.com/chroma-core/chroma) - The simple one. Embeddings database that feels like a Python dict; great for prototypes.
- [Weaviate](https://github.com/weaviate/weaviate) - Vector DB with hybrid search and GraphQL. Solid pick when you outgrow Chroma.
- [LanceDB](https://github.com/lancedb/lancedb) - Serverless vector DB on top of Lance columnar format. No infra to run.

## Agent Memory

Agents that remember things across sessions beat agents that start blank every time.

- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for agents. Remembers user preferences and facts, recalls them when relevant.
- [Letta](https://github.com/letta-ai/letta) - Framework for stateful agents with long-term memory (formerly MemGPT). The research project that started the agent-memory conversation.
- [Zep](https://github.com/getzep/zep) - Memory server for agents with temporal knowledge graphs. Knows not just what happened, but when.
- [Supermemory](https://github.com/supermemoryai/supermemory) - Fast memory engine and API built for the AI era.

## Evals and Observability

If you cannot measure it, you cannot tell whether the new prompt helped or hurt.

- [Langfuse](https://github.com/langfuse/langfuse) - Open source LLM observability. Traces, scores, and prompt management; self-hostable.
- [LangSmith](https://www.langchain.com/langsmith) - LangChain's hosted tracing and eval platform. The default choice if you already live in LangChain.
- [Braintrust](https://www.braintrust.dev) - Evals, prompt playground, and observability in one place. Strong dataset-driven eval workflow.
- [Ragas](https://github.com/explodinggradients/ragas) - Metrics for RAG pipelines: faithfulness, answer relevance, context precision. The standard RAG eval library.
- [DeepEval](https://github.com/confident-ai/deepeval) - LLM eval framework with pytest-style tests for agents and RAG.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open source AI observability from Arize. Trace and troubleshoot LLM apps locally.

## MCP

Model Context Protocol: the open standard for giving agents tools. One protocol, works across Claude Code, Cursor, Gemini CLI, and the rest.

- [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) - The protocol itself. Start here if you want to understand how it works.
- [MCP Servers](https://github.com/modelcontextprotocol/servers) - The official collection of reference servers: files, git, databases, web search, and more.
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - GitHub's official MCP server. Issues, PRs, code, and Actions as agent tool calls.
- [FastMCP](https://github.com/jlowin/fastmcp) - The fast way to build MCP servers in Python. Decorators in, working server out.

## Voice and Audio

Speech to text, text to speech, and everything between.

- [Whisper](https://github.com/openai/whisper) - OpenAI's speech recognition. Still the accuracy baseline everything else is measured against.
- [Piper](https://github.com/rhasspy/piper) - Fast local neural text to speech. Runs on a Raspberry Pi, voices are small downloads.
- [Coqui TTS](https://github.com/coqui-ai/TTS) - Text to speech library with voice cloning. The open source toolkit for custom voices.
- [VoiceStudio](https://github.com/debpalash/VoiceStudio) - Open source, fully local ElevenLabs alternative: voice cloning, dubbing, transcription, audiobooks.

## Image and Video

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based UI for Stable Diffusion workflows. The power tool for serious image generation work.
- [Fooocus](https://github.com/lllyasviel/Fooocus) - Image generation focused on simplicity. Prompt in, good image out, no parameter fiddling.

- [AI 만화 번역기](https://www.mangatranslate.com/ko/ai-manga-translator/) - Ficory LLC의 기업급 만화 리더로, 제품이 지원하는 모든 번역 언어를 제공합니다. 개인은 만화를 일괄 번역하고 번역을 맞춤 설정하며, 스튜디오는 완전한 온라인 Photoshop 스타일 편집기로 작업합니다. API를 개인 작업 흐름에 연결할 수 있으며, 일일 체크인 무료 크레딧과 유료 요금제를 제공합니다.

## Workflow Automation

For agents that need to run on a schedule or react to events.

- [n8n](https://github.com/n8n-io/n8n) - Visual workflow automation with native AI capabilities. Self-hostable; the one people actually run in production.
- [Dify](https://github.com/langgenius/dify) - Full-stack platform for building LLM apps with agent workflow orchestration.
- [Langflow](https://github.com/langflow-ai/langflow) - Drag-and-drop builder for LangChain agents and flows.
- [OpenClaw](https://github.com/openclaw/openclaw) - Personal AI agent that lives on your device and does real work: messages, calendar, browser, cron jobs.
