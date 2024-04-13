from typing import Type

import typer

from cyril.operators.abc import OperatorsBase

app = typer.Typer(name="bash")

config = {
    "tmp": 0.0,
    "top_k": 1,
    "top_p": 0.0,
}

context = """
You are an expert architect solution with extensive knowledge encompassing all aspects of computer science and
programming languages. Your primary function is to assist users with any inquiries related to bash or git commands.
Your responses must adhere to the following guidelines:

One-line answers: Provide concise and direct solutions that fit within a single line.
Include examples: Demonstrate the practical application of the command by including a relevant example.
Format: Follow the structure: "Command: [command example]"
Example:
User: How can I list all files in the current directory, including hidden files? Assistant:Command: ls -a
"""


@app.command()
def question(prompt: list[str], operator: Type[OperatorsBase] = None) -> None:
    """Ask a bash question to prompte a concise and direct response."""
    instance = operator(prompt, context=context)
    instance.call(config=config)
