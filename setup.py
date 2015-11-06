from setuptools import setup

setup(name='async_request',
      version='0.1',
      install_requires=[
          "asyncio",
      ],
      description='A python 3.5 library that makes requests in parallel using async await',
      url='https://github.com/nickscript0/async_request',
      author='nickscript0',
      author_email='nickscript0@users.noreply.github.com',
      license='MIT',
      packages=['async_request'],
      zip_safe=False)
