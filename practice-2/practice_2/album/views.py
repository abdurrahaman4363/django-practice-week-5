from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_album(request):
    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.instance.musician = request.user
            album_form.save()
            return redirect("add_album")

    else:
        album_form = forms.AlbumForm()
    return render(request, "add_album.html", {"form": album_form})


@login_required
def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)

    if request.method == "POST":
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.instance.musician = request.user
            album_form.save()
            return redirect("musician_list")

    return render(request, "add_album.html", {"form": album_form})


@login_required
def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect("musician_list")
