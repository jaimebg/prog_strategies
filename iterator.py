combination = []


def initComb(size):
    global combination
    combination = [None] * size


def hasNext():
    for i in range(len(combination)):
        if combination[i] == 1:
            continue
        else:
            return True
    return False


def nextComb():
    for i in reversed(range(len(combination))):
        if combination[i] == 0:
            combination[i] = 1
            return combination
        else:
            combination[i] = 0
            continue
    return combination


