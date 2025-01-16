import requests
import os
import random
import telegram
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


def send_message(tg_bot_token, tg_chat_id, filename, comic_text):
    bot = telegram.Bot(token=tg_bot_token)
    bot.send_photo(chat_id=tg_chat_id, photo=open(filename, 'rb'), caption=comic_text)


def main():
    load_dotenv()

    tg_bot_token = os.environ.get('TG_BOT_TOKEN')
    tg_chat_id = os.environ.get('TG_CHAT_ID')

    try:
        comic_link = get_link_of_the_random_comic()
        filename = get_comic_image(comic_link)
        comic_text = comic_link['alt'] 
        send_message(tg_bot_token, tg_chat_id, filename, comic_text)
    finally:
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    main()
