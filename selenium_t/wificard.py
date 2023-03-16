import selenium_t.utils as utils
from selenium.webdriver.common.by import By


def wificard(driver, S, P, T='WPA', H='false'):
    driver.get('https://wificard.io/')
    ssid_dom = utils.wait_element_by(driver, By.ID, 'ssid')
    ssid_dom.send_keys(S)
    password_dom = utils.wait_element_by(driver, By.ID, 'password')
    password_dom.send_keys(P)
    radios_dom = utils.wait_elements_by(driver, By.XPATH,
                                        '//div[@class="ub-box-szg_border-box" and @role="group"]/descendant::div')
    ckboxs_dom = utils.wait_elements_by(driver, By.XPATH,
                                        '//label[@class="ub-crsr_pointer ub-pst_relative ub-dspl_flex ub-mb_16px '
                                        'ub-mt_16px ub-box-szg_border-box"]/descendant::div')
    if 'true' == H:
        ckboxs_dom[2].click()
    if 'nopass' == T:
        radios_dom[0].click()
    if 'WPA' == T:
        radios_dom[1].click()
    elif 'EAP' == T:
        radios_dom[2].click()
    elif 'WEP' == T:
        radios_dom[3].click()

    print('WIFI:T:%s;S:%s;P:%s;H:%s;' % (T, S, P, H))


if __name__ == '__main__':
    driver = utils.init(detach=True)
    utils.run(driver, wificard, 'wifi-ssid', 'wifi-password', quit=False)