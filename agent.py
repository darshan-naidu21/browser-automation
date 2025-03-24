from langchain_openai import ChatOpenAI
from browser_use import Agent, BrowserConfig, Browser
import asyncio
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def main():
    # browser_config = BrowserConfig(
    #     chrome_instance_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
    # )

    # browser = Browser(browser_config)

    agent = Agent(
        task="""Go to the URL: https://subway.com.my/find-a-subway
        1. Filter the search results by “Kuala Lumpur” to find relevant outlets.
        2. For each outlet, scrape the following details:
            - Name of the outlet
            - Full address
            - Operating hours
            - Waze direction link
        3. Ensure your script can handle pagination effectively to navigate through all available pages of content.""",
        llm=ChatOpenAI(model="gpt-4o-mini"),
        save_conversation_path="logs/conversation.json"
        # browser=browser
    )
    result = await agent.run()
    print(result)

asyncio.run(main())