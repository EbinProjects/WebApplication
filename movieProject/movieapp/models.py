from django.db import models


# Create your models here.


class MovieTimes(models.Model):
    name = models.CharField(max_length=240)
    desc = models.TextField(max_length=240)
    year = models.IntegerField()
    images = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    middle = models.CharField(max_length=240)
    first = models.CharField(max_length=240)
    last = models.CharField(max_length=240)
    username = models.CharField(max_length=240)
    password = models.CharField(max_length=240)
    confirm = models.CharField(max_length=240)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.username
