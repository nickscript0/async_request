"""
A python 3.5 library that makes concurrent requests using async await (PEP 492).

This library is intended to be called by synchronous code (it's a synchronous wrapper of aiohttp.get),
the public methods do not return until all requests are complete.
"""

import asyncio
import math
from itertools import islice
from collections import OrderedDict
import logging
from logging import NullHandler


import aiohttp

logging.getLogger(__name__).addHandler(NullHandler())
logger = logging.getLogger(__name__)


def async_urlopen(urls, in_parallel=5):
    """
    Given a list of url strings return a list of responses
    - urls: a list of urls to request
    - in_parallel: an integer of the number of requests to make concurrently
      at a time
    """
    return AsyncRequest(urls, in_parallel).run()


class AsyncRequest:

    """
    Simple wrapper for aiohttp.get to request a set of urls concurrently
    """

    def __init__(self, urls, in_parallel):
        self.request_responses = OrderedDict([(k, None) for k in urls])
        self.urls_iter = iter(urls)
        self.num_urls = len(urls)
        self.in_parallel = in_parallel

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._runAsync())
        return self.request_responses.values()

    async def _runAsync(self):
        num_groups = max(math.ceil(self.num_urls / self.in_parallel), 1)
        for i in range(num_groups):
            await asyncio.wait([self._asyncRequest(url, i)
                                for url in islice(self.urls_iter, self.in_parallel)])

    async def _asyncRequest(self, url, group_id):
        res = await aiohttp.get(url)
        text = await res.text()
        logger.debug('Retrieved (Group {}): {} ({:.2f} KB)'.format(
            group_id, url, len(text) / 1000))
        self.request_responses[url] = text
