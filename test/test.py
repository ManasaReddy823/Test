import unittest
import add
import time

class test(unittest.TestCase):
    def setUp(self):
        print("Test start: Intelligence-SystemTesting-D0-Mock")

    def test_add(self):
        add.sum(2,3)

    def tearDown(self):
        print("Test end: Intelligence-SystemTesting-D0-Mock")
        time.sleep(1)

if __name__ == "__main__":
        unittest.main()
