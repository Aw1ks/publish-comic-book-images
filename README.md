# publish-comic-book-images
In this project, photos of the [comic](https://xkcd.com/info.0.json) are downloaded and published in the telegram channel.
## How to install 
This project uses libraries such as: [os](https://docs.python.org/3/library/os.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [asyncio](https://docs.python.org/3/library/asyncio.html), [random](https://docs.python.org/3/library/random.html) and [telegram](https://core.telegram.org/bots/api#available-methods).
You need to get the bot's API token and also get chat ID of your telegram channrl  using [bot father](https://core.telegram.org/bots/tutorial).

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To save the data from prying eyes, we will create an .env file in which we will place: `tg_bot_token` and `tg_chat_id`. Let's do it this way:
```
TG_BOT_TOKEN = 'the secret key that you received'
TG_CHAT_ID = 'the secret key that you received'
```
## Environment variables
Environment variables are key—value pairs that determine the settings and behavior of the operating system and programs. You can read more here [More about Environment Variables](https://habr.com/ru/companies/gnivc/articles/792082/)
The variables accept the `API token` and `chat ID` from the bot father from the file`.env` using the [os](https://docs.python.org/3/library/os.html) library using the method:`.getenv`
```
tg_bot_token = os.getenv('TG_BOT_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
```
## How to launch
To run the script, you need to enter it into the console according to this example:
```
python main.py
```
