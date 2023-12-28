from django.test import Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed


def test_index_url():
    path = reverse("index")

    assert path == "/"
    assert resolve(path).view_name == "index"


def test_index_view(client: Client):
    path = reverse("index")
    response = client.get(path)

    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
    assertTemplateUsed(response, "index.html")
