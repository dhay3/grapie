import aiohttp_t.utils  as u
import aiohttp
import os
import asyncio
from lxml import etree

url = 'https://movie.douban.com/top250'


async def list_top250_xpath(url):
    conn = aiohttp.TCPConnector(ssl=False, ttl_dns_cache=30)
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout, connector=conn) as session:
        r = await u.do(session, url, u.METHOD.GET, None)
        x_dom = etree.HTML(r)
        x_lis = x_dom.xpath('//div[@id="content"]/descendant::ol/li')
        for x_li in x_lis:
            title = ''.join([_.text for _ in
                             x_li.xpath('./descendant::div[@class="hd"]/descendant::span[@class="title"]')])
            description = x_li.xpath('./descendant::div[@class="bd"]/p/text()')[1].strip()
            star = x_li.xpath('./descendant::div[@class="star"]/span[@class="rating_num"]/text()')[0]
            print(title, description, star)


if __name__ == '__main__':
    tasks = []
    if 'nt' == os.name:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    for idx in range(0, 10):
        tasks.append(list_top250_xpath(f'{url}?start={idx * 25}'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
