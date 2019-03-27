from typing import List

from django.db import models


# Create your models here.
class Video(models.Model):
    words = models.ManyToManyField('Word')
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)


class Word(models.Model):
    key_word = models.CharField(max_length=64)
    videos = models.ManyToManyField('Video')

    def get_all_videos(self) -> List[Video]:
        return self.videos.all()
