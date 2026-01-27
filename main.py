from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

@tool
def search(query: str) -> str:
    """
    Useful for searching weather and current events. Input should be a search query.
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "The current weather in Tokyo is sunny, around 25°C, with light wind."

llm = ChatGroq(temperature=0.3, model="llama-3.1-8b-instant")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    # result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})

    messages = [
        SystemMessage(content="You are a helpful assistant that uses tools accurately. When calling a tool, provide only the necessary JSON arguments."),
        HumanMessage(content="Whats the weather like in Tokyo")
    ]
    result = agent.invoke({"messages": messages})

    print(result)

if __name__ == "__main__":
    main()
