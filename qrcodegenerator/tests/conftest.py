import pytest

from django.test import Client


@pytest.fixture(scope="function")
def client() -> Client:
    """
    Fixture to provide an client
    :return: Client
    """
    yield Client()
