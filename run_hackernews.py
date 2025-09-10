#!/usr/bin/env python3
"""
Run Jane's Hacker News Research Agent with default tasks
Usage: python run_hackernews.py
"""

import sys
import warnings
from datetime import datetime
from src.janeai.crew import Janeai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def main():
    """Run the Hacker News research crew with default tasks"""
    print("🚀 Jane's Hacker News Research Agent")
    print("=" * 50)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    inputs = {
        'topic': 'Hacker News Analysis',
        'current_year': str(datetime.now().year)
    }
    
    try:
        print("📰 Running Hacker News research crew...")
        print("This will:")
        print("1. Fetch the top 30 stories from Hacker News")
        print("2. Filter them based on Jane's interests")
        print("3. Select the 10 most relevant stories")
        print("4. Generate TLDR summaries with 3 bullet points each")
        print("5. Save results to 'hackernews_tldr_summaries.md'")
        print()
        
        # Run the crew with default tasks
        result = Janeai().crew().kickoff(inputs=inputs)
        
        print("\n✅ Hacker News research completed successfully!")
        print(f"📄 Results saved to: hackernews_tldr_summaries.md")
        print(f"⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error running Hacker News research: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
