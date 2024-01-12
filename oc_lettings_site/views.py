"""Views"""
import logging

from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request: HttpRequest) -> HttpResponse:
    """
    Fonction vue pour la page d'accueil du site.

    :param request: Requête du client
    :type request: HttpRequest
    :return: Réponse http
    :rtype: HttpResponse
    """
    return render(request, "index.html")


def trigger_error(request: HttpRequest) -> HttpResponse:
    """
    Fonction vue qui loggue une erreur à des fins de test.

    :param request: Requête du client
    :type request: HttpRequest
    :return: Réponse "Server Error"
    :rtype: HttpResponse
    """
    logging.error("This is a volontary error.")
    return HttpResponseServerError()
