import requests
import json
from urllib import parse, request


def send_gif(gif_to_search='Error'):
  url = "http://api.giphy.com/v1/gifs/search"
  params = parse.urlencode({
    "q": gif_to_search,
    "api_key": "Dh2pIw38gCGCDIYl3GYDC145V60pUg24",
    "limit": "1"
  })
  with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())
  print(f'Here is your gif of {gif_to_search}', data['data'][0]['images']['original']['url'])
  return data['data'][0]['images']['original']['url']

search = input("Gif you want to find: ")
send_gif(search)
send_gif('Sun')

