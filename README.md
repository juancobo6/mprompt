# mprompt

**mprompt** is a CLI tool that helps you generate high-quality, structured prompts for your projects. Instead of writing prompts from scratch, you have a short conversation with an AI assistant that asks the right questions and turns your ideas into a ready-to-use prompt—then copies it to your clipboard.

## What it does

- **Guided conversation**: You describe what you want to prompt for (e.g. “I need a prompt that makes the AI act like a senior DevOps engineer and write deployment runbooks”). The assistant asks clarifying questions about role, audience, task, constraints, and output format.
- **Structured output**: When it has enough information, it produces a structured prompt with:
  - **Persona** — the role or identity the AI should adopt
  - **Context** — background, audience, or relevant history
  - **Task** — the main goal or mission
  - **Examples** — optional few-shot examples (invented by the assistant when appropriate)
  - **Constraints** — rules, limits, or things to avoid
  - **Output format** — structure and tone of the output (e.g. Markdown, JSON, formal email)
- **Clipboard**: The final prompt is copied to your clipboard so you can paste it into your IDE, docs, or another tool.

## Requirements

- **Python 3.12+**
- **Google API key**: Set the `GOOGLE_API_KEY` environment variable. The tool uses Google’s Gemini model (via [pydantic-ai](https://ai.pydantic.dev/)).

## Installation

From the project root:

```bash
pip install .
```

Or install in development mode:

```bash
pip install -e .
```

## Usage

1. Set your API key:

   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

   On Windows (PowerShell):

   ```powershell
   $env:GOOGLE_API_KEY = "your-api-key-here"
   ```

2. Run the CLI:

   ```bash
   mprompt
   ```

3. Answer the assistant’s questions. When it has enough information, it will show you the generated prompt and ask if you’re okay with it. Reply `y` to accept (and copy to clipboard), or describe what you’d like to change for another round.

4. Paste the prompt wherever you need it (Cursor, ChatGPT, your app, etc.).

## Example flow

```
> Agent: Hello, I'm a meta-prompting assistant. I'll help you generate a high-quality prompt for your project. Please describe what you would like to prompt.

> You: I want a prompt for writing Git commit messages in conventional commits style.

> Agent: Who will be using this—solo devs or a team? Any project conventions?

> You: Small team, Python project, we use feat/fix/docs etc.

… (a few more exchanges) …

> Agent: [shows structured prompt]

> Are you okay with this output? (y for yes, or describe what you would like to change): y

> Copied to clipboard.
```

## License

MIT. See the project metadata for author and details.
