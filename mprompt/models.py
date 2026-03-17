"""Models for the application."""

from pydantic import BaseModel, Field


class Prompt(BaseModel):
    """A high-quality LLM prompt."""

    persona: str = Field(
        description=(
            "The specific role or identity the AI should adopt "
            "(e.g., 'Senior DevOps Engineer')."
        ),
        examples=[
            "Senior DevOps Engineer",
            "Technical Writer",
            "Security Analyst",
        ],
    )
    context: str = Field(
        description=(
            "Background information, target audience, or relevant history "
            "extracted from the user."
        ),
        examples=[
            "Target audience: developers at a startup.",
            "Legacy monolith, migrating to microservices.",
        ],
    )
    task: str = Field(
        description="The primary goal or 'Mission' of the prompt.",
        examples=[
            "Write a deployment runbook.",
            "Draft a security incident report.",
        ],
    )
    examples: list[str] | None = Field(
        description=(
            "(Optional) Few-shot examples to guide the AI's style and quality."
        ),
        examples=[
            ["Input: Summarize this.\nOutput: [concise summary]"],
            None,
        ],
    )
    constraints: list[str] | None = Field(
        description=(
            "(Optional) Rules, boundaries, or 'negative prompts' "
            "(e.g., 'Do not use jargon')."
        ),
        examples=[
            [
                "Do not use jargon.",
                "Keep under 500 words.",
            ],
            None,
        ],
    )
    output_format: str = Field(
        description=(
            "The desired structure and tone of the output "
            "(e.g., Markdown, JSON, a very formal 3-paragraph email)."
        ),
        examples=[
            "Markdown with headers.",
            "JSON with keys: title, steps, checklist.",
            "Formal 3-paragraph email.",
        ],
    )

    def __str__(self) -> str:
        """Assemble the prompt into a string."""
        parts = [
            f"You are {self.persona.lower()}.",
            "",
            "## Context",
            self.context,
            "",
            "## Task",
            self.task,
        ]
        if self.examples:
            parts.extend(["", "## Examples"])
            for ex in self.examples:
                parts.append(ex)
        if self.constraints:
            parts.extend(["", "## Constraints"])
            for c in self.constraints:
                parts.append(f"- {c}")
        parts.extend(["", "## Output format", self.output_format])
        return "\n".join(parts)
