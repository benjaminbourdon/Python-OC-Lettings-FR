"""Module des fonctions de rendu des vues du module Lettings."""

import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
def index(request: HttpRequest) -> HttpResponse:
    """
    Fonction vue pour la page d'accueil de la partie location.

    :param request: Requête du client
    :type request: HttpRequest
    :return: Réponse http
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request: HttpRequest, letting_id: str) -> HttpResponse:
    """
    Fonction vue pour la page de détail d'une location.

    :param request: Requête du client
    :type request: HttpRequest
    :param letting_id: Identifiant de la location
    :type request: String
    :return: Réponse http
    :rtype: HttpResponse
    """

    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist as e:
        logging.error(
            "Tried to access a non-existant letting.", extra={"letting_id": letting_id}
        )
        raise e

    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
