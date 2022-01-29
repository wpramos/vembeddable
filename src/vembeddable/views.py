from django.http.response import HttpResponse

import logging

import os

import requests

from django.shortcuts import render

from googleapiclient.discovery import build

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
)

# Create your views here.


def index(request):
    return render(request, 'vembeddable/index.html')


def search(request):
    # GET API KEY
    youtube_api_key = os.environ['VEMBEDDABLE_YOUTUBE_API_KEY']

    # BUILD YouTube API SERVICE OBJECT
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)

    # CREATE HTTP REQUEST OBJECT AND EXECUTE REQUEST
    query = request.GET['q']

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
        'query': query,
        'youtube_api_response': youtube_api_response,
    }

    return render(request, 'vembeddable/search.html', context)


def verify(request, video_id):
    response = requests.get('https://www.youtube.com/embed/' + video_id)

    # 'error_element' is a sequence of text, the presence of which in
    # the HTTP response to the above request implies that the video will
    # not play on the embedded player.
    error_element = '<meta name="robots" content="noindex">'

    if error_element in response.text:
        response_text = 'isError'
    else:
        response_text = ''

    return HttpResponse(response_text)
