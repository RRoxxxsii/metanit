from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, "hello/index.html", context={"my_date": datetime.now()})