import urllib_t.utils as utils
from lxml import etree

if __name__ == '__main__':
    url = 'https://movie.douban.com/chart'
    r = utils.do(url, fake_ua=True)
    x_dom = etree.HTML(r)
    x_article = x_dom.xpath('//div[@class="article"]')[0]
    print(x_article.xpath('./h2')[0].text)
