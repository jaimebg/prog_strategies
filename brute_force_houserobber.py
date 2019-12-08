import iterator
from time import time

v = (3, 10, 3, 1, 2)
sum = 0


def isValid(next):
    i = 0
    for _ in next:
        if i == len(next) - 1:
            return True
        if next[i] == 1 and next[i+1] == 1:
            return False
        i = i + 1
    return True


def sumValues(next):
    res = 0
    i = 0
    for _ in next:
        if next[i] == 1:
            res = res + v[i]
        i = i + 1
    return res


def brute_force_iter():
    sum = 0
    iterator.initComb(len(v))
    while iterator.hasNext():
        next = iterator.nextComb()
        if isValid(next):
            if sumValues(next) > sum:
                sum = sumValues(next)
    return sum


def brute_force_rec(size, v, sum):
    if size < 0:
        return sum

    take = brute_force_rec(size - 2, v, sum + v[size])
    not_take = brute_force_rec(size - 1, v, sum)
    return max(take, not_take)


print("Iterative:", end=" ")
startTime = time()
print(brute_force_iter())
elapsedTime = time() - startTime
print("Execution time:", elapsedTime * 1000, "milliseconds\n")
print("Recursive:", end=" ")
startTime2 = time()
print(brute_force_rec(len(v) - 1, v, sum))
elapsedTime = time() - startTime2
print("Execution time:", elapsedTime * 1000, "milliseconds\n")
