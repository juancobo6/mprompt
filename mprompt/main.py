"""Main script for the skelegen CLI."""

import os

import pyperclip

from .agent import init_agent
from .cli import cli


def main() -> None:
    """Main function for the mprompt project."""
    if os.getenv("GOOGLE_API_KEY") is None:
        raise ValueError("GOOGLE_API_KEY is not set")

    agent = init_agent()
    prompt = cli(agent)

    if prompt is not None:
        pyperclip.copy(str(prompt))
        print("\n> Copied to clipboard.")


if __name__ == "__main__":
    main()
