"""Voice input module for Jane's Digital Twin.

Provides a pluggable interface for different voice input providers.
Currently supports Web Speech API with future support for Whisper.
"""

from .voice_interface import VoiceInput
from .web_speech import WebSpeechInput
from .whisper_api import WhisperInput

def get_voice_input(provider="web_speech"):
    """Factory function to get voice input provider.
    
    Args:
        provider (str): Voice provider to use. Options: "web_speech", "whisper"
        
    Returns:
        VoiceInput: Voice input implementation
    """
    if provider == "web_speech":
        return WebSpeechInput()
    elif provider == "whisper":
        return WhisperInput()
    else:
        raise ValueError(f"Unknown voice provider: {provider}")

__all__ = ["VoiceInput", "WebSpeechInput", "WhisperInput", "get_voice_input"]
