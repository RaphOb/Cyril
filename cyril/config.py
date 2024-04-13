from pydantic_settings import BaseSettings
from rich.console import Console

console = Console()


class Settings(BaseSettings):
    # Required settings
    HELP_GENERAL: str = """ Ensure that this application functions correctly by meeting one of the following prerequisites:\n
 - Have an CYRIL_OPEN_API API key set up.\n
 - Have CYRIL_GEMINI API key set up.(NOT IMPLEMENTED)\n
 - Have a PROJECT_ID project set up with Application Default Credentials (ADC) configured.
"""
    APIS_LIST: list[str] = ["CYRIL_OPEN_API", "CYRIL_GEMINI", "PROJECT_ID"]
    TEXT: str = ""
    SPINNER: str = "earth"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
