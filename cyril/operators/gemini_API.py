import os

import google.generativeai as genai
from rich.markdown import Markdown

from cyril.config import console
from cyril.operators.abc import OperatorsBase


class GeminiApi(OperatorsBase):
    """Gemini API Operator"""

    def __init__(self, prompt: list[str], context: str):
        super().__init__(prompt, context)
        self.api_key = os.getenv("CYRIL_GEMINI")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": {
                        "text": self.context,
                    },
                },
                {
                    "role": "model",
                    "parts": {"text": "Sure! Ask me a question:"},
                },
            ]
        )

    def call(self, config: dict = None):
        """Call the API"""
        response = self.chat.send_message(self.prompt)
        md = Markdown(response.text)
        console.print(md)
