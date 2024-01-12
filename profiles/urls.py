"""Source des routes du module Profiles."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
