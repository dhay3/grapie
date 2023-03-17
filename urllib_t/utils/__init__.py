import json
from common import random_ua, random_desktop_ua, random_phone_ua
from typing import Dict
from urllib import (request, parse)

"""
API Reference
https://docs.python.org/3/library/urllib.request.html#module-urllib.request
"""


def do(url: str, method: str = 'GET', params: Dict = None, is_json: bool = False, fake_ua: bool = False):
    data = parse.urlencode(params).encode('utf-8') if params else ''
    if method in ('GET', 'HEAD'):
        url = f'{url}?{data}'
        req = request.Request(url=url)
    else:
        req = request.Request(url=url, data=data)
        if is_json:
            req.add_header('Content-Type', 'application/json')
            req.data = bytes(json.dumps(params).encode('utf-8'))
    if fake_ua:
        req.add_header('User-Agent', random_desktop_ua())
    with request.urlopen(req, timeout=3) as r:
        return r.read().decode('utf-8')


def do_download(url, filename):
    request.urlretrieve(url, filename)
