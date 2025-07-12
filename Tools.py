import logging
import requests
from bs4 import BeautifulSoup
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun

logging.basicConfig(level=logging.INFO)

@function_tool()
async def get_weather(location: str, run_context: RunContext) -> str:
    """
    Get the current weather for a given location (works well for South Africa).
    """
    try:
        response = requests.get(f"https://wttr.in/{location}?format=3")
        if response.status_code == 200:
            weather = response.text.strip()
            logging.info(f"Weather for {location}: {weather}")
            return weather
        else:
            logging.error(f"Failed to get weather for {location}: {response.status_code}")
            return f"Could not retrieve weather for {location}."
    except Exception as e:
        logging.error(f"Error getting weather for {location}: {str(e)}")
        return f"An error occurred while retrieving the weather for {location}."

@function_tool()
async def search_web(context: RunContext, query: str) -> str:
    """
    Perform a quick and simple web search using DuckDuckGo.
    """
    try:
        results = DuckDuckGoSearchRun().run(tool_input=query)
        if results:
            logging.info(f"Search results for '{query}': {results}")
            return results
        else:
            return f"No relevant information found for '{query}'."
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {str(e