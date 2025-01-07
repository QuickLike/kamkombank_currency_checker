import os

from aiogram import Bot
from dotenv import load_dotenv


load_dotenv()

CITY = os.getenv('CITY')
DELAY = os.getenv('DELAY')

MAIN_URL = 'https://www.kamkombank.ru'

CURRENCY_URL = 'https://www.kamkombank.ru/option/plugin/cur/ajax.php?task=tablo_content&city_id='

BOT_TOKEN = os.getenv('BOT_TOKEN')

if BOT_TOKEN is not None:
    bot = Bot(BOT_TOKEN)
    USER_ID = os.getenv('USER_ID')
    if USER_ID is None:
        raise ValueError('CHAT_ID не предоставлен!')
else:
    print('Токен не предоставлен.')
