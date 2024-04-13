from functools import partial

from _pytest.fixtures import fixture
from typer.testing import CliRunner

from cyril.commands.register import app


@fixture(scope="session")
def get_runner():
    cli_runner = CliRunner()
    yield partial(cli_runner.invoke, app)


class LoadEnvFixture:
    def __init__(self, *args, **kwargs):
        self._instance = None

    @property
    def instance(self):
        return self._instance
