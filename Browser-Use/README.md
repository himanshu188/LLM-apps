# Browser-Use

A Python application that enables LLMs to browse and interact with web content using the `browser-use` library.

## Description

Browser-Use is a project that allows AI model with web browsing capabilities. It allows language models to perform tasks on the web, such as searching for information, extracting data, and potentially automating web-based workflows.

## Features

- Web browsing capabilities for LLMs
- Integration with Google's Gemini 2.0 Flash model
- Asynchronous task execution
- Simple agent-based architecture

## Prerequisites

- Python 3.12+
- A Google API key for Gemini AI access

## Installation

1. Clone this repository:

2. Set up a virtual environment (the project comes with a `.python-version` file for Python 3.12):
   ```bash
   uv sync
   ```
3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Run the main.py file
    ```
    uv run main.py
    ```

## Usage

The main script demonstrates how to use the Browser-Use agent to perform a web search:

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()
import asyncio

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

async def main():
    # Create agent with the model
    agent = Agent(
        task="Search for the AAPL stock price",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

To run the example:

```bash
python main.py
```

## Customizing Tasks

You can customize the agent's task by modifying the `task` parameter when creating an Agent:

```python
agent = Agent(
    task="Your custom task here",
    llm=llm
)
```

## Dependencies

- `browser-use` - Core library for web browsing capabilities
- `langchain-google-genai` - Integration with Google's Generative AI models
- `patchright` - Utility library used by the project
- `python-dotenv` - For loading environment variables


## Acknowledgements

- [browser-use](https://github.com/browser-use/browser-use) library
- [LangChain](https://github.com/langchain-ai/langchain) for AI model integration