"""OpenAI Text-to-Speech service for Jane's responses."""

import os
import tempfile
from typing import Optional
import openai
from openai import OpenAI
import streamlit as st


class TTSService:
    """Service for converting text to speech using OpenAI's TTS API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize TTS service.
        
        Args:
            api_key: OpenAI API key. If None, will try to get from environment.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def text_to_speech(self, text: str, voice: str = "nova", model: str = "tts-1") -> bytes:
        """Convert text to speech using OpenAI TTS.
        
        Args:
            text: Text to convert to speech
            voice: Voice to use (alloy, echo, fable, onyx, nova, shimmer)
            model: TTS model (tts-1 or tts-1-hd)
            
        Returns:
            bytes: Audio data in MP3 format
            
        Raises:
            Exception: If TTS conversion fails
        """
        try:
            response = self.client.audio.speech.create(
                model=model,
                voice=voice,
                input=text,
                response_format="mp3"
            )
            
            return response.content
            
        except Exception as e:
            raise Exception(f"TTS conversion failed: {str(e)}")
    
    def play_audio_in_streamlit(self, text: str, voice: str = "nova") -> None:
        """Convert text to speech and play in Streamlit.
        
        Args:
            text: Text to convert and play
            voice: Voice to use
        """
        try:
            # Convert text to speech
            audio_bytes = self.text_to_speech(text, voice=voice)
            
            # Create a temporary file for better compatibility
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name
            
            # Read the file and play in Streamlit
            with open(temp_file_path, "rb") as audio_file:
                audio_data = audio_file.read()
                st.audio(audio_data, format="audio/mp3")
            
            # Clean up
            os.unlink(temp_file_path)
            
        except Exception as e:
            st.error(f"Failed to play audio: {str(e)}")
    
    def is_available(self) -> bool:
        """Check if TTS service is available.
        
        Returns:
            bool: True if API key is configured
        """
        return bool(self.api_key)
    
    def get_cost_estimate(self, text: str) -> float:
        """Estimate cost for TTS conversion.
        
        Args:
            text: Text to estimate cost for
            
        Returns:
            float: Estimated cost in USD
        """
        # TTS-1 pricing: $15 per 1M characters
        char_count = len(text)
        return (char_count / 1_000_000) * 15.0
    
    @staticmethod
    def get_available_voices():
        """Get list of available voices.
        
        Returns:
            list: Available voice names
        """
        return ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
