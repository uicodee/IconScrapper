import aiohttp
from data.config import BASE_URL
from bs4 import BeautifulSoup
SIZE = 2048


async def get_icons(query: str) -> list:
    links = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BASE_URL.format(query=query)) as response:
            r = await response.text()
            soup = BeautifulSoup(r, "lxml")
            images = soup.find_all("div", class_="icon-preview-bg")
            for img in images:
                link = (img.img['src']).split(" ")[0]
                # 2048 px * 2048 px
                photo = (link.split("-128"))[0] + f"-{SIZE}.png"
                links.append(photo)
    return links


async def paginator(data: list, page: int, products_page: int) -> list:
    result_list = []
    key_count = 0
    for i in range(0, len(data), products_page):
        key_count += 1
        result_list.append({
            key_count: data[i:i + products_page]
        })

    return result_list[page-1][page]
