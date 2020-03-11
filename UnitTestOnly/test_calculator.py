import math
import unittest

import UnitTestOnly.calculator as calc

import UnitTestOnly.helperFuncs as helper


class TestMultiplication(unittest.TestCase):
    def testMultiply(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(self.posInt * self.posInt2, calc.multiplication(self.posInt, self.posInt2))
        self.assertEqual(self.posFloat * self.posFloat2, calc.multiplication(self.posFloat, self.posFloat2))
        self.assertEqual(self.fraction * self.posInt, calc.multiplication(self.fraction, self.posInt))
        # negative cases
        self.assertEqual(self.negInt * self.negInt2, calc.multiplication(self.negInt, self.negInt2))
        self.assertEqual(self.negfraction * self.posInt, calc.multiplication(self.negfraction, self.posInt))
        # other
        self.assertEqual(self.zeroCase * self.posInt, calc.multiplication(self.zeroCase, self.posInt))
        self.assertEqual(self.hugeNumber * self.hugeNumber2,
                         calc.multiplication(self.hugeNumber, self.hugeNumber2))
        self.assertEqual(False, calc.multiplication(self.posFloat, self.invalidChar))


class TestFactorial(unittest.TestCase):
    def testFactorial(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(math.factorial(self.posInt), calc.factorial(self.posInt))
        self.assertEqual(math.factorial(self.posFloat), calc.factorial(self.posFloat))
        self.assertEqual(math.factorial(self.fraction), calc.factorial(self.fraction))
        # negative cases
        self.assertEqual(math.factorial(self.negInt), calc.factorial(self.negInt))
        self.assertEqual(math.factorial(self.negfraction), calc.factorial(self.negfraction))
        # other
        self.assertEqual(math.factorial(self.zeroCase), calc.factorial(self.zeroCase))
        self.assertEqual(False, calc.factorial(self.invalidChar))
        self.assertEqual(math.factorial(self.hugeNumber),
                         calc.factorial(self.hugeNumber))


class TestAbsolute(unittest.TestCase):
    def testAbsolute(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(abs(self.posInt), calc.absolute(self.posInt))
        self.assertEqual(abs(self.posFloat), calc.absolute(self.posFloat))
        self.assertEqual(abs(self.fraction), calc.absolute(self.fraction))
        # negative cases
        self.assertEqual(abs(self.negInt), calc.absolute(self.negInt))
        self.assertEqual(abs(self.negfraction), calc.absolute(self.negfraction))
        # other
        self.assertEqual(abs(self.zeroCase), calc.absolute(self.zeroCase))
        self.assertEqual(False, calc.absolute(self.invalidChar))
        self.assertEqual(abs(self.hugeNumber), calc.absolute(self.hugeNumber))


class MyTestCase(unittest.TestCase):
    def test_sqrRt(self):
        helper.prepTestInputs(self)
        # pos input
        self.assertEqual(math.sqrt(self.posInt), calc.sqrRt(self.posInt))
        self.assertEqual(math.sqrt(self.posInt2), calc.sqrRt(self.posInt2))
        self.assertEqual(math.sqrt(self.posFloat), calc.sqrRt(self.posFloat))
        self.assertEqual(math.sqrt(self.posFloat2), calc.sqrRt(self.posFloat2))
        self.assertEqual(self.posInt, round(calc.sqrRt(self.posInt) * calc.sqrRt(self.posInt), 0))
        self.assertEqual(self.posInt2, round(calc.sqrRt(self.posInt2) * calc.sqrRt(self.posInt2), 0))

        # neg input
        self.assertEqual(False, calc.sqrRt(self.negInt))
        self.assertEqual(False, calc.sqrRt(self.negInt2))
        self.assertEqual(False, calc.sqrRt(self.negFloat))
        self.assertEqual(False, calc.sqrRt(self.negFloat2))
        # frac input
        self.assertEqual(math.sqrt(self.fraction), calc.sqrRt(self.fraction))

        self.assertEqual(False, calc.sqrRt(self.negFraction))
        self.assertEqual(math.sqrt(self.fraction2), calc.sqrRt(self.fraction2))

        self.assertEqual(False, calc.sqrRt(self.negFraction2))
        # bad input
        self.assertEqual(False, calc.sqrRt('a'))
        self.assertEqual(False, calc.sqrRt(' '))

    def test_sin(self):
        helper.prepTestInputs(self)
        # pos input
        self.assertEqual(math.sin(self.posInt), calc.sin(self.posInt))
        self.assertEqual(math.sin(self.posInt2), calc.sin(self.posInt2))
        self.assertEqual(math.sin(self.posFloat), calc.sin(self.posFloat))
        self.assertEqual(math.sin(self.posFloat2), calc.sin(self.posFloat2))
        # neg input
        self.assertEqual(math.sin(self.negInt), calc.sin(self.negInt))
        self.assertEqual(math.sin(self.negInt2), calc.sin(self.negInt2))
        self.assertEqual(math.sin(self.negFloat), calc.sin(self.negFloat))
        self.assertEqual(math.sin(self.negFloat2), calc.sin(self.negFloat2))
        # frac input
        self.assertEqual(math.sin(self.fraction), calc.sin(self.fraction))
        self.assertEqual(math.sin(self.negFraction), calc.sin(self.negFraction))
        self.assertEqual(math.sin(self.fraction2), calc.sin(self.fraction2))
        self.assertEqual(math.sin(self.negFraction2), calc.sin(self.negFraction2))
        # bad input
        self.assertEqual(False, calc.sin('a'))
        self.assertEqual(False, calc.sin(' '))

    def test_cos(self):
        helper.prepTestInputs(self)
        # pos input
        self.assertEqual(math.cos(self.posInt), calc.cosin(self.posInt))
        self.assertEqual(math.cos(self.posInt2), calc.cosin(self.posInt2))
        self.assertEqual(math.cos(self.posFloat), calc.cosin(self.posFloat))
        self.assertEqual(math.cos(self.posFloat2), calc.cosin(self.posFloat2))
        # neg input
        self.assertEqual(math.cos(self.negInt), calc.cosin(self.negInt))
        self.assertEqual(math.cos(self.negInt2), calc.cosin(self.negInt2))
        self.assertEqual(math.cos(self.negFloat), calc.cosin(self.negFloat))
        self.assertEqual(math.cos(self.negFloat2), calc.cosin(self.negFloat2))
        # frac input
        self.assertEqual(math.cos(self.fraction), calc.cosin(self.fraction))
        self.assertEqual(math.cos(self.negFraction), calc.cosin(self.negFraction))
        self.assertEqual(math.cos(self.fraction2), calc.cosin(self.fraction2))
        self.assertEqual(math.cos(self.negFraction2), calc.cosin(self.negFraction2))
        # bad input
        self.assertEqual(False, calc.cosin('a'))
        self.assertEqual(False, calc.cosin(' '))


class TestDivision(unittest.TestCase):
    def test_division(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(self.posInt / self.posInt2, calc.division(self.posInt, self.posInt2))
        self.assertEqual(self.posFloat / self.posFloat2, calc.division(self.posFloat, self.posFloat2))
        self.assertEqual(self.fraction / self.posInt, calc.division(self.fraction, self.posInt))
        # negative cases
        self.assertEqual(self.negInt / self.negInt2, calc.division(self.negInt, self.negInt2))
        self.assertEqual(self.negfraction / self.posInt, calc.division(self.negfraction, self.posInt))
        # other
        self.assertEqual(self.zeroCase / self.posInt, calc.division(self.zeroCase, self.posInt))
        self.assertEqual(self.hugeNumber / self.hugeNumber2,
                         calc.division(self.hugeNumber, self.hugeNumber2))
        self.assertEqual(False, calc.division(self.posFloat, self.invalidChar))


class TestSquare(unittest.TestCase):
    def test_square(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(math.sqrt(self.posInt), calc.square(self.posInt))
        self.assertEqual(math.sqrt(self.posFloat), calc.square(self.posFloat))
        self.assertEqual(math.sqrt(self.fraction), calc.square(self.fraction))
        # negative cases
        self.assertEqual(math.sqrt(self.negInt), calc.square(self.negInt))
        self.assertEqual(math.sqrt(self.negfraction), calc.square(self.negfraction))
        # other
        self.assertEqual(math.sqrt(self.zeroCase), calc.square(self.zeroCase))
        self.assertEqual(False, calc.square(self.invalidChar))
        self.assertEqual(math.sqrt(self.hugeNumber),
                         calc.square(self.hugeNumber))


class TestFraction(unittest.TestCase):
    def test_fraction(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(1 / (self.posInt), calc.fraction(self.posInt))
        self.assertEqual(1 / (self.posFloat), calc.fraction(self.posFloat))
        self.assertEqual(1 / (self.fraction), calc.fraction(self.fraction))
        # negative cases
        self.assertEqual(1 / (self.negInt), calc.fraction(self.negInt))
        self.assertEqual(1 / (self.negfraction), calc.fraction(self.negfraction))
        # other
        self.assertEqual(1 / (self.zeroCase), calc.fraction(self.zeroCase))
        self.assertEqual(False, calc.fraction(self.invalidChar))
        self.assertEqual(1 / (self.hugeNumber), calc.fraction(self.hugeNumber))


if __name__ == '__main__':
    unittest.main()
