from async_request import async_urlopen
import logging

logging.getLogger('async_request').addHandler(
    logging.StreamHandler())
logging.getLogger('async_request').setLevel(logging.DEBUG)

URLS = (
    'css/main.css',
    'js/ext/pure-min.css',
    'js/ext/opentip.css',
    'js/ext/opentip-native.js',
    'js/ext/mithril.min.js'
)

FULL_URLS = ['http://192.168.1.80:8000/' + x for x in URLS]


def main():
    async_urlopen(FULL_URLS, 4)

if __name__ == '__main__':
    main()
