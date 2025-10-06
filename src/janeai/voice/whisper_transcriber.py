"""Whisper API transcription service."""

import os
import tempfile
from typing import Optional
import openai
from openai import OpenAI


class WhisperTranscriber:
    """Service for transcribing audio using OpenAI's Whisper API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Whisper transcriber.
        
        Args:
            api_key: OpenAI API key. If None, will try to get from environment.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def transcribe_audio(self, audio_data, language: str = "en") -> str:
        """Transcribe audio data using Whisper API.
        
        Args:
            audio_data: Raw audio bytes or Streamlit UploadedFile object
            language: Language code (e.g., "en", "fr", "es")
            
        Returns:
            str: Transcribed text
            
        Raises:
            Exception: If transcription fails
        """
        try:
            # Handle both bytes and UploadedFile objects
            if hasattr(audio_data, 'read'):
                # It's an UploadedFile object from Streamlit
                audio_bytes = audio_data.read()
                # Reset file pointer for potential future reads
                audio_data.seek(0)
            else:
                # It's already bytes
                audio_bytes = audio_data
            
            # Create a temporary file for the audio
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name
            
            try:
                # Open the file and send to Whisper
                with open(temp_file_path, "rb") as audio_file:
                    transcript = self.client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        language=language,
                        response_format="text"
                    )
                
                return transcript.strip()
                
            finally:
                # Clean up temporary file
                if os.path.exists(temp_file_path):
                    os.unlink(temp_file_path)
                    
        except Exception as e:
            raise Exception(f"Whisper transcription failed: {str(e)}")
    
    def is_available(self) -> bool:
        """Check if Whisper API is available.
        
        Returns:
            bool: True if API key is configured
        """
        return bool(self.api_key)
    
    def get_cost_estimate(self, duration_minutes: float) -> float:
        """Estimate cost for transcription.
        
        Args:
            duration_minutes: Audio duration in minutes
            
        Returns:
            float: Estimated cost in USD
        """
        # Whisper pricing: $0.006 per minute
        return duration_minutes * 0.006
