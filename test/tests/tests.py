import unittest

from async_request import async_urlopen


class TestAsyncRequest(unittest.TestCase):

    def test_async_urlopen_twoRequests(self):
        responses = async_urlopen(
            ['http://testserver/test1.txt', 'http://testserver/test2.txt'])

        expected_responses = ['test 1', 'test 2']
        for i in range(len(expected_responses)):
            self.assertEquals(responses[i].strip(), expected_responses[i])

    def test_async_urlopen_DEBUGGING(self):
        self.assertEquals(True, False)

if __name__ == '__main__':
    unittest.main()
