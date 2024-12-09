import os

from dotenv import load_dotenv
from langchain.pydantic_v1 import BaseModel,Field
from langchain_core.tools import StructuredTool,BaseTool
from typing import Type

from ToolsFiles.quote_tool import get_quote_from_api,get_quote_from_file
from ToolsFiles.weather_tool import get_weather
from ToolsFiles.whatsapp_tool import session


load_dotenv()


class WhatsappArgs(BaseModel):
    """Arguments for sending a WhatsApp message."""
    name: str = Field(description="Name of the person")
    message: str = Field(description="Message to be sent")


class SimpleSearchInputArgs(BaseModel):
    """Arguments for performing a simple search query."""
    query: str = Field(description="Should be a search query")


def wikipedia_search(query: str) -> str:
    """Searches for a summary of the query on Wikipedia.

    Args:
        query: The query to search for.

    Returns:
        A string containing a brief summary from Wikipedia or an error message.
    """
    from wikipedia import summary
    try:
        return summary(query, sentences=2)
    except Exception:
        return "I couldn't find any information on that."


class SimpleSearchTool(BaseTool):
    """Tool for performing a simple search using the Tavily API."""
    name = "SimpleInternetSearch"
    description = "Useful for when you need to answer questions about current events."
    args_schema: Type[BaseModel] = SimpleSearchInputArgs

    def _run(self, query: str) -> str:
        """Executes a simple search query.

        Args:
            query: The search query string.

        Returns:
            The search results as a formatted string.
        """
        from tavily import TavilyClient

        api_key = os.getenv("TAVILY_API_KEY")
        client = TavilyClient(api_key=api_key)
        results = client.search(query=query)
        return f"Search results for: {query}\n\n{results}\n"  


tools = [
    StructuredTool.from_function(
        name = "WeatherTool",
        func = get_weather,
        description = "Useful for when you need to know the current weather in a City.",
    ),
    StructuredTool.from_function(
        name = "WikepediaSearch",
        func = wikipedia_search,
        description = "Useful for when wanting to search Wikipedia for something.",
    ),
    StructuredTool.from_function(
        name = "QuoteTool",
        func = get_quote_from_api,
        description = "Useful for when you need to output a quote from the internet.",
    ),
    StructuredTool.from_function(
        name = "QuoteFromFileTool",
        func = get_quote_from_file,
        description = "Useful for when you need to output a quote from the text file.",
    ),
    StructuredTool.from_function(
        name="WhatsappTool",
        func=session,
        description="Useful for opening Whatsapp and writing a message.",
        args_schema=WhatsappArgs,
    ),
    SimpleSearchTool(),
]