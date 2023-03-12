from django.urls import path
from hello.views import *

urlpatterns = [
    path("", index),
]