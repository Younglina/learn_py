"""
example06.py - 异步I/O版本爬虫
"""
import asyncio
import json
import os
import re

import aiofile
import aiohttp


async def download_picture(session, url, filename):
    filename2 = ''.join(re.findall(r"\w+", filename))
    filetype = url[url.rfind('.'):]
    async with session.get(url, ssl=False) as resp:
        if resp.status == 200:
            data = await resp.read()
            async with aiofile.async_open(f'threadP/images/beauty/{filename2}{filetype}', 'wb') as file:
                await file.write(data)


async def fetch_json():
    async with aiohttp.ClientSession() as session:
        for page in range(3):
            async with session.get(
                url=f'https://image.so.com/zjl?ch=beauty&t1=625&sn={page * 30}',
                ssl=False
            ) as resp:
                if resp.status == 200:
                    json_str = await resp.text()
                    result = json.loads(json_str)
                    for pic_dict in result['list']:
                        await download_picture(session, pic_dict['qhimg_url'], pic_dict['pic_desc'])


def main():
    if not os.path.exists('threadP/images/beauty'):
        os.makedirs('threadP/images/beauty')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_json())
    loop.close()


main()