import json
import aiohttp
from enum import Enum


class METHOD(Enum):
    GET = 1
    POST = 2
    HEAD = 3


async def do(session: aiohttp.ClientSession, url: str, method: METHOD, payload: dict):
    if method.value == 1:
        r = await session.request(method.name, url, params=json.dumps(payload))
    elif method.value == 2:
        r = await session.request(method.name, url, data=json.dumps(payload))
    else:
        r = await session.request(method.name, url)
    if isinstance(r, aiohttp.ClientResponse):
        if 200 == r.status:
            rt = await r.text()
            return rt


async def _():
    async with aiohttp.ClientSession() as session:
        r = await do(session, url='http://baidu.com', method=METHOD.GET, payload={})
        print(r)


if __name__ == '__main__':
    import os
    import asyncio

    if 'nt' == os.name:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_())
    # print(METHOD.GET.name)
