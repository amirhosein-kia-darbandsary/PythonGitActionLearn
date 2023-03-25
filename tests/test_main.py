import unittest

from source.main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        actual = main()
        expected = 4
        self.assertEqual(actual, expected)

# if __name__ == '__main__':
#     x = TestMain()
#     x.test_main()