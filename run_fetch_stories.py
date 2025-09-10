#!/usr/bin/env python3
"""
Run only the fetch_personalized_stories_task
Usage: python run_fetch_stories.py
"""

import sys
import warnings
from datetime import datetime
from crewai import Task, Crew, Process
from src.janeai.crew import Janeai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def main():
    """Run only the fetch_personalized_stories_task"""
    print("🔍 Jane's Hacker News Story Fetcher")
    print("=" * 50)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Create the crew instance
        janeai = Janeai()
        
        # Get the researcher agent
        researcher = janeai.hackernews_researcher()
        
        # Get the fetch task
        fetch_task = janeai.fetch_personalized_stories_task()
        
        # Create a crew with just the researcher and fetch task
        crew = Crew(
            agents=[researcher],
            tasks=[fetch_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("📰 Fetching personalized Hacker News stories...")
        print("This will:")
        print("1. Fetch the top 30 stories from Hacker News")
        print("2. Filter them based on Jane's interests")
        print("3. Select the 10 most relevant stories")
        print("4. Show relevance scores and why each story is relevant")
        print()
        
        # Run the crew
        result = crew.kickoff()
        
        print("\n✅ Story fetching completed successfully!")
        print(f"⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error fetching stories: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
