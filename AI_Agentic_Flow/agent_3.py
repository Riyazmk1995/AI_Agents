from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

class InternetConnectedAgent:
    def __init__(self):
        # Initialize SerpAPI wrapper
        self.search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

    def fetch_information(self, query):
        # Perform a web search using SerpAPI
        search_results = self.search.run(query)
        
        return {
            "query": query,
            "response": search_results,
            "source": "SerpAPI (Google Search)"
        }