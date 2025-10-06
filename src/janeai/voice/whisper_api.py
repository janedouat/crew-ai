"""Whisper API implementation for voice input."""

import os
from .voice_interface import VoiceInput
from .whisper_transcriber import WhisperTranscriber


class WhisperInput(VoiceInput):
    """OpenAI Whisper API implementation for voice recognition."""
    
    def __init__(self):
        """Initialize Whisper input."""
        self.transcriber = None
        try:
            self.transcriber = WhisperTranscriber()
        except ValueError:
            # API key not available
            pass
    
    def render_voice_component(self) -> str:
        """Render the Whisper voice input component.
        
        Note: This uses Streamlit's native audio_input, so this method
        returns an empty string as the component is handled in Streamlit.
        
        Returns:
            str: Empty string (Streamlit handles the UI)
        """
        return ""
    
    def transcribe_audio(self, audio_data) -> str:
        """Transcribe audio using Whisper API.
        
        Args:
            audio_data: Raw audio bytes or Streamlit UploadedFile object
            
        Returns:
            str: Transcribed text
            
        Raises:
            Exception: If transcription fails or API not available
        """
        if not self.transcriber:
            raise Exception("Whisper API not available. Please set OPENAI_API_KEY environment variable.")
        
        return self.transcriber.transcribe_audio(audio_data)
    
    def is_supported(self) -> bool:
        """Check if Whisper API is available.
        
        Returns:
            bool: True if OpenAI API key is configured
        """
        return self.transcriber is not None and self.transcriber.is_available()
    
    def get_error_message(self) -> str:
        """Get error message for Whisper setup.
        
        Returns:
            str: Setup instructions for Whisper
        """
        return ("Whisper voice input requires OpenAI API key. "
                "Add OPENAI_API_KEY to your environment variables.")
