import telebot
import requests
import json
from urllib import parse, request

bot = telebot.TeleBot('7297224482:AAFTuziQAbP0K1c1r7_ATgb8VgCT6QEO2Gw')

def get_gif(message) -> str:
    search = message.text
    """Get a gif"""
    url = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
        "q": search,
        "api_key": "Dh2pIw38gCGCDIYl3GYDC145V60pUg24",
        "limit": "1"
    })
    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    return data['data'][0]['images']['original']['url']

def fetch_search(message):
    try:
        gif = get_gif(message)
        bot.send_message(message.chat.id, f'Here\'s your GIF')
        bot.send_message(message.chat.id, gif)
    except:
        bot.send_message(message.chat.id, 'Oh no, something went wrong. Try again')

@bot.message_handler(commands=['gif'], func=lambda message: True)
def main(message):
    text = 'Hi! Search for GIF, just print your prompt.'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, fetch_search)

bot.infinity_polling()