from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_tavily import TavilySearch

load_dotenv()

model = init_chat_model(
    model="gemini-3.5-flash",
    model_provider="google_genai",
    temperature=1.0,
)

search_tool = TavilySearch(max_results=3)

agent = create_agent(
    model=model,
    tools=[search_tool],
    checkpointer=InMemorySaver(),
    system_prompt=(
        "You are a helpful assistant. Use the search tool to answer "
        "questions about current events or facts you're unsure of."
    ),
)

config = {"configurable": {"thread_id": "1"}}


def ask(text: str) -> str:
    """Send one message on the same thread and print/return just the reply."""
    response = agent.invoke({"messages": [HumanMessage(content=text)]}, config)
    answer = response["messages"][-1].content
    print(answer)
    return answer


if __name__ == "__main__":
    ask("My name is Sohail, my favourite color is green, and I live in Pakistan.")
    ask("Where do I live?")
