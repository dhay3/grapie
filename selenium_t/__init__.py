#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author：cc
@Date：3/27/25 16:18
@Description: 
"""
import time
import requests
from requests import Session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

START_MAXIMIZED = '--start-maximized'
IGNORE_CERTIFICATE_ERRORS = '--ignore-certificate-errors'
DISABLE_POPUP_BLOCKING = '--disable-popup-blocking'
INCOGNITO = '--incognito'
DISABLE_DEFAULT_APPS = '--disable-default-apps'
HEADLESS = '--headless'
DISABLE_GPU = '--disable-gpu'
USER_DATA_DIR = 'user-data-dir='


def init_webdriver(*args) -> WebDriver | None:
    options = webdriver.ChromeOptions()
    for _ in args: options.add_argument(_)
    try:
        return webdriver.Chrome(options=options, service=ChromeService())
    except Exception:
        webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


def wait_element_by(driver, by: str, path: str, timeout: int = 3) -> WebElement | None:
    if by in (By.ID, By.XPATH, By.NAME, By.TAG_NAME, By.CLASS_NAME, By.TAG_NAME, By.CSS_SELECTOR, By.LINK_TEXT,
              By.PARTIAL_LINK_TEXT):
        return WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(by, path))


def login_tower(username: str, password: str) -> Session:
    se = requests.Session()
    driver = init_webdriver(DISABLE_GPU, HEADLESS)
    driver.get('https://tower.icloud.cn/back')
    wait_element_by(driver, By.ID, 'showUsername').send_keys(username)
    wait_element_by(driver, By.ID, 'showPassword').send_keys(password)
    wait_element_by(driver, By.ID, 'accountSubmit').click()
    wait_element_by(driver, By.XPATH,
                    '//main/descendant::div[contains(@class, "ant-page-header")]/descendant::div[@class="ant-select-selector"]',
                    10)
    cookies = driver.get_cookies()
    driver.quit()
    for co in cookies: requests.utils.add_dict_to_cookiejar(se.cookies, {co['name']: co['value']})
    return se


s = login_tower('hz.cheng', '!Chz19970218')

r = s.post(url=f'https://tower.icloud.cn/gateway/tower/manage/api/overview/calcStatistics?t={time.time()}',
           json={
               'regionId': 55
           })

print(r.json())
