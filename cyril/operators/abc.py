from abc import abstractmethod


class OperatorsBase:
    def __init__(self, prompt: list[str], context: str):
        self.prompt = " ".join(prompt)
        self.context = context

    @abstractmethod
    def call(self, config: dict = None):
        """Call the API"""
        pass
