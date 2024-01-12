"""Module des fonctions de rendu des vues du module Profiles."""

import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Profile


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request: HttpRequest) -> HttpResponse:
    """
    Fonction vue pour la page d'accueil de la partie profiles.

    :param request: Requête du client
    :type request: HttpRequest
    :return: Réponse http
    :rtype: HttpResponse
    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Fonction vue pour la page de détail d'un profile.

    :param request: Requête du client
    :type request: HttpRequest
    :param username: Nom d'utilisateurice concerné
    :type request: String
    :return: Réponse http
    :rtype: HttpResponse
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist as e:
        logging.error(
            "Tried to access a non-existant profile.", extra={"username": username}
        )
        raise e

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
