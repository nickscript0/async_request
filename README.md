# async_request
A python 3.5 library that makes concurrent requests using async await (PEP 492).

This library is intended to be called by synchronous code (it's a synchronous wrapper of [aiohttp](https://github.com/KeepSafe/aiohttp).get), the public methods do not return until all requests are complete. 

## Purpose
1. A simple way of speeding up the retrieval of a set of web requests (that are network I/O bound) using concurrency 
1. Abstract the concurrent part away from the calling code so that a synchronous codebase can call this (without worrying about asynchronous things like asyncio.BaseEventLoop and 'async await')
1. An exercise in using Python 3.5's new async await syntax

## Usage
### Minimal example
```python
from async_request import async_urlopen
async_urlopen(['https://github.com', 'https://gist.github.com'])
```

### Logging the requests example
```python
from async_request import async_urlopen
import logging

logging.getLogger('async_request').addHandler(
    logging.StreamHandler())
logging.getLogger('async_request').setLevel(logging.DEBUG)

responses = async_urlopen(['https://github.com', 'https://gist.github.com'])

print(responses)
```

## TODO
1. Add automated e2e tests
