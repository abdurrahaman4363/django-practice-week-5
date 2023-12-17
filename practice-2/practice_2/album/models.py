from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
