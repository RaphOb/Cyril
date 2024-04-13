import os
from collections import defaultdict

from openai import OpenAI
from rich.markdown import Markdown

from cyril.config import console
from cyril.operators.abc import OperatorsBase


class OpenAi(OperatorsBase):
    """OpenAI API Operator"""

    def __init__(self, prompt: list[str], context: str):
        super().__init__(prompt, context)
        self.api_key = os.getenv("CYRIL_OPEN_API")

        self.client = OpenAI(
            api_key=self.api_key,
        )

    def call(self, config: dict = None):
        """
        Call the API
        """
        if config is None:
            config = defaultdict()
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=config.get("tmp", 0.5),
            top_p=config.get("top_p", 0.5),
            messages=[
                {
                    "role": "system",
                    "content": self.context,
                },
                {"role": "user", "content": self.prompt},
            ],
        )
        md = Markdown(response.choices[0].message.content)
        console.print(md)
