import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Workaround for ChromaDB SQLite issue on Streamlit Cloud
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"

from src.janeai.crew import Janeai
from src.janeai.voice import get_voice_input
from src.janeai.voice.whisper_api import WhisperInput

# Page config
st.set_page_config(
    page_title="Jane's Digital Twin",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide the header
st.markdown("""
<style>
    .stApp > header {
        visibility: hidden;
    }
    .stApp > div:first-child {
        padding-top: 0;
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS for white background and styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stApp {
        background-color: white;
    }
    .jane-title {
        font-size: 20rem;
        font-weight: bold;
        text-align: center;
        color: #000000;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        justify-content: center;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        font-size: 1.2rem;
        font-weight: 600;
        color: #000000;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 16px;
    }
    .stTabs [data-baseweb="tab-panel"] .stButton {
        margin-top: 16px !important;
    }
    .stTabs [data-baseweb="tab-panel"] .stButton > button {
        margin-top: 0 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #000000;
    }
    .stTabs [aria-selected="true"] {
        color: #000000;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #000000;
    }
    p, div, span {
        color: #000000;
    }
    .stButton button, .stButton button span, .stButton button div, .stButton button p {
        color: white !important;
    }
    .stTextInput > div > div > input {
        color: #000000 !important;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #999999 !important;
    }
    .stTextInput > div > div > input:focus {
        background-color: white !important;
        color: #000000 !important;
        border-color: #4CAF50 !important;
        box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.15) !important;
        outline: none !important;
    }
    .stButton > button {
        color: white !important;
        background-color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        height: 2.5rem !important;
        font-size: 1rem !important;
        margin: 0 auto !important;
        display: block !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        background-color: #333333 !important;
        border-color: #333333 !important;
        color: white !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:focus {
        color: white !important;
    }
    .stButton > button:active {
        color: white !important;
    }
    button[data-testid="baseButton-secondary"] {
        color: white !important;
    }
    button[data-testid="baseButton-secondary"]:hover {
        color: white !important;
    }
    .stMarkdown {
        color: #000000;
    }
    .stSuccess {
        color: #000000;
    }
    .stWarning {
        color: #000000;
    }
    .stError {
        color: #000000;
    }
    .stInfo {
        color: #000000;
    }
    .stJson {
        background-color: white !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
        border-radius: 4px !important;
        padding: 1rem !important;
    }
    .stJson pre {
        background-color: white !important;
        color: #000000 !important;
    }
    .stCodeBlock {
        background-color: white !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
    .stCodeBlock pre {
        background-color: white !important;
        color: #000000 !important;
    }
    .stMarkdown pre {
        background-color: white !important;
        color: #000000 !important;
    }
    .text-input-container {
        position: relative;
        display: inline-block;
        width: 100%;
    }
    .text-input-container .stTextInput > div {
        position: relative;
    }
    .text-input-container .stTextInput > div > div {
        position: relative;
    }
    .text-input-container .stTextInput > div > div > input {
        padding-right: 4rem !important;
        background-color: white !important;
        width: 100% !important;
        margin-top: 16px !important;
    }
    .text-input-container .stTextInput > div > div::after {
        content: "→";
        position: absolute;
        right: 0.5rem;
        top: 50%;
        transform: translateY(-50%);
        width: 2.5rem;
        height: 2.5rem;
        background-color: #4CAF50;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        color: white;
        pointer-events: none;
        z-index: 10;
    }
    .arrow-icon {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="jane-title">HI I\'M JANE</h1>', unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["Ask Me Anything", "Hacker News"])

# Tab 1: Ask Me Anything
with tab1:
    # Initialize session state for voice input
    if "voice_question" not in st.session_state:
        st.session_state.voice_question = ""
    
    # Voice input section
    st.markdown("**🎤 Voice Input** (record your question)")
    audio_bytes = st.audio_input("Record your question")g
    
    # Initialize session state for tracking audio
    if "last_audio_hash" not in st.session_state:
        st.session_state.last_audio_hash = None
    
    if audio_bytes:
        st.audio(audio_bytes)
        
        # Create a hash of the audio to detect new recordings
        import hashlib
        current_audio_hash = hashlib.md5(audio_bytes.read()).hexdigest()
        audio_bytes.seek(0)  # Reset file pointer
        
        # Check if this is a new recording
        is_new_recording = st.session_state.last_audio_hash != current_audio_hash
        
        if is_new_recording:
            st.session_state.last_audio_hash = current_audio_hash
            
            # Initialize Whisper transcriber
            whisper_input = WhisperInput()
            
            if whisper_input.is_supported():
                with st.spinner("🔄 Auto-transcribing your audio..."):
                    try:
                        transcription = whisper_input.transcribe_audio(audio_bytes)
                        st.session_state.voice_question = transcription
                        st.success(f"✅ Transcribed: '{transcription}'")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Transcription failed: {str(e)}")
            else:
                st.warning("⚠️ " + whisper_input.get_error_message())
                st.info("💡 Add your OpenAI API key to `.env` file: `OPENAI_API_KEY=your_key_here`")
        else:
            # Show existing transcription if available
            if st.session_state.voice_question:
                st.info(f"💬 Current transcription: '{st.session_state.voice_question}'")
    
    # Text input (populated by voice or manual typing)
    question = st.text_input(
        "Or type your question:",
        placeholder="ask me anything",
        value=st.session_state.voice_question,
        key="question_input"
    )
    
    # Clear voice question after it's been used
    if st.session_state.voice_question and question != st.session_state.voice_question:
        st.session_state.voice_question = ""
    
    # Process question on Enter key or when text changes
    if question:
        with st.spinner("Jane is thinking..."):
            try:
                # Create inputs
                inputs = {
                    'topic': 'Chat with Jane',
                    'user_question': question,
                    'current_year': str(datetime.now().year)
                }
                
                # Create and run chat crew
                janeai = Janeai()
                crew = janeai.create_chat_crew(inputs)
                result = crew.kickoff(inputs=inputs)
                
                
                # Extract and display the raw content
                if isinstance(result, dict) and 'raw' in result:
                    st.markdown(result['raw'])
                else:
                    st.markdown(str(result))
                
            except Exception as e:
                st.error(f"Error: {e}")

# Tab 2: Hacker News
with tab2:
    if st.button("get my take on Hacker News today", type="primary", use_container_width=True):
        with st.spinner("Jane is analyzing Hacker News..."):
            try:
                # Create inputs
                inputs = {
                    'topic': 'Hacker News Analysis',
                    'current_year': str(datetime.now().year)
                }
                
                # Create and run hackernews crew
                janeai = Janeai()
                crew = janeai.create_hackernews_crew(inputs)
                result = crew.kickoff(inputs=inputs)
                
                # Display result
                st.markdown("### Jane's Hacker News Analysis:")
                
                # Extract and display the raw content
                if isinstance(result, dict) and 'raw' in result:
                    st.markdown(result['raw'])
                else:
                    st.markdown(str(result))
                
                    
            except Exception as e:
                st.error(f"Error: {e}")
