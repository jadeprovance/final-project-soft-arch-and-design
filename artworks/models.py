# artworks/models.py

from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
