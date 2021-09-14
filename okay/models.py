from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, default='no photo title')
    album = models.CharField(max_length=100, default='no album title')
    preview_url = models.CharField(max_length=200, null=True)
    # owner = models.ForeignKey(
    #     'users.User', related_name='', on_delete=models.CASCADE)

    def __str__(self):
      return self.title