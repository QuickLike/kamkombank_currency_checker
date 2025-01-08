import asyncio

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from constraints import CITY, MAIN_URL, CURRENCY_URL


def get_points() -> dict[int, str]:
    resp = requests.get(MAIN_URL)
    soup = BeautifulSoup(resp.text, 'lxml')
    return {
        option.get('value'): option.text
        for option in soup.find('div', class_='cur__tablo1_change').find_all('option')
    }


def get_currencies():
    currencies = {}
    for id_, address in tqdm(get_points().items(), desc='Сбор курсов валют из пунктов обмена'):
        resp = requests.get(f'{CURRENCY_URL}{id_}')
        soup = BeautifulSoup(resp.text, 'lxml')
        trs = [tr for tr in soup.find('tbody').find_all('tr')]
        currencies[address] = {
            tds.find_all('td')[0].text: (tds.find_all('td')[1].text, tds.find_all('td')[2].text)
            for tds in trs[:-1]
        }
        currencies[address]['Комиссия'] = soup.find('strong').text
    return currencies


async def send_data(data: dict[str, dict[str, tuple]]):
    from constraints import bot, USER_ID

    if CITY is not None:
        await bot.send_message(USER_ID, f'Курсы валют по городу "{CITY.capitalize()}"')
    for address, currencies in data.items():
        if CITY is not None:
            if CITY.lower() not in address.lower():
                continue
        commission = currencies['Комиссия']
        del currencies['Комиссия']
        message_text = (
            "<u>" + address + "</u>\n\n" + '\n'.join([f'{cur[0]}:     {cur[1][0]} - {cur[1][1]}' for cur in currencies.items()]) + "\n\n"
            f'Комиссия: {commission}'
        )
        await bot.send_message(USER_ID, message_text, parse_mode='HTML')
        await asyncio.sleep(1.5)



if __name__ == '__main__':
    get_currencies()
