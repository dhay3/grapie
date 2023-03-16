import selenium_t.utils as utils
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

if __name__ == '__main__':
    usr_data_dir = ''
    driver = utils.init(detach=True)
    driver.get('https://mail.google.com/mail/')
    try:
        utils.wait_element_by(driver, By.CSS_SELECTOR, 'a[data-action="sign in"]').click()
    except TimeoutException:
        pass
    utils.wait_element_by(driver, By.CSS_SELECTOR, 'input[name="identifier"]').send_keys('example@gmail.com')
    utils.wait_element_by(driver, By.ID, 'identifierNext').click()