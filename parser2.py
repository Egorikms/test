import aiohttp
from fake_useragent import UserAgent
import asyncio
from bs4 import BeautifulSoup as BS


url = "https://www.globus.ru/restaurant/"
Headers = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=Headers) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")
            items = soup.find_all("a", {"class": "pim-list__item"})

            for item in items:
                price = item.find("span", {"class": "pim-list__item-price-actual-main"}).text.strip()
                print(price)
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
   
