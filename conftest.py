"""Configuration de la suite de teste utilisant Pytest."""

import pytest
from django.test import Client


@pytest.fixture()
def client():
    client = Client()

    yield client
