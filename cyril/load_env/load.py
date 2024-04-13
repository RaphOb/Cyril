import os

from cyril.config import settings
from cyril.operators.gemini import Gemini
from cyril.operators.open_ai import OpenAi


class LoadEnv:
    def __init__(self):
        required_vars = ["CYRIL_OPEN_API", "CYRIL_GEMINI", "PROJECT_ID"]
        if not any(var in os.environ for var in required_vars):
            raise ValueError(settings.HELP_GENERAL)
        self._initialize_operators()

    def _initialize_operators(self):
        # Check and print the status of each environment variable if set
        if "CYRIL_OPEN_API" in os.environ:
            self._instance = OpenAi
            return
        if "CYRIL_GEMINI" in os.environ:
            print("CYRIL_GEMINI is set.")
        if "PROJECT_ID" in os.environ:
            self._instance = Gemini

    @property
    def instance(self):
        """Return the instance of the operator."""
        return self._instance
