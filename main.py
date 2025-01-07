import asyncio

from currency import get_currencies, send_data


async def main():
    while True:
        await send_data(get_currencies())
        await asyncio.sleep(1800)


if __name__ == '__main__':
    asyncio.run(main())
