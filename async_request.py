"""
A python 3.5 library that makes requests in parallel using async await.
"""

import asyncio
import math
from itertools import islice

import aiohttp


def async_urlopen(urls, in_parallel=5):
    """
    Given a list of url strings return a list of responses
    - urls: a list of urls to request
    - in_parallel: an integer of the number of requests to send in parallel
      at a time
    """
    return AsyncRequest(urls, in_parallel).run()


class AsyncRequest:

    """
    Simple wrapper for aiohttp.get to request a set of urls in parallel
    """

    def __init__(self, urls, in_parallel):
        self.responses = []
        self.urls_iter = iter(urls)
        self.num_urls = len(urls)
        self.in_parallel = in_parallel

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run_async())
        return self.responses

    async def run_async(self):
        group_size = max(math.ceil(self.num_urls / self.in_parallel), 1)
        for i in range(group_size):
            await asyncio.wait([self.async_request(url)
                                for url in islice(self.urls_iter, self.in_parallel)])

    async def async_request(self, url):
        res = await aiohttp.get(url)
        self.responses.append(await res.text())