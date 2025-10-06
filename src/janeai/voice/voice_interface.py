"""Abstract interface for voice input providers."""

from abc import ABC, abstractmethod
from typing import Optional


class VoiceInput(ABC):
    """Abstract base class for voice input implementations."""
    
    @abstractmethod
    def render_voice_component(self) -> str:
        """Render the voice input component (HTML/JS).
        
        Returns:
            str: HTML/JavaScript code for the voice input component
        """
        pass
    
    @abstractmethod
    def is_supported(self) -> bool:
        """Check if this voice input method is supported in current environment.
        
        Returns:
            bool: True if supported, False otherwise
        """
        pass
    
    def get_error_message(self) -> Optional[str]:
        """Get any error message from the voice input.
        
        Returns:
            Optional[str]: Error message if any, None otherwise
        """
        return None
