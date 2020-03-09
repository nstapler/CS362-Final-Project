import math
import unittest

import UnitTestAndCode.nick_calculator as nick_calc

import UnitTestAndCode.helperFuncs as helper


class TestMultiplication(unittest.TestCase):
    def testMultiply(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(self.posInt * self.posInt2, nick_calc.multiplication(self.posInt, self.posInt2))
        self.assertEqual(self.posFloat * self.posFloat2, nick_calc.multiplication(self.posFloat, self.posFloat2))
        self.assertEqual(self.fraction * self.posInt, nick_calc.multiplication(self.fraction, self.posInt))
        # negative cases
        self.assertEqual(self.negInt * self.negInt2, nick_calc.multiplication(self.negInt, self.negInt2))
        self.assertEqual(self.negFraction * self.posInt, nick_calc.multiplication(self.negFraction, self.posInt))
        # other
        self.assertEqual(self.zeroCase * self.posInt, nick_calc.multiplication(self.zeroCase, self.posInt))
        self.assertEqual(self.hugeNumber * self.hugeNumber2,
                         nick_calc.multiplication(self.hugeNumber, self.hugeNumber2))
        self.assertEqual(False, nick_calc.multiplication(self.posFloat, self.invalidChar))


class TestFactorial(unittest.TestCase):
    def testFactorial(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(math.factorial(self.posInt), nick_calc.factorial(self.posInt))
        self.assertEqual(math.factorial(self.posFloat), nick_calc.factorial(self.posFloat))
        self.assertEqual(math.factorial(self.fraction), nick_calc.factorial(self.fraction))
        # negative cases
        self.assertEqual(math.factorial(self.negInt), nick_calc.factorial(self.negInt))
        self.assertEqual(math.factorial(self.negfraction), nick_calc.factorial(self.negfraction))
        # other
        self.assertEqual(math.factorial(self.zeroCase), nick_calc.factorial(self.zeroCase))
        self.assertEqual(False, nick_calc.factorial(self.invalidChar))
        self.assertEqual(math.factorial(self.hugeNumber),
                         nick_calc.factorial(self.hugeNumber))


class TestAbsolute(unittest.TestCase):
    def testAbsolute(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(abs(self.posInt), nick_calc.absolute(self.posInt))
        self.assertEqual(abs(self.posFloat), nick_calc.absolute(self.posFloat))
        self.assertEqual(abs(self.fraction), nick_calc.absolute(self.fraction))
        # negative cases
        self.assertEqual(abs(self.negInt), nick_calc.absolute(self.negInt))
        self.assertEqual(abs(self.negfraction), nick_calc.absolute(self.negfraction))
        # other
        self.assertEqual(abs(self.zeroCase), nick_calc.absolute(self.zeroCase))
        self.assertEqual(False, nick_calc.absolute(self.invalidChar))
        self.assertEqual(abs(self.hugeNumber), nick_calc.absolute(self.hugeNumber))


if __name__ == '__main__':
    unittest.main()
