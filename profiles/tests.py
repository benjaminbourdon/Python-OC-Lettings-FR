"""Tests liés au module Profiles."""

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Profile


@pytest.mark.django_db
def test_profile_model():
    """Teste du modèle du module Profile."""

    user = User.objects.create(username="Coco")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    expected_adress = "Coco"
    assert str(profile) == expected_adress


def test_index_profiles_url():
    """Teste l'url de l'index du module Profiles"""

    path = reverse("profiles_index")

    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_index_profiles_view_no_profile(client: Client):
    """Teste le rendu de l'index de l'index du module Profiles en l'absence de données."""

    path = reverse("profiles_index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Profiles</h1>" in response.content.decode()
    assert "<p>No profiles are available.</p>" in response.content.decode()
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_index_profiles_view_with_profile(client: Client):
    """Teste le rendu de l'index de l'index du module Profiles en présence de données."""

    username = "Coco"
    user = User.objects.create(username=username)
    Profile.objects.create(user=user, favorite_city="Paris")

    path = reverse("profiles_index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Profiles</h1>" in response.content.decode()
    assert (
        f'<a href="/profiles/{username}/">{username.capitalize()}</a>'
        in response.content.decode()
    )
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_display_profiles_url():
    """Teste l'url d'une page de présentation d'un profile."""

    username = "Coco"
    user = User.objects.create(username=username)
    Profile.objects.create(user=user, favorite_city="Paris")
    path = reverse("profile", args={username})

    assert path == f"/profiles/{username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_display_profiles_view(client: Client):
    """Teste le rendu d'une page de présentation d'un profile."""

    username = "Coco"
    city = "Paris"
    user = User.objects.create(username=username)
    Profile.objects.create(user=user, favorite_city=city)

    path = reverse("profile", args={username})
    response = client.get(path)

    assert response.status_code == 200
    assert f"<title>{username}</title>" in response.content.decode()
    assert (
        f"<p><strong>Favorite city :</strong> {city}</p>" in response.content.decode()
    )
    assert f"{username}</h1>" in response.content.decode()
    assertTemplateUsed(response, "profiles/profile.html")
