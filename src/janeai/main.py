#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from janeai.crew import Janeai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with interactive user input.
    """
    print("🤖 Jane's Digital Twin - Interactive Mode")
    print("=" * 50)
    
    # Ask what the user wants
    print("\nWhat would you like?")
    print("1. Ask Jane a question")
    print("2. Get Jane's take on the Hacker News news of the day")
    
    choice = input("\nEnter your choice (1-2): ").strip()
    
    if choice == "1":
        # Ask Jane a question
        question = input("\nWhat would you like to ask Jane? ")
        inputs = {
            'topic': 'Chat with Jane',
            'user_question': question,
            'current_year': str(datetime.now().year)
        }
        
    elif choice == "2":
        # Jane's Hacker News perspective
        inputs = {
            'topic': 'Hacker News Analysis',
            'current_year': str(datetime.now().year)
        }
        
    else:
        print("Invalid choice. Running default Hacker News analysis...")
        inputs = {
            'topic': 'Hacker News Analysis',
            'current_year': str(datetime.now().year)
        }
    
    try:
        print(f"\n🚀 Running: {inputs['topic']}")
        print("=" * 50)
        
        janeai = Janeai()
        
        if choice == "1":
            # Chat with Jane
            crew = janeai.create_chat_crew(inputs)
        elif choice == "2":
            # Jane's Hacker News perspective
            crew = janeai.create_hackernews_crew(inputs)
        else:
            # Default crew
            crew = janeai.crew()
        
        crew.kickoff(inputs=inputs)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Hacker News Analysis",
        'current_year': str(datetime.now().year)
    }
    try:
        Janeai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Janeai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Hacker News Analysis",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Janeai().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
