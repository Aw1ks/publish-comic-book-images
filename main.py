import requests
import os
import asyncio

import random

from telegram import Bot
from dotenv import load_dotenv


def get_link_of_the_random_comic():
    comic_link = 'https://xkcd.com/info.0.json'
    comic_response = requests.get(comic_link)
    comic_response.raise_for_status()
    comic_image = comic_response.json()
    comic_number = int(comic_image['num'])

    random_index_comic = random.randint(1, comic_number)
    random_comic_link = f'https://xkcd.com/{random_index_comic}/info.0.json'
    comic_link_response = requests.get(random_comic_link)
    comic_link_response.raise_for_status()
    random_comic = comic_link_response.json()

    return random_comic


def get_comic_image(comic_link):
    comic_image = comic_link['img']
    filename = 'comic.png'

    comic_image_response = requests.get(comic_image)
    comic_image_response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(comic_image_response.content)

    return filename


async def send_message(tg_bot_token, tg_chat_id, filename, text):
    bot = Bot(token=tg_bot_token)    
    await bot.send_photo(chat_id=tg_chat_id, photo=filename, caption=text)


def main():
    load_dotenv()

    tg_bot_token = os.environ['TG_BOT_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']

    asyncio.run(send_message(tg_bot_token, tg_chat_id, filename, text))

    try:
        comic_link = get_link_of_the_random_comic()
        filename = get_comic_image(comic_link)
        text = comic_link['alt']
    finally:
        os.remove(filename)


if __name__ == "__main__":
    main()