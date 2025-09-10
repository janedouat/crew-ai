#!/usr/bin/env python3
"""
Jane's Digital Twin with Hacker News Search Capability
Usage: python jane_search_hackernews.py "Your question about tech"
"""

import sys
import warnings
from datetime import datetime
from crewai import Task, Crew, Process
from src.janeai.crew import Janeai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def main():
    """Run Jane's digital twin with Hacker News search capability"""
    if len(sys.argv) < 2:
        print("Usage: python jane_search_hackernews.py 'Your question about tech'")
        print("Example: python jane_search_hackernews.py 'What are the latest developments in AI healthcare?'")
        print("Example: python jane_search_hackernews.py 'Tell me about recent privacy concerns in tech'")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    
    print("🤖 Jane's Digital Twin with Hacker News Search")
    print("=" * 60)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"❓ Question: {question}")
    print()
    
    try:
        # Create the crew instance
        janeai = Janeai()
        
        # Get Jane's digital twin agent (now with Hacker News tools)
        jane_agent = janeai.jane_digital_twin_light()
        
        # Create a task for Jane to search and analyze
        task = Task(
            description=f"""
            The user asked: "{question}"
            
            You MUST use the Hacker News tools available to you to search for and fetch real, current stories.
            Do not make up or reference stories without actually fetching them from Hacker News.
            
            Steps to follow:
            1. Use the Hacker News search tool to find stories related to the user's question
            2. If no specific search results, use the Hacker News tool to fetch top stories
            3. Analyze the real stories you fetched with your unique perspective
            4. Use your knowledge of healthcare tech, AI, privacy, and women in tech to give insightful commentary
            5. Be your usual sarcastic but helpful self while providing valuable insights based on REAL data
            
            Remember: You must actually call the Hacker News tools - don't just pretend to use them.
            """,
            expected_output="Jane's analysis of REAL Hacker News stories (fetched using tools) with her unique perspective, insights, and personality",
            agent=jane_agent
        )
        
        # Create a crew with just Jane
        crew = Crew(
            agents=[jane_agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        print("🔍 Jane is searching Hacker News and analyzing...")
        print()
        
        # Run the crew
        result = crew.kickoff()
        
        print("\n" + "="*60)
        print("🤖 Jane's Response:")
        print("="*60)
        print(result)
        print(f"\n⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
