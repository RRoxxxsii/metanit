from django.urls import path
from django.views.generic import TemplateView

from hello.views import *

from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index),
]