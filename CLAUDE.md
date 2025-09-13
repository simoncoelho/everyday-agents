# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is for "everyday-agents" - a collection of simple agentic workflows for automation of everyday tasks using the OpenAI Agents SDK.

## Tech Stack

- **Package Manager**: uv (Ultra-fast Python package installer and resolver)
- **Agent Framework**: OpenAI Agents SDK
- **Language**: Python

## Development Commands

```bash
# Package management
uv sync                             # Install dependencies from lockfile
uv add <package>                    # Add a new dependency
uv remove <package>                 # Remove a dependency
uv run <command>                    # Run command in virtual environment

# Development tasks
uv run pytest                       # Run tests
uv run ruff check                   # Lint code
uv run ruff format                  # Format code
uv run mypy src                     # Type checking
```

## Project Structure

```
├── src/everyday_agents/    # Main package
│   └── core/              # Core functionality
│       ├── base_agent.py  # Abstract base agent class
│       └── __init__.py
├── agents/                # Specific agent implementations
├── examples/             # Usage examples
├── tests/                # Test suite
├── docs/                 # Documentation
└── .env.example          # Environment variable template
```

## Architecture Notes

- **BaseAgent**: Abstract base class for all agents (`src/everyday_agents/core/base_agent.py`)
- **Agents Directory**: Specific agent implementations for different tasks
- **Examples Directory**: Demonstrations of how to use agents
- **Environment Configuration**: Use `.env` files for API keys and settings

This project builds agentic workflows using OpenAI's API. Each agent inherits from `BaseAgent` and implements the `execute()` method for its specific automation task.