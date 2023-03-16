from common import random_phone_ua, random_desktop_ua
from typing import Callable, List
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService, DEFAULT_EXECUTABLE_PATH
from webdriver_manager.chrome import ChromeDriverManager

"""
Options can be check here 
https://peter.sh/experiments/chromium-command-line-switches/
"""
# maximize window size
START_MAXIMIZED = '--start-maximized'
# skip TLS errors
IGNORE_CERTIFICATE_ERRORS = '--ignore-certificate-errors'
DISABLE_POPUP_BLOCKING = '--disable-popup-blocking'
# incognito mode
INCOGNITO = '--incognito'
DISABLE_DEFAULT_APPS = '--disable-default-apps'
HEADLESS = '--headless'
DISABLE_GPU = '--disable-gpu'
USER_DATA_DIR = 'user-data-dir='


def init(*args, executable_path: str = DEFAULT_EXECUTABLE_PATH,
         headless: bool = False, usr_dir: str = None, detach: bool = False, is_phone: bool = False) -> WebDriver:
    """
    # Remote Webdriver implementation
    Since Selenium >= 4.6 there is no need to download webdriver and configure the executable_path.
    Otherwise, you should download webdriver and set executable_path to the path of webdriver, or use drivermanager.
    Driver can be download from here:
    https://chromedriver.storage.googleapis.com/index.html
    :param is_phone: Use phone User-Agent or not
    :param detach: Close browser or not when task over
    :param args: Chrome webdriver options
    :param executable_path: Chrome webdriver executable path
    :param headless: Start Chrome headless or not
    :param usr_dir: User profile path for cookies, check chrome://version to get default path
    :return: webdriver
    """
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    if is_phone:
        options.add_argument(f'user-agent={random_phone_ua()}')
    else:
        options.add_argument(f'user-agent={random_desktop_ua()}')
    if detach:
        options.add_experimental_option('detach', True)
    if headless:
        options.add_argument(HEADLESS)
        options.add_argument(DISABLE_GPU)
    if usr_dir:
        options.add_argument(f'{USER_DATA_DIR}{usr_dir}')
    for _ in args:
        if _ in [HEADLESS, DISABLE_GPU]:
            continue
        options.add_argument(_)
    try:
        return webdriver.Chrome(service=ChromeService(executable_path=DEFAULT_EXECUTABLE_PATH), options=options)
    except Exception:
        return webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)


def wait_elements_by(driver, by: str, path: str, timeout: int = 3) -> List[WebElement]:
    if by in (By.ID, By.XPATH, By.NAME, By.TAG_NAME, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR, By.LINK_TEXT,
              By.PARTIAL_LINK_TEXT):
        """
        EC.presence_of_all_elements_located((by, path)) == lambda d: d.find_element(by, path)
        """
        return WebDriverWait(driver, timeout) \
            .until(EC.presence_of_all_elements_located((by, path)))


def wait_element_by(driver, by: str, path: str, timeout: int = 3) -> WebElement:
    if by in (By.ID, By.XPATH, By.NAME, By.TAG_NAME, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR, By.LINK_TEXT,
              By.PARTIAL_LINK_TEXT):
        return WebDriverWait(driver, timeout=timeout) \
            .until(lambda d: d.find_element(by, path))


def run_t(times: int, driver, func: Callable, *args, quit=True) -> None:
    func(driver, *args)
    with ThreadPoolExecutor(max_workers=times) as executor:
        for _ in range(0, times):
            executor.submit(func, driver, *args)
    if quit:
        driver.quit()


def run(driver, func: Callable, *args, quit=True) -> None:
    func(driver, *args)
    if quit:
        driver.quit()
