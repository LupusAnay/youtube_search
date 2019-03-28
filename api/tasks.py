import logging

from celery import shared_task
from googleapiclient.discovery import build

from api.models import Word, Video
from youtube_search.settings import GOOGLE_API_KEY

DEVELOPER_KEY = GOOGLE_API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)


def search_videos_by_keyword(client, keyword):
    response = client \
        .search() \
        .list(part='snippet', type='video', order='date', q=keyword) \
        .execute()
    return response


@shared_task
def fetch_videos():
    # there is a big lack of validation and error checking
    client = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                   developerKey=DEVELOPER_KEY)
    words = Word.objects.all()
    for word in words:
        raw_search_data = search_videos_by_keyword(client, word.key_word)
        raw_videos = raw_search_data['items']
        for raw_video in raw_videos:
            video_id = raw_video['id']['videoId']
            title = raw_video['snippet']['title']
            url = f'https://www.youtube.com/watch?v={video_id}'
            (video, _) = Video.objects.get_or_create(title=title, url=url)
            video.save()
            word.videos.add(video)
            word.save()
