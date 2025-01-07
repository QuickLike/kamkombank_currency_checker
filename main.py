import asyncio
from pprint import pprint

from constraints import BOT_TOKEN, DELAY
from currency import get_currencies, send_data


async def main():
    while True:
        BOT_TOKEN = None
        if BOT_TOKEN is not None:
            await send_data(get_currencies())
        else:
            pprint(get_currencies())
        await asyncio.sleep(int(DELAY) * 60)


if __name__ == '__main__':
    asyncio.run(main())
