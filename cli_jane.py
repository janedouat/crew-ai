#!/usr/bin/env python3
"""
Jane's Digital Twin - Command Line Input
Usage: python cli_jane.py "Your prompt here"
"""

import sys
from crewai import Task, Crew, Process
from src.janeai.crew import Janeai

def create_jane_agent():
    """Get Jane's digital twin agent from the crew"""
    return Janeai().jane_digital_twin_light()

def main():
    """Main function to handle command line input"""
    if len(sys.argv) < 2:
        print("Usage: python cli_jane.py 'Your prompt here'")
        print("Example: python cli_jane.py 'Introduce yourself to the class'")
        print("Example: python cli_jane.py 'Explain your background in 3 sentences'")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    
    print(f"🤖 Jane's Digital Twin Light")
    print(f"📝 Prompt: {prompt}")
    print("=" * 50)
    
    jane_agent = create_jane_agent()
    
    # Create task for the prompt
    task = Task(
        description=prompt,
        expected_output="A witty, sarcastic response that captures Jane's personality and knowledge and uses available tools (like the hacker news tool)",
        agent=jane_agent
    )
    
    # Create crew
    crew = Crew(
        agents=[jane_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=False
    )
    
    # Run the task
    try:
        result = crew.kickoff()
        print(f"\n🤖 Jane's response:\n{result}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
