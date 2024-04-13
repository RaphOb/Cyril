import os

import pytest

from cyril.load_env.load import LoadEnv
from cyril.operators.gemini import Gemini
from cyril.operators.open_ai import OpenAi


def test_load_env_without_env():
    # test without env
    with pytest.raises(ValueError):
        LoadEnv()


def test_load_env_with_env():
    # test with env
    os.environ["CYRIL_OPEN_API"] = "FAKE_API"
    assert LoadEnv().instance == OpenAi
    del os.environ["CYRIL_OPEN_API"]
    os.environ["PROJECT_ID"] = "test"
    assert LoadEnv().instance == Gemini
