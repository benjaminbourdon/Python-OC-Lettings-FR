"""Configuration de la partie admin du module Profiles."""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
