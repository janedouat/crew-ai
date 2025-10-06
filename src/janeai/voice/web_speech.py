"""Web Speech API implementation for voice input."""

import streamlit as st
from .voice_interface import VoiceInput


class WebSpeechInput(VoiceInput):
    """Web Speech API implementation for browser-based voice recognition."""
    
    def render_voice_component(self) -> str:
        """Render the Web Speech API voice input component.
        
        Returns:
            str: HTML/JavaScript code for voice input
        """
        return """
        <div id="voice-input-container" style="display: inline-block; position: relative;">
            <button id="voice-btn" 
                    style="
                        background-color: #4CAF50;
                        border: none;
                        border-radius: 50%;
                        width: 40px;
                        height: 40px;
                        color: white;
                        font-size: 16px;
                        cursor: pointer;
                        margin-left: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                        transition: all 0.2s ease;
                    "
                    onmouseover="this.style.backgroundColor='#45a049'"
                    onmouseout="this.style.backgroundColor='#4CAF50'"
                    title="Click to start voice input">
                🎤
            </button>
            <div id="voice-status" style="
                position: absolute;
                top: -25px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 12px;
                color: #666;
                white-space: nowrap;
                display: none;
            "></div>
        </div>

        <script>
        (function() {
            // Check if speech recognition is supported
            if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
                document.getElementById('voice-btn').style.display = 'none';
                return;
            }

            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            const voiceBtn = document.getElementById('voice-btn');
            const voiceStatus = document.getElementById('voice-status');
            
            let isListening = false;

            // Configure recognition
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';

            // Voice button click handler
            voiceBtn.addEventListener('click', function() {
                if (isListening) {
                    console.log('Stopping speech recognition');
                    recognition.stop();
                } else {
                    console.log('Starting speech recognition');
                    try {
                        recognition.start();
                    } catch (error) {
                        console.error('Error starting recognition:', error);
                        alert('Error starting voice recognition: ' + error.message);
                    }
                }
            });

            // Recognition event handlers
            recognition.onstart = function() {
                console.log('Speech recognition started');
                isListening = true;
                voiceBtn.innerHTML = '🔴';
                voiceBtn.style.backgroundColor = '#f44336';
                voiceStatus.textContent = 'Listening...';
                voiceStatus.style.display = 'block';
            };

            recognition.onend = function() {
                console.log('Speech recognition ended');
                isListening = false;
                voiceBtn.innerHTML = '🎤';
                voiceBtn.style.backgroundColor = '#4CAF50';
                voiceStatus.style.display = 'none';
            };

            recognition.onnomatch = function() {
                console.log('No speech was recognized');
                voiceStatus.textContent = 'No speech detected';
                voiceStatus.style.color = '#ff9800';
                setTimeout(() => {
                    voiceStatus.style.display = 'none';
                    voiceStatus.style.color = '#666';
                }, 2000);
            };

            recognition.onspeechstart = function() {
                console.log('Speech detected');
                voiceStatus.textContent = 'Speech detected...';
            };

            recognition.onspeechend = function() {
                console.log('Speech ended');
                voiceStatus.textContent = 'Processing...';
            };

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                console.log('Speech recognition result:', transcript);
                
                // Wait a moment for DOM to be ready, then try multiple approaches
                setTimeout(() => {
                    // Try multiple selectors to find the text input
                    let textInput = document.querySelector('input[placeholder="ask me anything"]');
                    if (!textInput) {
                        textInput = document.querySelector('input[data-testid="stTextInput-input"]');
                    }
                    if (!textInput) {
                        textInput = document.querySelector('input[type="text"]');
                    }
                    if (!textInput) {
                        // Look for any input in the streamlit app
                        textInput = document.querySelector('.stTextInput input');
                    }
                    if (!textInput) {
                        // Last resort - find any text input
                        const inputs = document.querySelectorAll('input');
                        for (let input of inputs) {
                            if (input.type === 'text' || !input.type) {
                                textInput = input;
                                break;
                            }
                        }
                    }
                    
                    if (textInput) {
                        console.log('Found text input, setting value:', transcript);
                        
                        // Set the value using multiple methods
                        textInput.value = transcript;
                        
                        // Trigger React/Streamlit events
                        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                        nativeInputValueSetter.call(textInput, transcript);
                        
                        // Dispatch events
                        const events = ['input', 'change', 'keyup', 'keydown'];
                        events.forEach(eventType => {
                            const event = new Event(eventType, { bubbles: true });
                            textInput.dispatchEvent(event);
                        });
                        
                        // Focus the input
                        textInput.focus();
                        
                        // Try React fiber approach for Streamlit
                        const reactFiber = textInput._valueTracker;
                        if (reactFiber) {
                            reactFiber.setValue(transcript);
                        }
                        
                        console.log('Successfully set input value to:', textInput.value);
                    } else {
                        console.error('Could not find text input element');
                        console.log('Available inputs:', document.querySelectorAll('input'));
                        alert('Heard: "' + transcript + '" but could not find input field');
                    }
                }, 100);
            };

            recognition.onerror = function(event) {
                console.error('Speech recognition error:', event.error);
                voiceStatus.textContent = 'Error: ' + event.error;
                voiceStatus.style.color = '#f44336';
                
                setTimeout(() => {
                    voiceStatus.style.display = 'none';
                    voiceStatus.style.color = '#666';
                }, 3000);
            };
        })();
        </script>
        """
    
    def is_supported(self) -> bool:
        """Check if Web Speech API is supported.
        
        Note: This always returns True since we handle the check in JavaScript.
        The actual support check happens in the browser.
        
        Returns:
            bool: Always True (browser-side check)
        """
        return True
    
    def get_error_message(self) -> str:
        """Get error message for unsupported browsers.
        
        Returns:
            str: Error message for unsupported browsers
        """
        return ("Voice input requires a modern browser like Chrome, Edge, or Safari. "
                "Firefox and some mobile browsers may not support this feature.")
