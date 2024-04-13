import json
import os
from collections import defaultdict

import google.auth.transport.requests
import httpx
import typer
from google.auth import default
from rich.markdown import Markdown

from cyril.config import console
from cyril.operators.abc import OperatorsBase


class Gemini(OperatorsBase):
    """Gemini API, While I have not API Key, I will use the CURL command to make the request."""

    def __init__(self, prompt: list[str], context: str):
        super().__init__(prompt, context)
        self.api_key = os.getenv("PROJECT_ID")

    @staticmethod
    def get_credentials():
        credentials, _ = default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        return credentials

    def _prepare_data(self, config: dict) -> tuple[dict, dict]:
        """Prepare the data for the API call"""
        access_token = self.get_credentials().token
        data = {
            "contents": [
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
                {
                    "role": "user",
                    "parts": {"text": f"My question is: {self.prompt}"},
                },
            ],
            "generation_config": {
                "temperature": config.get("tmp", 0.5),
                "topP": config.get("topP", 0.5),
                "topK": config.get("topK", 20),
            },
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json; charset=utf-8",
        }
        return data, headers

    def call(self, config: dict = None):
        """
        Call the API
        """
        if config is None:
            config = defaultdict()
        data, headers = self._prepare_data(config)
        base_url = (
            f"https://us-central1-aiplatform.googleapis.com/v1/projects/{self.api_key}/locations/us-central1"
            f"/publishers/google/models/gemini-1.0-pro:streamGenerateContent?alt=sse"
        )
        try:
            response = httpx.post(base_url, json=data, headers=headers)
            resp = ""
            for chunk in response.text.split("\r\n"):
                if chunk.startswith("data:"):
                    data = json.loads(chunk.replace("data: ", ""))
                    resp += data["candidates"][0]["content"]["parts"][0]["text"]
            md = Markdown(resp)
            console.print(md)
        except Exception:
            typer.echo("An error occurred: Probably due to misspelled prompt.")
