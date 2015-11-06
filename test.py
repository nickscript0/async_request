URLS = (
    'css/main.css',
    'js/ext/pure-min.css',
    'js/ext/opentip.css',
    'js/ext/opentip-native.js',
    'js/ext/mithril.min.js'
)

FULL_URLS = ['http://192.168.1.80:8000/' + x for x in URLS]

from async_request import async_urlopen


def main():
    async_urlopen(FULL_URLS, 4)

if __name__ == '__main__':
    main()
