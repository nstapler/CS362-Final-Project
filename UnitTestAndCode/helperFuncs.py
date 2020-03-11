import random


def checkIfValid(val):
    if not val:
        return False
    if type(val) == str and (not val.isnumeric()):
        return False
    return True


def prepTestInputs(testSelf):
    random.seed()
    # First set
    testSelf.zeroCase = 0
    testSelf.posInt = random.randint(1, 1000)  # 1-1000
    testSelf.posFloat = (random.random() * random.randint(1, 999)) + 1  # 1-1000
    testSelf.negInt = -1 * random.randint(1, 1000)  # -(1-1000)
    testSelf.negFloat = -1 * (random.random() * random.randint(1, 999)) + 1  # -(1-1000)
    testSelf.invalidChar = chr(random.randint(32, 126))  # ' ' to ~
    testSelf.hugeNumber = random.randint(1000, 10000) * random.randint(1000, 10000) * random.randint(1000, 10000)  #
    # 1mill to 1 bill
    testSelf.fraction = 1 / (testSelf.posInt + 1)  # 1/2 to 1/1001
    testSelf.negFraction = 1 / (testSelf.negFloat + 1)  # -(1/2 to 1/1001)

    # Second Set
    testSelf.posInt2 = random.randint(1, 1000)  # 1-1000
    testSelf.posFloat2 = (random.random() * random.randint(1, 999)) + 1  # 1-1000
    testSelf.negInt2 = -1 * random.randint(1, 1000)  # -(1-1000)
    testSelf.negFloat2 = -1 * (random.random() * random.randint(1, 999)) + 1  # -(1-1000)
    testSelf.invalidChar2 = chr(random.randint(32, 126))  # ' ' to ~
    testSelf.hugeNumber2 = random.randint(1000, 10000) * random.randint(1000, 10000) * random.randint(1000, 10000)
    # 1 billion to 1 trillion
    testSelf.fraction2 = 1 / (testSelf.posInt2 + 1)  # 1/2 to 1/1001
    testSelf.negFraction2 = 1 / (testSelf.negFloat2 + 1)  # -(1/2 to 1/1001)
