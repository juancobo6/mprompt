"""Handles the process of initializing an AI agent."""

from pydantic_ai import Agent

from .instructions import get_instructions
from .models import Prompt

MODEL = "google-gla:gemini-2.5-flash"


def init_agent() -> Agent[None, str | Prompt]:
    """Initialize the agent."""
    return Agent[None, Prompt | str](
        model=MODEL,
        instructions=get_instructions(),
        output_type=str | Prompt,
        output_retries=3,
    )
