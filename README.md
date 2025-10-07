# Jane's Digital Twin Agent

![Jane's Digital Twin UI](ui_screenshot.png)

A voice-enabled AI assistant featuring Jane's digital twin with two main capabilities: interactive voice/text conversations and personalized Hacker News analysis.

## Features

### 🎙️ Voice-Enabled Conversations
- **Voice input**: Record questions using OpenAI Whisper (99+ languages supported)
- **Voice output**: Jane responds with natural speech using OpenAI TTS
- **Auto-transcription**: Seamless speech-to-text integration
- **Complete voice workflow**: Speak → Auto-transcribe → Jane responds in voice + text

### 💬 Ask Jane a Question
- **Direct conversation** with Jane's digital twin
- **Multi-modal input**: Voice recording or text typing
- **AI-powered responses** using GPT-4o-mini
- **Jane's expertise**: Healthcare tech, AI, privacy, and women in tech background
- **Natural conversation flow** with session memory

### 📰 Get Jane's Take on Hacker News
- **Full research pipeline** using specialized Hacker News agents
- **Personalized filtering** based on Jane's interests (healthcare tech, AI, privacy, women in tech)
- **TLDR summaries** of the most relevant stories
- **Jane's unique perspective** on the day's tech news
- **Output file**: `hackernews_tldr_summaries.md`

## Installation

### Prerequisites

- **Python**: >=3.10 <3.14 installed on your system
- **API Keys**: 
  - OpenAI API key (for voice input/output and AI responses)
  - Modern web browser with microphone access for voice features

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

Create a `.env` file in the project root and add your OpenAI API key:

```bash
# Create .env file
touch .env

# Add your API key (replace with your actual values)
echo "OPENAI_API_KEY=your_openai_api_key_here" >> .env
```

**Configuration details:**
- **API Key**: Visit [platform.openai.com](https://platform.openai.com) to create an account and generate an API key
- **Voice Features**: 
  - Whisper API for speech-to-text (~$0.006/minute)
  - TTS API for text-to-speech (~$15/1M characters)
  - GPT-4o-mini for AI responses (~$0.15/1M input tokens)

### Step 4: Verify Installation

Test that everything is working:

```bash
# Run the interactive CLI
uv run janeai
```

You should see the Jane's Digital Twin menu appear!


## Running Jane's Digital Twin

### 🌐 Web UI (Recommended - Voice Enabled)

Interact with Jane through a voice-enabled web interface:

```bash
uv run streamlit run streamlit_app.py
```

**Voice Features:**
- 🎤 **Record questions**: Click the microphone to record voice input
- 🔄 **Auto-transcription**: Speech automatically converts to text
- 🔊 **Voice responses**: Jane speaks her answers using natural TTS
- 📝 **Text fallback**: Can also type questions manually

### 💻 Interactive CLI

You can also interact with Jane in your terminal (text-only):

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
- **Web UI**: Includes voice input/output capabilities

### Option 2: Get Jane's Take on Hacker News
- Choose option 2 for Jane's analysis of today's tech news
- Uses specialized Hacker News research agents
- Creates personalized summaries based on Jane's interests
- Saves results to `hackernews_tldr_summaries.md`

## 🎙️ Voice Interaction Guide

### Using Voice Features
1. **Start conversation**: Open the web UI and navigate to "Ask Me Anything" tab
2. **Record question**: Click the microphone icon and speak your question
3. **Auto-transcription**: Your speech appears as text automatically
4. **Jane responds**: Get both text and voice responses
5. **Natural flow**: Continue the conversation with voice or text

### Voice Quality & Performance
- **Speech Recognition**: OpenAI Whisper (high accuracy, 99+ languages)
- **Voice Synthesis**: OpenAI TTS with "nova" voice (natural, conversational)
- **Response Time**: ~2-5 seconds for typical questions
- **Cost**: ~$0.01 per conversation turn (very affordable)

## Customization

### Agent Personality & Behavior
- Edit `src/janeai/config/agents.yaml` to change agent roles and goals
- Edit `src/janeai/config/tasks.yaml` to modify filtering criteria or output format
- Edit `src/janeai/tools/custom_tool.py` to add new data sources or tools

### Voice Settings
- **Change voice**: Modify `voice="nova"` in `src/janeai/voice/tts_service.py`
- **Available voices**: alloy, echo, fable, onyx, nova, shimmer
- **TTS model**: Switch between `tts-1` (fast) and `tts-1-hd` (high quality)
- **Response length**: Adjust prompts for shorter/longer voice responses

## Support

For support, questions, or feedback regarding Jane's AI Agents:
- Reach out through the project repository
- Check the configuration files in `src/janeai/config/` for customization options

Experience Jane's unique perspective through her voice-enabled digital twin! Have natural conversations about healthcare tech, AI, and get personalized insights on the latest tech news.

## 🏗️ Technical Architecture

### Voice Pipeline
```
Voice Input → Whisper API → Text Processing → GPT-4o-mini → TTS API → Voice Output
```

### Key Components
- **Frontend**: Streamlit web interface with voice controls
- **STT**: OpenAI Whisper for speech recognition
- **AI Engine**: CrewAI framework with GPT-4o-mini
- **TTS**: OpenAI Text-to-Speech with natural voices
- **Backend**: Modular Python architecture with pluggable voice providers

### Cost Structure
- **Voice Input**: ~$0.006 per minute of speech
- **AI Processing**: ~$0.001 per response
- **Voice Output**: ~$0.005 per response
- **Total**: ~$0.01 per conversation turn
