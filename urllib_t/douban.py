import urllib_t.utils as utils
from lxml import etree
from bs4 import BeautifulSoup

"""
About tbody
https://stackoverflow.com/questions/20522820/how-to-get-tbody-from-table-from-python-beautiful-soup
"""


def top250_piece():
    url = 'http://movie.douban.com/top250'
    r = utils.do(url, fake_ua=True)
    x_dom = etree.HTML(r)
    x_content = x_dom.xpath('//div[@id="content"]')
    title = x_content[0].xpath('./h1/text()')
    print(title)
    x_lis = x_content[0] \
        .xpath('./descendant::ol[@class="grid_view"]')[0] \
        .xpath('./li')
    for x_li in x_lis:
        x_info = x_li.xpath('./div/div[@class="info"]')[0]
        x_hd = x_info.xpath('./div[@class="hd"]')[0]
        x_bd = x_info.xpath('./div[@class="bd"]')[0]
        title = x_hd.xpath('./a/span')[0].text
        title_en = x_hd.xpath('./a/span')[1].text
        time = x_bd.xpath('./p/text()')[1].strip()
        rating = x_bd.xpath('./div[@class="star"]/span[@class="rating_num"]/text()')
        print(title, title_en, time, rating)


def new_board():
    """
    豆瓣电影新片榜
    :return:
    """
    url = 'https://movie.douban.com/chart'
    r = utils.do(url, fake_ua=True)
    soup = BeautifulSoup(r, features='lxml')
    soup_content = soup.find('div', class_='article')
    board_title = soup_content.h2.string
    print(board_title)
    tables = soup_content.find_all('table', {'class': ''})
    for table in tables:
        soup_tr = table.find('tr')
        soup_td = soup_tr.find_all('td')
        title = soup_td[0].a['title']
        release_date = soup_td[1].div.p.string.split('/')[0]
        star = soup_tr.find('div', {'class': 'star clearfix'}).find('span', class_='rating_nums').string
        print(title, release_date, star)


if __name__ == '__main__':
    pass
