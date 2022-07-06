import os
from dotenv import load_dotenv
import pytest


load_dotenv(verbose=True)
pytest.url = os.getenv("GITEA_URL")
pytest.token = os.getenv("GITEA_TOKEN")


def test_if_environment_variables_are_set():
    assert pytest.url is not None
    assert pytest.token is not None
    assert pytest.url != ""
    assert pytest.token != ""
