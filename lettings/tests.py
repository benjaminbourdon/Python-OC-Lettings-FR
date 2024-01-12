"""Tests liés au module Lettings."""

import pytest
from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Address, Letting


@pytest.mark.django_db
def test_lettings_models():
    """Teste les modèles du module Lettings."""

    adress = Address.objects.create(
        number=2, street="main street", city="megalopole", zip_code=10000
    )
    expected_adress = "2 main street"
    assert str(adress) == expected_adress

    letting = Letting.objects.create(title="Big House", address=adress)
    expected_letting = "Big House"
    assert str(letting) == expected_letting


def test_index_lettings_url():
    """Teste l'url de l'index de la partie Lettings."""

    path = reverse("lettings_index")

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_index_lettings_view_no_letting(client: Client):
    """Teste le rendu de l'index de la partie Lettings en l'absence de données."""

    path = reverse("lettings_index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Lettings</h1>" in response.content.decode()
    assert "<p>No lettings are available.</p>" in response.content.decode()
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_index_lettings_view_with_letting(client: Client):
    """Teste le rendu de l'index de la partie Lettings en présence de données."""

    letting_title = "Big House"
    adress = Address.objects.create(
        number=2, street="main street", city="megalopole", zip_code=10000
    )
    letting = Letting.objects.create(title=letting_title, address=adress)

    path = reverse("lettings_index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Lettings</h1>" in response.content.decode()
    assert (
        f'<a href="/lettings/{letting.id}/">{letting_title}</a>'
        in response.content.decode()
    )
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_display_lettings_url():
    """Teste l'url de la page d'une location."""

    letting_title = "Big House"
    adress = Address.objects.create(
        number=2, street="main street", city="megalopole", zip_code=10000
    )
    letting = Letting.objects.create(title=letting_title, address=adress)
    path = reverse("letting", args={letting.id})

    assert path == f"/lettings/{letting.id}/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_display_lettings_view(client: Client):
    """Teste le rendu de la page d'une location."""

    letting_title = "Big House"
    adress = Address.objects.create(
        number=2, street="main street", city="megalopole", zip_code=10000
    )
    letting = Letting.objects.create(title=letting_title, address=adress)
    path = reverse("letting", args={letting.id})
    response = client.get(path)

    assert response.status_code == 200
    assert f"<title>{letting_title}</title>" in response.content.decode()
    assert f"<p>{adress.number} {adress.street}</p>" in response.content.decode()
    assert f"{letting_title}</h1>" in response.content.decode()
    assertTemplateUsed(response, "lettings/letting.html")
