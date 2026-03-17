"""Simple chat CLI that runs a pydantic-ai agent until it returns a structured result."""

from typing import Any

from pydantic_ai import Agent


def cli(agent: Agent[None, Any], hot_start: str | None = None) -> Any:
    """Simple chat CLI; exits when the agent returns a non-str (structured result).

    Args:
        agent: The agent to run.
        hot_start: The hot start message to use.

    Returns:
        The final structured output (the agent's output DTO) when the agent
        returns a non-string; the loop exits at that point.
    """
    print(
        "\n> Agent: Hello, I'm a meta-prompting assistant. I'll help you generate a high-quality prompt for your project. Please describe what you would like to prompt."
    )

    message_history: list[Any] = []
    while True:
        if not hot_start:
            user_message = input("\n> You: ").strip()

        else:
            user_message = hot_start
            hot_start = None

        if not user_message:
            continue

        result = agent.run_sync(user_message, message_history=message_history)
        output = result.output
        if isinstance(output, str):
            print(f"\n> Agent: {output}")
            message_history = result.all_messages()

        else:
            print("\n> Agent: ")
            print(output)

            user_confirmation = input(
                "\n> Are you okay with this output? (y for yes, or describe what you would like to change): "
            ).strip()

            if user_confirmation == "y":
                return output
            else:
                hot_start = user_confirmation
                continue
