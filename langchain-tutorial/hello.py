import getpass
import os

from langchain_openai import ChatOpenAI


def main():
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    model = ChatOpenAI(model="gpt-4o-mini")

    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage("Translate the following from English into Chinese"),
        HumanMessage(
            "Note that ChatModels receive message objects as input and generate message objects as output. In addition to text content, message objects convey conversational roles and hold important data, such as tool calls and token usage counts.!"
        ),
    ]

    print(model.invoke(messages))


if __name__ == "__main__":
    main()
