import requests
import bs4 as BeautifulSoup
import time

def ticker_symbols():
            req= requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDroWU7bNZMAgKue9pvS5gTvHe4OLHQKrQ&channelId=UCmA06PHZc6O--2Yw4Vt4Wug&part=snippet,id&order=date&maxResults=1')
            video_id = req.json()['items'][0]['id']['videoId']
            get_description = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&id='+ video_id + '&key=AIzaSyDroWU7bNZMAgKue9pvS5gTvHe4OLHQKrQ')
            description = get_description.json()['items'][0]['snippet']['description']
            description_list = description.split()
            tickers = []

            for strings in description_list:
                if len(strings) >= 3 and len(strings) <5 and strings.isalpha() and strings.isupper():
                    tickers.append(strings)
            return tickers        

x=0
while x == 0:
    r = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDroWU7bNZMAgKue9pvS5gTvHe4OLHQKrQ&channelId=UCmA06PHZc6O--2Yw4Vt4Wug&part=snippet,id&order=date&maxResults=1')
    recentvideo = r.json()['items'][0]['snippet']['title']
    thefile = open("oldvideo.txt", "r")
    oldvideo= thefile.read()

    if recentvideo != oldvideo:
        writingfile= open("oldvideo.txt", "w")
        writingfile.write(recentvideo)
        writingfile.close
        ticker_symbols()

    time.sleep(60)
    