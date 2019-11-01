import unittest


class NumbersTest(unittest.TestCase):

    def test_equal1(self):
        self.assertEqual(1 + 1, 2)

    def test_equal2(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()
