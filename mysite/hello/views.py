from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная")


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")