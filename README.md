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
