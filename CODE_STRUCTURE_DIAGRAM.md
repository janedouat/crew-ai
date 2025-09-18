# Jane's Digital Twin - Code Structure Diagram

## Current Architecture (Simplified)

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                    │
├─────────────────────────────────────────────────────────────┤
│  cli_jane.py          │  run_hackernews.py  │  run_fetch_stories.py │
│  (Basic chat)         │  (Full pipeline)   │  (Fetch only)         │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    MAIN ORCHESTRATION                      │
├─────────────────────────────────────────────────────────────┤
│                    src/janeai/main.py                      │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  Simple Input → Default Crew Execution                 │ │
│  │  inputs = {                                            │ │
│  │    'topic': 'Hacker News Analysis',                    │ │
│  │    'current_year': '2024'                             │ │
│  │  }                                                     │ │
│  │  Janeai().crew().kickoff(inputs=inputs)               │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    CREW ORCHESTRATION                      │
├─────────────────────────────────────────────────────────────┤
│                    src/janeai/crew.py                      │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  @crew                                                  │ │
│  │  def crew(self) -> Crew:                               │ │
│  │    return Crew(                                        │ │
│  │      agents=self.agents,  # All agents                 │ │
│  │      tasks=self.tasks,    # All tasks                  │ │
│  │      process=Process.sequential                        │ │
│  │    )                                                   │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      AGENT LAYER                           │
├─────────────────────────────────────────────────────────────┤
│                    src/janeai/config/agents.yaml           │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  jane_digital_twin_light                               │ │
│  │  ├─ Role: Jane's Digital Twin                          │ │
│  │  ├─ Tools: HackerNewsTool, HackerNewsSearchTool        │ │
│  │  └─ Personality: Sarcastic, healthcare-focused        │ │
│  │                                                        │ │
│  │  hackernews_researcher                                 │ │
│  │  ├─ Role: Hacker News Research Specialist              │ │
│  │  ├─ Tools: HackerNewsTool, HackerNewsSearchTool        │ │
│  │  └─ Purpose: Fetch and filter stories                  │ │
│  │                                                        │ │
│  │  hackernews_analyst                                    │ │
│  │  ├─ Role: Hacker News Content Analyst                  │ │
│  │  ├─ Tools: None (analysis only)                        │ │
│  │  └─ Purpose: Create TLDR summaries                    │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      TASK LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                    src/janeai/config/tasks.yaml            │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  fetch_personalized_stories_task                       │ │
│  │  ├─ Agent: hackernews_researcher                       │ │
│  │  ├─ Purpose: Fetch top 30, filter by Jane's interests│ │
│  │  └─ Output: 10 most relevant stories                   │ │
│  │                                                        │ │
│  │  create_tldr_summaries_task                            │ │
│  │  ├─ Agent: hackernews_analyst                          │ │
│  │  ├─ Purpose: Create 3-bullet TLDR summaries           │ │
│  │  └─ Output: hackernews_tldr_summaries.md              │ │
│  │                                                        │ │
│  │  jane_hackernews_search_task                           │ │
│  │  ├─ Agent: jane_digital_twin_light                     │ │
│  │  ├─ Purpose: Jane's perspective on findings           │ │
│  │  └─ Output: Jane's analysis                           │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      TOOL LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                    src/janeai/tools/custom_tool.py         │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  HackerNewsTool                                        │ │
│  │  ├─ Purpose: Fetch stories by type (top, new, best)     │ │
│  │  ├─ API: Hacker News Firebase API                      │ │
│  │  └─ Output: Formatted story list                       │ │
│  │                                                        │ │
│  │  HackerNewsSearchTool                                  │ │
│  │  ├─ Purpose: Search stories by keywords                 │ │
│  │  ├─ Method: Search through top 100 stories            │ │
│  │  └─ Output: Matching stories with details              │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Execution Flow

### Default Execution (Sequential Process)
```
1. fetch_personalized_stories_task
   ↓ (output becomes input for next task)
2. create_tldr_summaries_task
   ↓ (output becomes input for next task)
3. jane_hackernews_search_task
   ↓
Final Output: Jane's analysis + hackernews_tldr_summaries.md
```

### Agent-Task Mapping
```
hackernews_researcher → fetch_personalized_stories_task
hackernews_analyst → create_tldr_summaries_task
jane_digital_twin_light → jane_hackernews_search_task
```

## File Structure
```
MIT-AI-STUDIO/
├── cli_jane.py                    # Basic chat interface
├── run_hackernews.py              # Research pipeline runner
├── run_fetch_stories.py           # Story fetcher only
├── pyproject.toml                 # Project config & scripts
├── README.md                      # Documentation
└── src/janeai/
    ├── __init__.py
    ├── main.py                    # Simple orchestration
    ├── crew.py                    # Single crew definition
    ├── config/
    │   ├── agents.yaml            # Agent configurations
    │   └── tasks.yaml             # Task configurations
    └── tools/
        ├── __init__.py
        └── custom_tool.py         # Hacker News tools
```

## Key Characteristics

### 1. **Simplified Architecture**
- Single crew with all agents and tasks
- Sequential process execution
- No dynamic routing or conditional logic

### 2. **Fixed Execution Order**
- Always runs all 3 tasks in sequence
- No adaptation based on user input
- Consistent behavior regardless of input

### 3. **Agent Specialization**
- Each agent has a specific role
- Tools are assigned to relevant agents
- Clear separation of concerns

### 4. **Configuration-Driven**
- Agent personalities in YAML
- Task descriptions in YAML
- Easy to modify without code changes

## Input Flow
```
main.py inputs → crew.kickoff() → CrewAI interpolation → Task execution
```

## Benefits of Current Structure
1. **Simplicity**: Easy to understand and maintain
2. **Consistency**: Always produces the same output format
3. **Reliability**: No complex routing logic to debug
4. **Completeness**: Always runs full pipeline

## Limitations
1. **No Flexibility**: Can't adapt to different user needs
2. **Always Runs Everything**: Even if user only wants chat
3. **Fixed Output**: Always produces Hacker News analysis
4. **No User Choice**: No way to select different behaviors

## Usage Examples

### Running the Default Crew
```bash
# Via pyproject.toml script
uv run janeai

# Direct Python execution
python -m janeai.main

# Individual components
python run_hackernews.py      # Full pipeline
python run_fetch_stories.py   # Fetch only
python cli_jane.py "prompt"   # Chat with Jane
```

### What Happens
1. Fetches top 30 Hacker News stories
2. Filters by Jane's interests (healthcare tech, AI, privacy, etc.)
3. Selects 10 most relevant stories
4. Creates TLDR summaries with 3 bullet points each
5. Provides Jane's perspective on the findings
6. Saves results to `hackernews_tldr_summaries.md`

This is a clean, simple architecture that always produces comprehensive Hacker News analysis with Jane's unique perspective!
