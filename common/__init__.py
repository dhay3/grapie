import random

__PHONE_USER_AGENT__ = (
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) '
    'Version/10.0 Mobile/14E304 Safari/602.1 ',
    'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) '
    'Version/3.0 Mobile/1A543 Safari/419.3 ',
    'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254',
    'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, '
    'like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 '
)
__DESKTOP_USER_AGENT__ = (
    'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) '
    'Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 '
    'Safari/537.36 Edge/12.246 '
)


def random_phone_ua():
    return random.choice(__PHONE_USER_AGENT__)


def random_desktop_ua():
    return random.choice(__DESKTOP_USER_AGENT__)


def random_ua():
    return random.choice(__PHONE_USER_AGENT__ + __DESKTOP_USER_AGENT__)
