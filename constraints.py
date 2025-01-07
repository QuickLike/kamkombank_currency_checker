import os

from aiogram import Bot
from dotenv import load_dotenv


load_dotenv()

CITY = os.getenv('CITY')

USER_ID = os.getenv('USER_ID')

MAIN_URL = 'https://www.kamkombank.ru'

CURRENCY_URL = 'https://www.kamkombank.ru/option/plugin/cur/ajax.php?task=tablo_content&city_id='

bot = Bot(os.getenv('BOT_TOKEN'))
