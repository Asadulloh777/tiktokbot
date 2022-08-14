"https://www.tiktok.com/@nor10122/video/7037155617491913986"

import requests
import json
def link(link):


    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "64b5f788b5mshd9452863cc50d31p1a9174jsna667ab7e79c4",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    return {'Video' : rest['video'][0]}
