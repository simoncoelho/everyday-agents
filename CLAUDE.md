# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"everyday-agents" is a collection of simple agentic workflows for automation of everyday tasks using the OpenAI Agents SDK. The project is designed to help users automate common tasks through AI agents.

## Tech Stack

- **Package Manager**: uv (Ultra-fast Python package installer and resolver)
- **Agent Framework**: OpenAI Agents SDK (`openai-agents` package)
- **Language**: Python 3.13+
- **Key Dependencies**:
  - `openai` - OpenAI API client
  - `python-dotenv` - Environment variable management
  - `markdown-pdf` - PDF generation from markdown

## Development Commands

```bash
# Package management
uv sync                             # Install dependencies from lockfile
uv add <package>                    # Add a new dependency
uv remove <package>                 # Remove a dependency
uv run <command>                    # Run command in virtual environment

# Development tasks
uv run pytest                       # Run all tests
uv run pytest tests/specific_test.py # Run specific test file
uv run ruff check                   # Lint code (check for errors)
uv run ruff format                  # Format code (auto-fix style)
uv run ruff check --fix             # Fix auto-fixable linting issues
uv run mypy src                     # Type checking on source code

# Project execution
uv run everyday-agents              # Run the main CLI (when implemented)
```

## Actual Project Structure

```
├── src/
│   ├── everyday_agents/           # Main package (importable as everyday_agents)
│   │   └── __init__.py           # Package initialization
│   └── workflows/                # Specific workflow implementations
│       └── tailored-learning/    # Educational content generation workflow
│           ├── __init__.py
│           ├── tailored-learning-workflow.py  # Main workflow class
│           └── agent/
│               ├── tailored-lesson-agent.py   # Agent definition
│               └── tools/
│                   └── create-pdf.py          # PDF creation tool
├── .env.example                  # Environment variable template
├── pyproject.toml               # Project configuration and dependencies
└── uv.lock                      # Dependency lockfile
```

## Architecture & Workflow Pattern

**Workflow Structure**: Each workflow in `src/workflows/` follows this pattern:
- Main workflow class (e.g., `TailoredLearningWorkflow`)
- Agent definitions using OpenAI Agents SDK
- Tool implementations for specific capabilities
- Integration with external services (Notion, PDF generation, etc.)

**Key Patterns**:
- Workflows are organized in separate directories under `src/workflows/`
- Each workflow contains its own agent definitions and tools
- Agents are configured with specific instructions/prompts
- Tools handle specific capabilities (PDF creation, API calls, etc.)

**Environment Configuration**:
- Use `.env` files for API keys (OpenAI, Notion, etc.)
- Follow the `.env.example` template for required variables

## Python/uv Specific Notes

**Package vs Project Naming Convention**:
- Project name: `everyday-agents` (with hyphens, used in pip install, PyPI)
- Package name: `everyday_agents` (with underscores, used in Python imports)
- This is standard Python convention - hyphens in distribution names, underscores in import names

**uv Benefits over pip**:
- Much faster dependency resolution and installation
- Built-in virtual environment management
- Lockfile for reproducible builds (`uv.lock`)
- `uv run` automatically manages virtual environment

**Development Workflow**:
1. `uv sync` to install dependencies
2. `uv run ruff format && uv run ruff check --fix` before committing
3. `uv run mypy src` to verify type annotations
4. `uv run pytest` to run tests