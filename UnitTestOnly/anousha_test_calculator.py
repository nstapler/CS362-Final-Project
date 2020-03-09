import math
import unittest

import UnitTestOnly.anousha_calculator as anousha_calc

import UnitTestOnly.helperFuncs as helper


class TestDivision(unittest.TestCase):
    def test_division(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(self.posInt / self.posInt2, anousha_calc.division(self.posInt, self.posInt2))
        self.assertEqual(self.posFloat / self.posFloat2, anousha_calc.division(self.posFloat, self.posFloat2))
        self.assertEqual(self.fraction / self.posInt, anousha_calc.division(self.fraction, self.posInt))
        # negative cases
        self.assertEqual(self.negInt / self.negInt2, anousha_calc.division(self.negInt, self.negInt2))
        self.assertEqual(self.negfraction / self.posInt, anousha_calc.division(self.negfraction, self.posInt))
        # other
        self.assertEqual(self.zeroCase / self.posInt, anousha_calc.division(self.zeroCase, self.posInt))
        self.assertEqual(self.hugeNumber / self.hugeNumber2,
                         anousha_calc.division(self.hugeNumber, self.hugeNumber2))
        self.assertEqual(False, anousha_calc.division(self.posFloat, self.invalidChar))


class TestSquareRoot(unittest.TestCase):
    def test_sqrt(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(math.sqrt(self.posInt), anousha_calc.sqrt(self.posInt))
        self.assertEqual(math.sqrt(self.posFloat), anousha_calc.sqrt(self.posFloat))
        self.assertEqual(math.sqrt(self.fraction), anousha_calc.sqrt(self.fraction))
        # negative cases
        self.assertEqual(math.sqrt(self.negInt), anousha_calc.sqrt(self.negInt))
        self.assertEqual(math.sqrt(self.negfraction), anousha_calc.sqrt(self.negfraction))
        # other
        self.assertEqual(math.sqrt(self.zeroCase), anousha_calc.sqrt(self.zeroCase))
        self.assertEqual(False, anousha_calc.sqrt(self.invalidChar))
        self.assertEqual(math.sqrt(self.hugeNumber),
                         anousha_calc.sqrt(self.hugeNumber))


class TestFraction(unittest.TestCase):
    def test_fraction(self):
        helper.prepTestInputs(self)
        # positive case
        self.assertEqual(1/(self.posInt), anousha_calc.fraction(self.posInt))
        self.assertEqual(1/(self.posFloat), anousha_calc.fraction(self.posFloat))
        self.assertEqual(1/(self.fraction), anousha_calc.fraction(self.fraction))
        # negative cases
        self.assertEqual(1/(self.negInt), anousha_calc.fraction(self.negInt))
        self.assertEqual(1/(self.negfraction), anousha_calc.fraction(self.negfraction))
        # other
        self.assertEqual(1/(self.zeroCase), anousha_calc.fraction(self.zeroCase))
        self.assertEqual(False, anousha_calc.fraction(self.invalidChar))
        self.assertEqual(1/(self.hugeNumber), anousha_calc.fraction(self.hugeNumber))


if __name__ == '__main__':
    unittest.main()
