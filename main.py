from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

# Video 23
class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatGroq(temperature=0, model="llama-3.1-8b-instant")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    # result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})

    messages = [
        SystemMessage(content="You are a helpful assistant that uses tools accurately. When calling a tool, provide only the necessary JSON arguments."),
        HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")
    ]
    result = agent.invoke({"messages": messages})

    print(result)

if __name__ == "__main__":
    main()