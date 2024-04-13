from functools import partial

from pytest_mock import MockerFixture

from tests.conftest import LoadEnvFixture


def test_command_bash(get_runner: partial, mocker: MockerFixture):
    mocker.patch("cyril.commands.register.LoadEnv", return_value=LoadEnvFixture)
    mocker.patch(
        "cyril.commands.register.sh",
    )

    result = get_runner(["bash", "How can I recursively remove a directory using rm?"])

    assert result.exit_code == 0


def test_command_ask(get_runner: partial, mocker: MockerFixture):
    mocker.patch("cyril.commands.register.LoadEnv", return_value=LoadEnvFixture)
    mocker.patch(
        "cyril.commands.register.q",
    )

    result = get_runner(["ask", "How can I read documentation in Python?"])

    assert result.exit_code == 0


def test_command_terraform(get_runner: partial, mocker: MockerFixture):
    mocker.patch("cyril.commands.register.LoadEnv", return_value=LoadEnvFixture)
    mocker.patch(
        "cyril.commands.register.tf",
    )

    result = get_runner(["terraform", "TERRAFORM?"])

    assert result.exit_code == 0


def test_command_keyboard(get_runner: partial, mocker: MockerFixture):
    mocker.patch("cyril.commands.register.LoadEnv", return_value=LoadEnvFixture)
    mocker.patch(
        "cyril.commands.register.kb",
    )

    result = get_runner(["keyboard", "KEYBOARD?"])

    assert result.exit_code == 0
