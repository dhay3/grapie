import re
import urllib_t.utils as utils
from concurrent.futures import ThreadPoolExecutor


def cip():
    r = utils.do('http://cip.cc', fake_ua=True)
    for row in r.split('\n'):
        if re.search(r'(\s+<pre>IP)', row):
            print(row.split('>')[1])
        if re.search('^地址|^运营商|^数据二|^数据三', row):
            print(row)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as ex:
        for _ in range(0, 10):
            ex.submit(cip)
