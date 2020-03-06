import unittest
import UnitTestOnly.nick_calculator as nick_calc


class TestMultiplication(unittest.TestCase):
    def testMultiply(self):
        self.assertNotEqual(None, nick_calc.multiplication())


class TestFactorial(unittest.TestCase):
    def testFactorial(self):
        self.assertNotEqual(None, nick_calc.factorial())


class TestAbsolute(unittest.TestCase):
    def testAbsolute(self):
        self.assertNotEqual(None, nick_calc.absolute())


if __name__ == '__main__':
    unittest.main()
