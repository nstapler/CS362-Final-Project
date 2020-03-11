import math
def sqrRt(val):
    testnum = 0;
    try:
        testnum+=val
    except (TypeError):
        return False
    if val < 0:
        return False
    else:
        return math.sqrt(val)


def sin(val):
    testnum = 0
    try:
        testnum+=val
    except (TypeError):
        return False
    return math.sin(val)


def cosin(val):
    testnum = 0
    try:
        testnum += val
    except (TypeError):
        return False
    return math.cos(val)