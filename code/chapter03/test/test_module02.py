import unittest
import inspect

class TestClass01(unittest.TestCase):

    def test_case02(self):
        print(f"\nRunning Test Method: {inspect.stack()[0][3]}")

    def test_case01(self):
        print(f"\nRunning Test Method: {inspect.stack()[0][3]}")

if __name__ == '__main__':
    unittest.main(verbosity=2)

