from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

from .models import CountdownMusic

def index(request):
    countdown_details = CountdownMusic.objects.get()

    return render(request, 'countdown.html', {'countdown_details': countdown_details})