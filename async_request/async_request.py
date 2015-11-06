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

    - Issues: this class using @asyncio.coroutine instead of the newer async await syntax
      due to the following error occuring with the newer syntax:
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/src/async_request/async_request.py", line 19, in async_urlopen
            return AsyncRequest(urls, in_parallel).run()
          File "/src/async_request/async_request.py", line 36, in run
            loop.run_until_complete(self.run_async())
          File "/usr/local/lib/python3.5/site-packages/asyncio-3.4.3-py3.5.egg/asyncio/base_events.py", line 296, in run_until_complete
            future = tasks.async(future, loop=self)
          File "/usr/local/lib/python3.5/site-packages/asyncio-3.4.3-py3.5.egg/asyncio/tasks.py", line 516, in async
            raise TypeError('A Future or coroutine is required')
        TypeError: A Future or coroutine is required
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

    @asyncio.coroutine
    def run_async(self):  # async
        num_groups = max(math.ceil(self.num_urls / self.in_parallel), 1)
        for i in range(num_groups):
            # await
            yield from asyncio.wait([self.async_request(url)
                                     for url in islice(self.urls_iter, self.in_parallel)])

    @asyncio.coroutine
    def async_request(self, url):  # async
        res = yield from aiohttp.get(url)  # await
        text = yield from res.text()  # await
        self.responses.append(text)  # await
