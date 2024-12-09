# AI Agent with Integrated Tools

## Overview
This is an AI agent powered by LangChain, capable of interacting with a variety of tools to assist with tasks such as weather lookup, Wikipedia search, sending WhatsApp messages, and fetching motivational quotes. The agent is built using OpenAI's GPT-4 model and integrates various tools through a modular architecture.

## Features
- **Weather Tool**: Retrieve current weather information for any city.
- **Wikipedia Search**: Fetch brief summaries from Wikipedia based on a search query.
- **Quote Tools**: Get motivational quotes either from an API or from a local text file.
- **WhatsApp Tool**: Send WhatsApp messages by providing the recipient's name and message content.
- **Simple Search Tool**: Perform internet searches for current events using the Tavily API.

## Tools Included
1. **WeatherTool**: Provides current weather information for any city.
2. **WikipediaSearch**: Allows for searching and summarizing articles from Wikipedia.
3. **QuoteTool**: Fetches motivational quotes from an external API.
4. **QuoteFromFileTool**: Retrieves motivational quotes from a local text file.
5. **WhatsappTool**: Enables the sending of WhatsApp messages by specifying the recipient and message.
6. **SimpleSearchTool**: Allows searching for current events or general information using the Tavily API.

## Dependencies
This project requires the following Python libraries:
- `langchain`
- `dotenv`
- `openai`
- `tavily`
- `wikipedia`
- `twilio`
- `pydantic`

## Setup and Installation
Clone the repository:

   ```bash
   git clone https://github.com/Pirogjikdhima/AI-Projects.git
   ```
# Disclaimer: LangChain Dependency

This project uses LangChain version 0.1, which may be outdated. It is recommended to check for updates to LangChain and other dependencies as newer versions might offer improved features, better performance, and bug fixes.
