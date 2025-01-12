import requests
import os
import asyncio

import random

from telegram import Bot
from dotenv import load_dotenv


def get_link_of_the_random_comic_book():
    comic_book_link = 'https://xkcd.com/info.0.json'
    comic_book_response = requests.get(comic_book_link)
    comic_book_response.raise_for_status()
    comic_book_image = comic_book_response.json()
    comic_book_number = int(comic_book_image['num'])

    random_comic_book_number =  random.randint(1, comic_book_number)
    random_comic_book_link = f'https://xkcd.com/{random_comic_book_number}/info.0.json'
    random_comic_book_response = requests.get(random_comic_book_link)
    random_comic_book = random_comic_book_response.json()

    return random_comic_book


def get_image_of_the_comic(comic_link):
    image_comic_book = comic_link['img']
    filename = 'comic_book.png'

    image_comic_book_response = requests.get(image_comic_book)
    image_comic_book_response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(image_comic_book_response.content)

    return filename


def get_text_from_comic_book_image(comic_link):

    return comic_link['alt']


async def send_message(tg_bot_token, tg_chat_id, filename, text):
    bot = Bot(token=tg_bot_token)    
    await bot.send_photo(chat_id=tg_chat_id, photo=filename, caption=text)



def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    comic_link = get_link_of_the_random_comic_book()
    filename = get_image_of_the_comic(comic_link)
    text = get_text_from_comic_book_image(comic_link)

    asyncio.run(send_message(tg_bot_token, tg_chat_id, filename, text))

    os.remove(filename)


if __name__ == "__main__":
    main()