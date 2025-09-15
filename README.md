# everyday-agents

A collection of AI-powered agentic workflows for automating everyday tasks using the OpenAI Agents SDK.

## Features

- **Tailored Learning Workflow**: Generates personalized learning content as PDF documents based on user profiles and interests
- **MCP Server Integration**: Connects to external services via Model Context Protocol (Notion, etc.)
- **PDF Generation**: Converts markdown content to professionally formatted PDF documents
- **Modern Python Stack**: Built with Python 3.13+ and uv package manager for fast dependency management

## Installation

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd everyday-agents

# Install dependencies
uv sync

# Copy environment template and configure
cp .env.example .env
# Edit .env with your API keys (OpenAI, Notion, etc.)
```

## Usage

### Tailored Learning Workflow

Generate personalized learning content:

```bash
# Run the tailored learning workflow
uv run python -m workflows.tailored_learning.tailored_learning_workflow
```

The workflow will:
1. Analyze your profile and learning preferences
2. Generate customized educational content
3. Create a PDF document in the `generated_pdfs/` directory

### Configuration

Customize the learning workflow:

```python
from workflows.tailored_learning.tailored_learning_workflow import TailoredLearningWorkflow

# Configure page count and document settings
workflow = TailoredLearningWorkflow(
    number_of_pages_low=10,    # Minimum pages
    number_of_pages_high=15,   # Maximum pages
    number_of_documents=1      # Number of documents to generate
)

await workflow.run()
```

## Development

### Commands

```bash
# Install dependencies
uv sync

# Add new dependency
uv add <package>

# Run tests
uv run pytest

# Code quality checks
uv run ruff check          # Lint code
uv run ruff format         # Format code
uv run ruff check --fix    # Auto-fix linting issues
uv run mypy src           # Type checking
```

### Project Structure

```
src/
├── everyday_agents/           # Main package
├── workflows/                 # Workflow implementations
    └── tailored_learning/     # Learning content generation
        ├── tailored_learning_workflow.py  # Main workflow
        └── agent/
            ├── get_learning_agent.py      # Agent configuration
            ├── tools/                     # Agent tools
            │   ├── create_pdf.py         # PDF generation
            │   └── send_pdf_to_kindle.py # Kindle integration
            ├── prompts/                   # Agent prompts
            └── mcp_servers/               # External service connections
```

## Architecture

### Workflows
Each workflow follows a consistent pattern:
- **Workflow Class**: Orchestrates the agent execution
- **Agent Definition**: Configures the AI agent with specific instructions
- **Tools**: Implements specific capabilities (PDF creation, API calls, etc.)
- **MCP Servers**: Handles connections to external services

### Key Technologies
- **OpenAI Agents SDK**: Core agent framework
- **Model Context Protocol (MCP)**: External service integration
- **uv**: Fast Python package management
- **markdown-pdf**: PDF generation from markdown

## Environment Variables

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key
NOTION_API_KEY=your_notion_api_key  # Optional, for Notion integration
# Add other service API keys as needed
```

## Contributing

1. Ensure Python 3.13+ and uv are installed
2. Run `uv sync` to install dependencies
3. Follow code quality standards: `uv run ruff format && uv run ruff check --fix`
4. Add tests for new functionality
5. Run `uv run pytest` before submitting changes

## License

MIT License - see LICENSE file for details.
