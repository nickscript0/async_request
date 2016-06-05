#!/bin/sh
pip install nose
pip install git+https://github.com/nickscript0/async_request.git
nosetests --with-xunit
