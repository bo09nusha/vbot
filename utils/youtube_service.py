# https://rapidapi.com/DataFanatic/api/youtube-media-downloader/pricing

import requests
import re
import json


def extract_video_id(url):
    """
    YouTube URL-laridan video ID ajratib beruvchi funksiya.
    """
    patterns = [
        r"v=([a-zA-Z0-9_-]+)",  # Oddiy video
        r"shorts/([a-zA-Z0-9_-]+)",  # YouTube Shorts
        r"embed/([a-zA-Z0-9_-]+)",  # Embed video
        r"youtu\.be/([a-zA-Z0-9_-]+)",  # Youtu.be short link
        r"live/([a-zA-Z0-9_-]+)"  # YouTube Live Stream
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def video_downloader(video_id):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    querystring = {"videoId": video_id}

    headers = {
        "x-rapidapi-key": "47111c6935mshb6dc9f9bf0df08ap1521ddjsn083e23b6cb5e",
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)
    return result['videos']['items'][0]['url']

# print(video_downloader(link="https://www.youtube.com/watch?v=gt4-lTrkYuE&list=RDMMYabOz_9l3Yo&index=4"))