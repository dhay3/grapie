import selenium_t.utils as utils
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


def ipinfo(driver) -> None:
    driver.get('https://ipinfo.io/')
    list_meta(driver)


def ipinfo_by_ip(driver, ip: str) -> None:
    driver.get('https://ipinfo.io')
    ip_box_dom = utils.wait_element_by(driver, By.CSS_SELECTOR,
                                       'input[class="w-full h-full bg-transparent border-none focus:outline-none '
                                       'heading-h4 text-white"]')
    ip_box_dom.clear()
    ip_box_dom.send_keys(ip)
    ip_box_dom.send_keys(Keys.ENTER)
    list_meta(driver)


def list_meta(driver) -> None:
    tryit_data_li_dom = utils.wait_elements_by(driver, By.XPATH,
                                               '//div[@id="tryit-data"]/ul[@class="my-2.5 space-y-2.5 w-full"]/li')
    rst = []
    for li_dom in tryit_data_li_dom:
        try:
            t_li = utils.wait_element_by(li_dom, By.XPATH, './descendant::span[@class="text-green-05"]').text
            if t_li:
                t_li_field = utils.wait_element_by(li_dom, By.XPATH, './descendant::span[@class="text-white"]').text
                if t_li_field in ('ip:', 'city:', 'region:', 'country:', 'org:'):
                    rst.append(t_li)
        except (NoSuchElementException, TimeoutException):
            pass
    print('ip: {0} city: {1} region: {2} country: {3} org: {4}'.format(*rst))


if __name__ == '__main__':
    driver = utils.init()
    # utils.run_t(10, driver, ipinfo)
    utils.run(driver, ipinfo_by_ip, '8.8.8.8')

    import time

    time.sleep(1000)
