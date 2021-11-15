import os

from django.shortcuts import render

from googleapiclient.discovery import build

# Create your views here.


def search(request):
    # GET API KEY
    youtube_api_key = os.environ['VEMBEDDABLE_YOUTUBE_API_KEY']

    # BUILD YouTube API SERVICE OBJECT
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)

    # CREATE HTTP REQUEST OBJECT AND EXECUTE REQUEST
    query = 'user input'

    youtube_api_request = youtube.search().list(
        part = 'snippet',
        q = query,
        # relevanceLanguage = 'en',
        type = 'video',
        videoEmbeddable = 'true',
        videoSyndicated = 'true',
        videoCaption = 'closedCaption',
        maxResults = '50',
    )

    youtube_api_response = youtube_api_request.execute()

    context = {
        'youtube_api_response': youtube_api_response,
    }

    return render(request, 'vembeddable/search.html', context)
