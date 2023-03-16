import selenium_t.utils as utils
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
    driver = utils.init(detach=True)
    driver.get('https://baidu.com')
    kw = utils.wait_element_by(driver, By.ID, 'kw')
    kw.send_keys('chatgpt')
    kw.send_keys(Keys.ENTER)
