from django.shortcuts import render
from django.contrib.auth.models import User

# from musician.models import Musician
from album.models import Album


def musician_list(request):
    musicians = User.objects.all()
    return render(request, "musician_list.html", {"musicians": musicians})
