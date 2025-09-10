# Jane's AI Agents

A collection of AI agents that represent Jane's digital presence and capabilities. This includes a conversational digital twin and a personalized Hacker News research system that filters and summarizes the most relevant tech news based on Jane's specific interests.

## Available Agents

### 1. Jane's Digital Twin
- **Conversational AI**: Responds to prompts with Jane's personality, background, and expertise
- **Personality**: Sarcastic but friendly, direct, and focused on healthcare tech innovation
- **Background**: MBA at HBS, former Special Projects lead at Vera Health (YC S24), CTO & Co-founder of OMENA
- **Expertise**: Healthcare tech, AI, privacy, women in tech, building tools that help people

### 2. Hacker News Research Agent
- **Personalized Filtering**: Filters Hacker News stories based on Jane's specific interests
- **Interest Categories**: AI providers, mobile apps, JavaScript, privacy, health tech, and more
- **TLDR Summaries**: Provides 3 bullet-point summaries for each relevant story
- **Relevance Scoring**: Ranks stories by personal relevance (1-10 scale)
- **Real-time Data**: Fetches live data from Hacker News API

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
uv sync
```

### Setup

**Add your `ANTHROPIC_API_KEY` into the `.env` file**


## Running the Agents

### Jane's Digital Twin (Conversational Agent)

To chat with Jane's digital twin:

```bash
python cli_jane.py "Your prompt here"
```

Examples:
```bash
python cli_jane.py "Introduce yourself to the class"
python cli_jane.py "Explain your background in 3 sentences"
python cli_jane.py "What are your thoughts on AI in healthcare?"
```

### Hacker News Research Agent

To run the Hacker News research agent:

```bash

# Run only the story fetching task
python run_fetch_stories.py
```

This will:
1. Fetch the top 30 stories from Hacker News
2. Filter them based on Jane's interests
3. Select the 10 most relevant stories
4. Generate TLDR summaries with 3 bullet points each
5. Save results to `hackernews_tldr_summaries.md`

## Output

### Jane's Digital Twin
- **Console output**: Direct responses from Jane's digital twin with her personality and expertise
- **Interactive**: Responds to any prompt with Jane's unique voice and perspective

### Hacker News Research Agent
- **Console output**: Filtered list of relevant stories with relevance scores
- **File output**: `hackernews_tldr_summaries.md` with detailed TLDR summaries

## Understanding the Agents

### Jane's Digital Twin
- **Role**: Conversational AI that represents Jane's personality, background, and interests
- **Personality**: Sarcastic but friendly and humble AI that knows everything about Jane
- **Background**: MBA at Harvard Business School, former Special Projects lead at Vera Health (YC S24), CTO & Co-founder of OMENA
- **Interests**: Healthcare tech, AI, privacy, building tools that help people, women in tech
- **Goal**: Represent Jane's personality with a healthy dose of sarcasm and wit

### Hacker News Research System
The Hacker News research system consists of two specialized AI agents:

#### Hacker News Research Specialist
- **Role**: Monitors and analyzes Hacker News for trending topics
- **Tools**: Hacker News API integration, search capabilities
- **Goal**: Identify the most relevant stories from top 30

#### Hacker News Content Analyst  
- **Role**: Analyzes and synthesizes stories into actionable insights
- **Goal**: Create detailed TLDR summaries with 3 bullet points per story

## Customization

To modify Jane's agents interests or behavior:
- Edit `src/janeai/config/agents.yaml` to change agent roles and goals
- Edit `src/janeai/config/tasks.yaml` to modify filtering criteria or output format
- Edit `src/janeai/tools/custom_tool.py` to add new data sources or tools

## Example Output

### Jane's Digital Twin
Jane's digital twin responds with her unique personality:

```
🤖 Jane's response:
Hey! I'm Jane - currently an MBA at HBS, but I'm really just a healthcare tech nerd who can't stop building things. 
I spent this summer at Vera Health (YC S24) building AI tools for doctors (because apparently writing YAML configs by hand is still a thing in 2024?). 
Before that, I co-founded OMENA for the 250 million women going through menopause. 
I'm always thinking "how would a physician actually use this?" and I never really take breaks - I just say "see you later" like I'll be back in an hour.
```

### Hacker News Research Agent
Jane's Hacker News agent will generate personalized summaries like:

```
1. Claude now has access to a server-side container environment (Relevance: 10/10)
   TLDR:
   • Claude can now create, edit, and execute files within a secure server-side container
   • Supports multiple programming languages for code execution
   • Enhances AI-assisted development capabilities significantly
```

## Support

For support, questions, or feedback regarding Jane's AI Agents:
- Reach out through the project repository
- Check the configuration files in `src/janeai/config/` for customization options

Experience Jane's unique perspective through her digital twin and stay informed with the most relevant tech news tailored to her interests!
