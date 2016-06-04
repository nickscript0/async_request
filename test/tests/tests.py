import unittest
import logging

from async_request import async_urlopen

logging.getLogger('async_request').addHandler(
    logging.StreamHandler())
logging.getLogger('async_request').setLevel(logging.DEBUG)


class TestAsyncRequest(unittest.TestCase):

    def test_async_urlopen_returnsValidRequests(self):
        responses = async_urlopen(
            ['http://testserver/test1.txt', 'http://testserver/test2.txt'])

        expected_responses = ['test 1', 'test 2']
        for i in range(len(expected_responses)):
            self.assertEqual(responses[i].strip(), expected_responses[i])

    def test_async_urlopen_returns404(self):
        res = async_urlopen(
            ['http://testserver/test404.txt'])
        self.assertIn("404 Not Found", res[0])

if __name__ == '__main__':
    unittest.main()
