"""Tests de la partie centrale de l'application."""

from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_url():
    """Teste l'url de la page d'accueil."""

    path = reverse("index")

    assert path == "/"
    assert resolve(path).view_name == "index"


def test_index_view(client: Client):
    """Teste le rendu de la page d'accueil."""

    path = reverse("index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
    assertTemplateUsed(response, "index.html")
