# Jane's Digital Twin Agent

A CLI-accessible Jane clone with two main features: ask Jane questions directly, or get her thoughts on today's Hacker News stories.

## Features

### 1. Ask Jane a Question
- **Direct conversation** with Jane's digital twin
- **Humble and brief responses** 
- **Access to Jane's background**
- **No external tool calls** - pure conversation mode

### 2. Get Jane's Take on Hacker News
- **Full research pipeline** using specialized Hacker News agents
- **Personalized filtering** based on Jane's interests (healthcare tech, AI, privacy, women in tech)
- **TLDR summaries** of the most relevant stories
- **Jane's unique perspective** on the day's tech news
- **Output file**: `hackernews_tldr_summaries.md`

## Installation

### Prerequisites

- **Python**: >=3.10 <3.14 installed on your system
- **API Key**: Anthropic API key for Claude (the AI model Jane uses)

### Step 1: Install UV Package Manager

This project uses [UV](https://docs.astral.sh/uv/) for fast dependency management. Install it first:

```bash
pip install uv
```

### Step 2: Clone and Setup Project

```bash
# Clone the repository (if not already done)
git clone <your-repo-url>
cd MIT-AI-STUDIO

# Install all dependencies
uv sync
```

This will:
- Create a virtual environment automatically
- Install all required packages (CrewAI, Anthropic, etc.)
- Set up the project structure

### Step 3: Environment Configuration

Create a `.env` file in the project root and add your Anthropic API key and model:

```bash
# Create .env file
touch .env

# Add your API key and model (replace with your actual values)
echo "ANTHROPIC_API_KEY=your_anthropic_api_key_here" >> .env
echo "MODEL=claude-3-5-sonnet-20240620" >> .env
```

**Configuration details:**
- **API Key**: Visit [console.anthropic.com](https://console.anthropic.com) to create an account and generate an API key
- **Model**: Choose from available Claude models:
  - `claude-3-5-sonnet-20240620` (recommended - latest and most capable)
  - `claude-3-5-haiku-20241022` (faster, more cost-effective)
  - `claude-3-opus-20240229` (most powerful, slower)

### Step 4: Verify Installation

Test that everything is working:

```bash
# Run the interactive CLI
uv run janeai
```

You should see the Jane's Digital Twin menu appear!


## Running Jane's Digital Twin

### Interactive CLI

Run the interactive interface to choose between the two features:

```bash
uv run janeai
```

This will show you a menu:
```
🤖 Jane's Digital Twin - Interactive Mode
==================================================

What would you like?
1. Ask Jane a question
2. Get Jane's take on the Hacker News news of the day

Enter your choice (1-2): 
```

### Option 1: Ask Jane a Question
- Choose option 1 and enter your question
- Jane will respond with her personality, background, and expertise
- Perfect for personal questions, career advice, or general conversation

### Option 2: Get Jane's Take on Hacker News
- Choose option 2 for Jane's analysis of today's tech news
- Uses specialized Hacker News research agents
- Creates personalized summaries based on Jane's interests
- Saves results to `hackernews_tldr_summaries.md`

## Customization

To modify Jane's agents interests or behavior:
- Edit `src/janeai/config/agents.yaml` to change agent roles and goals
- Edit `src/janeai/config/tasks.yaml` to modify filtering criteria or output format
- Edit `src/janeai/tools/custom_tool.py` to add new data sources or tools

## Support

For support, questions, or feedback regarding Jane's AI Agents:
- Reach out through the project repository
- Check the configuration files in `src/janeai/config/` for customization options

Experience Jane's unique perspective through her digital twin and stay informed with the most relevant tech news tailored to her interests!
