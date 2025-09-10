# Personalized Hacker News Agent

A personalized Hacker News research agent powered by [crewAI](https://crewai.com) that filters and summarizes the most relevant tech news based on your specific interests. The agent fetches top stories from Hacker News, filters them for relevance, and provides detailed TLDR summaries with actionable insights.

## Features

- **Personalized Filtering**: Filters Hacker News stories based on your specific interests
- **Interest Categories**: AI providers, mobile apps, JavaScript, privacy, health tech, and more
- **TLDR Summaries**: Provides 3 bullet-point summaries for each relevant story
- **Relevance Scoring**: Ranks stories by personal relevance (1-10 scale)
- **Real-time Data**: Fetches live data from Hacker News API
- **Automated Workflow**: Runs with a single command

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Setup

**Add your `OPENAI_API_KEY` into the `.env` file**

The agent is pre-configured to filter for these interests:
- AI providers (OpenAI, Anthropic, Google, etc.)
- Big AI labs news and announcements
- Health technology and medical AI
- Mobile apps and mobile development
- JavaScript frameworks and tools
- AI agents and automation
- LLMs and language models
- AI privacy and data privacy
- Cloudflare and infrastructure
- Apple development and Xcode
- Browser security and vulnerabilities
- Coding agents and AI development tools

## Running the Agent

To run your personalized Hacker News agent:

```bash
crewai run
```

This command will:
1. Fetch the top 30 stories from Hacker News
2. Filter them based on your interests
3. Select the 10 most relevant stories
4. Generate TLDR summaries with 3 bullet points each
5. Save results to `hackernews_tldr_summaries.md`

## Output

The agent generates:
- **Console output**: Filtered list of relevant stories with relevance scores
- **File output**: `hackernews_tldr_summaries.md` with detailed TLDR summaries

## Understanding the Agent

The Hacker News agent consists of two specialized AI agents:

### Hacker News Research Specialist
- **Role**: Monitors and analyzes Hacker News for trending topics
- **Tools**: Hacker News API integration, search capabilities
- **Goal**: Identify the most relevant stories from top 30

### Hacker News Content Analyst  
- **Role**: Analyzes and synthesizes stories into actionable insights
- **Goal**: Create detailed TLDR summaries with 3 bullet points per story

## Customization

To modify the agent's interests or behavior:
- Edit `src/janeai/config/agents.yaml` to change agent roles and goals
- Edit `src/janeai/config/tasks.yaml` to modify filtering criteria or output format
- Edit `src/janeai/tools/custom_tool.py` to add new data sources or tools

## Example Output

The agent will generate personalized summaries like:

```
1. Claude now has access to a server-side container environment (Relevance: 10/10)
   TLDR:
   • Claude can now create, edit, and execute files within a secure server-side container
   • Supports multiple programming languages for code execution
   • Enhances AI-assisted development capabilities significantly
```

## Support

For support, questions, or feedback regarding the Hacker News Agent or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Stay informed with the most relevant tech news tailored to your interests!
