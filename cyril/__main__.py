from halo import Halo

from cyril.commands.register import app
from cyril.config import settings

with Halo(text=settings.TEXT, spinner=settings.SPINNER):
    app()
