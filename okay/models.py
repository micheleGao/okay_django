from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='photo')
    title = models.CharField(max_length=100, default='no photo title')
    album = models.CharField(max_length=100, default='no album title')
    # preview_url = models.CharField(max_length=200, null=True)
    # owner = models.ForeignKey(
    #     'users.User', related_name='', on_delete=models.CASCADE)

    def __str__(self):
      return self.title

# class Review(models.Model):
#     artist = models.ForeignKey(
#         Artist, on_delete=models.CASCADE, related_name='reviews')
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     # author= models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     # owner = models.ForeignKey(
#     #     'owner.username', related_name='reviews', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title