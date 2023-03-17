import requests
from common import random_desktop_ua
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://movie.douban.com/top250'


def list_top250_bs():
    for idx in range(0, 10):
        r = requests.get(url=url,
                         headers={
                             'User-Agent': random_desktop_ua()
                         },
                         params={
                             'start': 25 * idx
                         })
        if 200 == r.status_code:
            soup = BeautifulSoup(r.text, features='lxml')
            soup_lis = soup.find('ol', class_='grid_view').find_all('li')
            for soup_li in soup_lis:
                soup_info = soup_li.find('div', class_='info')
                soup_info_hd = soup_info.find('div', class_='hd')
                soup_info_bd = soup_info.find('div', class_='bd')
                soup_titles = soup_info_hd.find_all('span', class_='title')
                titles = ''.join([_.string for _ in soup_titles])
                description = [_ for _ in soup_info_bd.find('p').stripped_strings][1]
                rating = soup_info_bd.find('span', class_='rating_num').string
                print(titles, description, rating)


def list_top250_xpath():
    for idx in range(0, 10):
        r = requests.get(url=url,
                         headers={
                             'User-Agent': random_desktop_ua()
                         },
                         params={
                             'start': 25 * idx
                         })
        if 200 == r.status_code:
            x_dom = etree.HTML(r.text)
            x_lis = x_dom.xpath('//div[@id="content"]/descendant::ol/li')
            for x_li in x_lis:
                title = ''.join([_.text for _ in
                                 x_li.xpath('./descendant::div[@class="hd"]/descendant::span[@class="title"]')])
                description = x_li.xpath('./descendant::div[@class="bd"]/p/text()')[1].strip()
                star = x_li.xpath('./descendant::div[@class="star"]/span[@class="rating_num"]/text()')[0]
                print(title, description, star)


if __name__ == '__main__':
    list_top250_xpath()
