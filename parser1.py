import asyncio
import aiohttp

from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://www.globus.ru/restaurant/" 
HEADERS = {"User-Agent": UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response: 
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")
            items = soup.find_all("a", {"class": "pim-list__item "}) 
            
            for item in items:
                title = item.find("div", {"class": "pim-list__item-title js-crop-text"})
                link = title.get("href")
                price = item.find("span", "pim-list__item-price-actual-main").text.strip()
                print(f"{title.text.strip()} | {price} | https://www.globus.ru{link}")
                print()

if __name__ == '__main__':
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(main())


