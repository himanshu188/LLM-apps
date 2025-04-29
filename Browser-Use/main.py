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
