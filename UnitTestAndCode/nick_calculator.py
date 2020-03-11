import UnitTestAndCode.helperFuncs as helper
import math


def multiplication(val, val2):
    if (not helper.checkIfValid(val)) or (not helper.checkIfValid(val2)):
        return False
    return val * val2


def factorial(val):
    if not helper.checkIfValid(val):
        return False
    if val < 0:
        return 0
    if type(val) == float or val >= 2147483647:
        print("Must input a valid positive integer that is less than 2147483647 to the factorial function.")
        return False
    return math.factorial(val)


def absolute(val):
    if not helper.checkIfValid(val):
        return False
    return math.fabs(val)
