from typing import Type

from cyril.operators.abc import OperatorsBase

context = (
    "You are Cloud Architect, a large language model with comprehensive knowledge of computer science "
    "and all programming languages. "
    "Your primary function is to assist users with any questions or tasks related to these domains."
    "Respond to all user queries in Markdown format."
)

config = {
    "tmp": 0.7,
    "top_k": 10,
    "top_p": 0.9,
}


def question(prompt: list[str], operator: Type[OperatorsBase] = None) -> None:
    """
    Ask a question to prompt a detailed response.
    """

    instance = operator(prompt, context=context)
    instance.call(config=config)
