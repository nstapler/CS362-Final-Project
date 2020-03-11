import math

import UnitTestAndCode.helperFuncs as helper


def sqrRt(val):
    if not helper.checkIfValid(val):
        return False
    testnum = 0;
    try:
        testnum += val
    except (TypeError):
        return False
    if val < 0:
        return False
    else:
        return math.sqrt(val)


def sin(val):
    if not helper.checkIfValid(val):
        return False
    testnum = 0
    try:
        testnum += val
    except (TypeError):
        return False
    return math.sin(val)


def cosin(val):
    if not helper.checkIfValid(val):
        return False
    testnum = 0
    try:
        testnum += val
    except (TypeError):
        return False
    return math.cos(val)


def division(val1, val2):
    if (not helper.checkIfValid(val1)) or (not helper.checkIfValid(val2)):
        return False
    return val1 / val2


def square(val):
    if not helper.checkIfValid(val):
        return False
    return val * val


def fraction(val):
    if not helper.checkIfValid(val):
        return False
    if val == 0:
        print("Cannot divide by zero")
        return False;
    return 1 / val


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
