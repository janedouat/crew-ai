from crewai.tools import BaseTool
from typing import Type, List, Dict, Any
from pydantic import BaseModel, Field
import requests
import json
from datetime import datetime, timedelta


class HackerNewsToolInput(BaseModel):
    """Input schema for HackerNewsTool."""
    story_type: str = Field(default="top", description="Type of stories to fetch: 'top', 'new', 'best', 'ask', 'show', 'job'")
    limit: int = Field(default=10, description="Number of stories to fetch (max 50)")

class HackerNewsTool(BaseTool):
    name: str = "Hacker News API Tool"
    description: str = (
        "Fetches stories from Hacker News API. Can get top stories, new stories, best stories, "
        "Ask HN, Show HN, or job postings. Returns story details including title, URL, score, "
        "comments count, and author information."
    )
    args_schema: Type[BaseModel] = HackerNewsToolInput

    def _run(self, story_type: str = "top", limit: int = 10) -> str:
        """Fetch stories from Hacker News API."""
        try:
            # Hacker News API endpoints
            endpoints = {
                "top": "https://hacker-news.firebaseio.com/v0/topstories.json",
                "new": "https://hacker-news.firebaseio.com/v0/newstories.json", 
                "best": "https://hacker-news.firebaseio.com/v0/beststories.json",
                "ask": "https://hacker-news.firebaseio.com/v0/askstories.json",
                "show": "https://hacker-news.firebaseio.com/v0/showstories.json",
                "job": "https://hacker-news.firebaseio.com/v0/jobstories.json"
            }
            
            if story_type not in endpoints:
                return f"Invalid story type. Available types: {list(endpoints.keys())}"
            
            # Get story IDs
            response = requests.get(endpoints[story_type], timeout=10)
            response.raise_for_status()
            story_ids = response.json()[:limit]
            
            # Fetch story details
            stories = []
            for story_id in story_ids:
                story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=10)
                story_response.raise_for_status()
                story_data = story_response.json()
                
                if story_data and story_data.get('type') == 'story':
                    stories.append({
                        'id': story_data.get('id'),
                        'title': story_data.get('title', 'No title'),
                        'url': story_data.get('url', 'No URL'),
                        'score': story_data.get('score', 0),
                        'by': story_data.get('by', 'Unknown'),
                        'time': story_data.get('time', 0),
                        'descendants': story_data.get('descendants', 0),  # comment count
                        'text': story_data.get('text', '')[:200] + '...' if story_data.get('text') else ''
                    })
            
            # Format output
            result = f"Hacker News {story_type.title()} Stories (showing {len(stories)}):\n\n"
            for i, story in enumerate(stories, 1):
                time_str = datetime.fromtimestamp(story['time']).strftime('%Y-%m-%d %H:%M')
                result += f"{i}. {story['title']}\n"
                result += f"   URL: {story['url']}\n"
                result += f"   Score: {story['score']} | Comments: {story['descendants']} | By: {story['by']} | Time: {time_str}\n"
                if story['text']:
                    result += f"   Text: {story['text']}\n"
                result += "\n"
            
            return result
            
        except requests.RequestException as e:
            return f"Error fetching Hacker News data: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"


class HackerNewsSearchToolInput(BaseModel):
    """Input schema for HackerNewsSearchTool."""
    query: str = Field(..., description="Search query to find stories")
    limit: int = Field(default=10, description="Number of stories to return")

class HackerNewsSearchTool(BaseTool):
    name: str = "Hacker News Search Tool"
    description: str = (
        "Searches Hacker News stories by keywords in titles and content. "
        "Returns matching stories with their details."
    )
    args_schema: Type[BaseModel] = HackerNewsSearchToolInput

    def _run(self, query: str, limit: int = 10) -> str:
        """Search Hacker News stories by query."""
        try:
            # Get top stories to search through
            response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
            response.raise_for_status()
            story_ids = response.json()[:100]  # Search through top 100
            
            matching_stories = []
            query_lower = query.lower()
            
            for story_id in story_ids:
                story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=5)
                story_response.raise_for_status()
                story_data = story_response.json()
                
                if story_data and story_data.get('type') == 'story':
                    title = story_data.get('title', '').lower()
                    text = story_data.get('text', '').lower()
                    
                    if query_lower in title or query_lower in text:
                        matching_stories.append({
                            'id': story_data.get('id'),
                            'title': story_data.get('title', 'No title'),
                            'url': story_data.get('url', 'No URL'),
                            'score': story_data.get('score', 0),
                            'by': story_data.get('by', 'Unknown'),
                            'time': story_data.get('time', 0),
                            'descendants': story_data.get('descendants', 0),
                            'text': story_data.get('text', '')[:200] + '...' if story_data.get('text') else ''
                        })
                        
                        if len(matching_stories) >= limit:
                            break
            
            if not matching_stories:
                return f"No stories found matching query: '{query}'"
            
            # Format output
            result = f"Hacker News Search Results for '{query}' (showing {len(matching_stories)}):\n\n"
            for i, story in enumerate(matching_stories, 1):
                time_str = datetime.fromtimestamp(story['time']).strftime('%Y-%m-%d %H:%M')
                result += f"{i}. {story['title']}\n"
                result += f"   URL: {story['url']}\n"
                result += f"   Score: {story['score']} | Comments: {story['descendants']} | By: {story['by']} | Time: {time_str}\n"
                if story['text']:
                    result += f"   Text: {story['text']}\n"
                result += "\n"
            
            return result
            
        except requests.RequestException as e:
            return f"Error searching Hacker News: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
