import re
import urllib_t.utils as utils
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
from bs4 import BeautifulSoup

url = 'http://cip.cc'


def cip_re():
    r = utils.do(url, fake_ua=True)
    for row in r.split('\n'):
        if re.search(r'(\s+<pre>IP)', row):
            print(row.split('>')[1])
        if re.search('^地址|^运营商|^数据二', row):
            print(row)
        if re.search('^数据三', row):
            print(row, '\n')


def cip_xpath():
    r = utils.do(url, fake_ua=True)
    x_dom = etree.HTML(r)
    x_pre = x_dom.xpath('//pre')[0].text
    print(x_pre)


def cip_by_ip(ip):
    r = utils.do(f'{url}/{ip}', fake_ua=True)
    x_dom = etree.HTML(r)
    x_pre = x_dom.xpath('//pre/text()')
    print(x_pre)


def cip_by_bs():
    r = utils.do(url, fake_ua=True)
    dom = BeautifulSoup(r, features='html.parser')
    print(dom.p)


if __name__ == '__main__':
    # with ThreadPoolExecutor(max_workers=10) as ex:
    #     for _ in range(0, 10):
    #         ex.submit(cip_by_ip, '8.8.8.8')
    cip_by_bs()
