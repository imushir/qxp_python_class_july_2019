"""
from django.urls import patterns, url
from django.views.generic import Templateview
from django.contrib import admin

urlpatterns = [
    'imageupload.views', url(r'^profile/', Templateview.as_view(
        template_name = 'profile.html')), url(r'^saved/', 'SaveProfile', name = 'saved')
]
"""
from django.urls import path
from . import views

app_name = "imageupload"
urlpatterns = [
    # /imageupload/
    path("", views.SaveProfile, name="saved"),
    ]