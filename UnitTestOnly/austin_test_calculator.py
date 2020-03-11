import math
import unittest

import austin_calculator as austin_calc

import helperFuncs as helper




class MyTestCase(unittest.TestCase):
    def test_sqrRt(self):
        helper.prepTestInputs(self)
        #pos input
        self.assertEqual(math.sqrt(self.posInt), austin_calc.sqrRt(self.posInt))
        self.assertEqual(math.sqrt(self.posInt2), austin_calc.sqrRt(self.posInt2))
        self.assertEqual(math.sqrt(self.posFloat), austin_calc.sqrRt(self.posFloat))
        self.assertEqual(math.sqrt(self.posFloat2), austin_calc.sqrRt(self.posFloat2))
        self.assertEqual(self.posInt, round(austin_calc.sqrRt(self.posInt)*austin_calc.sqrRt(self.posInt),0))
        self.assertEqual(self.posInt2, round(austin_calc.sqrRt(self.posInt2) * austin_calc.sqrRt(self.posInt2),0))

        #neg input
        self.assertEqual(False, austin_calc.sqrRt(self.negInt))
        self.assertEqual(False, austin_calc.sqrRt(self.negInt2))
        self.assertEqual(False, austin_calc.sqrRt(self.negFloat))
        self.assertEqual(False, austin_calc.sqrRt(self.negFloat2))
        #frac input
        self.assertEqual(math.sqrt(self.fraction), austin_calc.sqrRt(self.fraction))

        self.assertEqual(False, austin_calc.sqrRt(self.negFraction))
        self.assertEqual(math.sqrt(self.fraction2), austin_calc.sqrRt(self.fraction2))

        self.assertEqual(False, austin_calc.sqrRt(self.negFraction2))
        #bad input
        self.assertEqual(False, austin_calc.sqrRt('a'))
        self.assertEqual(False, austin_calc.sqrRt(' '))

    def test_sin(self):
        helper.prepTestInputs(self)
        # pos input
        self.assertEqual(math.sin(self.posInt), austin_calc.sin(self.posInt))
        self.assertEqual(math.sin(self.posInt2), austin_calc.sin(self.posInt2))
        self.assertEqual(math.sin(self.posFloat), austin_calc.sin(self.posFloat))
        self.assertEqual(math.sin(self.posFloat2), austin_calc.sin(self.posFloat2))
        # neg input
        self.assertEqual(math.sin(self.negInt), austin_calc.sin(self.negInt))
        self.assertEqual(math.sin(self.negInt2), austin_calc.sin(self.negInt2))
        self.assertEqual(math.sin(self.negFloat), austin_calc.sin(self.negFloat))
        self.assertEqual(math.sin(self.negFloat2), austin_calc.sin(self.negFloat2))
        # frac input
        self.assertEqual(math.sin(self.fraction), austin_calc.sin(self.fraction))
        self.assertEqual(math.sin(self.negFraction), austin_calc.sin(self.negFraction))
        self.assertEqual(math.sin(self.fraction2), austin_calc.sin(self.fraction2))
        self.assertEqual(math.sin(self.negFraction2), austin_calc.sin(self.negFraction2))
        # bad input
        self.assertEqual(False, austin_calc.sin('a'))
        self.assertEqual(False, austin_calc.sin(' '))

    def test_cos(self):
        helper.prepTestInputs(self)
        # pos input
        self.assertEqual(math.cos(self.posInt), austin_calc.cosin(self.posInt))
        self.assertEqual(math.cos(self.posInt2), austin_calc.cosin(self.posInt2))
        self.assertEqual(math.cos(self.posFloat), austin_calc.cosin(self.posFloat))
        self.assertEqual(math.cos(self.posFloat2), austin_calc.cosin(self.posFloat2))
        # neg input
        self.assertEqual(math.cos(self.negInt), austin_calc.cosin(self.negInt))
        self.assertEqual(math.cos(self.negInt2), austin_calc.cosin(self.negInt2))
        self.assertEqual(math.cos(self.negFloat), austin_calc.cosin(self.negFloat))
        self.assertEqual(math.cos(self.negFloat2), austin_calc.cosin(self.negFloat2))
        # frac input
        self.assertEqual(math.cos(self.fraction), austin_calc.cosin(self.fraction))
        self.assertEqual(math.cos(self.negFraction), austin_calc.cosin(self.negFraction))
        self.assertEqual(math.cos(self.fraction2), austin_calc.cosin(self.fraction2))
        self.assertEqual(math.cos(self.negFraction2), austin_calc.cosin(self.negFraction2))
        # bad input
        self.assertEqual(False, austin_calc.cosin('a'))
        self.assertEqual(False, austin_calc.cosin(' '))



if __name__ == '__main__':
    unittest.main()

