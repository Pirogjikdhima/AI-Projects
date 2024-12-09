from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from Tools import tools

def setup_agent() -> AgentExecutor:
    """Sets up the agent executor for handling user queries.

    Returns:
        An instance of `AgentExecutor` for managing agent and tool interactions.
    """
    load_dotenv()  # Load environment variables from .env file

    llm = ChatOpenAI(model="gpt-4o-mini")
    # llm = ChatGroq(model="mixtral-8x7b-32768")

    # Load the prompt for the OpenAI tools agent
    prompt = hub.pull("hwchase17/openai-tools-agent")

    # Initialize memory to store conversation history
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

    # Create the agent for calling tools
    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    # Create and return an agent executor
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        memory=memory,
    )

    return agent_executor

def main() -> None:
    """Main function to interact with the user and execute queries."""
    agent_executor = setup_agent()

    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            break

        try:
            response = agent_executor.invoke({"input": query})
            print(f"AI: {response['output']}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

