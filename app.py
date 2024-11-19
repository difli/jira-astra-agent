import uuid
from langchain_core.messages import HumanMessage
from agents.agent import Agent


def main():
    # Initialize the agent
    agent = Agent()

    print("Welcome to the 🛠️ JIRA Expert Chatbot 📋")
    print("Type your JIRA query below and press Enter. Type 'exit' to quit.")

    while True:
        # Get user input from the command line
        user_input = input("\nYour JIRA Query: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! Feel free to ask anytime! 👋")
            break

        if not user_input.strip():
            print("Please enter a valid JIRA query.")
            continue

        try:
            # Generate a unique thread ID for the query
            thread_id = str(uuid.uuid4())

            # Prepare the input messages
            messages = [HumanMessage(content=user_input)]
            config = {'configurable': {'thread_id': thread_id}}

            # Process the query using the agent
            print(f"Invoking the agent with thread ID: {thread_id}")  # Log the thread ID
            result = agent.graph.invoke({'messages': messages}, config=config)

            # Display the output to the user
            print("\nJIRA Information:")
            print(result['messages'][-1].content)

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Debugging Hint: Check the logs for more details or verify the tool input schema.")


if __name__ == '__main__':
    main()
