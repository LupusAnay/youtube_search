from typing import List

from django.db import models


# Create your models here.
class Video(models.Model):
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class Word(models.Model):
    key_word = models.CharField(max_length=50)

    def get_all_videos(self) -> List[Video]:
        return Video.objects.filter(word_id=self.id)
