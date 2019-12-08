import iterator
from time import time


def is_valid(next):
    for i in range(len(next)):
        if i == len(next) - 1:
            return True
        if next[i] == 1 and next[i+1] == 1:
            return False
    return True


def sum_values(next):
    res = 0
    for i in range(len(next)):
        if next[i] == 1:
            res = res + v[i]
    return res


def brute_force_iter():
    sum = 0
    iterator.initComb(len(v))
    while iterator.hasNext():
        next = iterator.nextComb()
        if is_valid(next):
            if sum_values(next) > sum:
                sum = sum_values(next)
    return sum


value = 0


def brute_force_rec(size, v, value):
    if size < 0:
        return value

    take = brute_force_rec(size - 2, v, value + v[size])
    not_take = brute_force_rec(size - 1, v, value)
    return max(take, not_take)


v = (3, 10, 3, 1, 2)
print("Iterative (Using combinations iterator):", end=" ")
startTime = time()
print(brute_force_iter())
elapsedTime = time() - startTime
print("Execution time:", elapsedTime * 1000, "milliseconds\n")
print("Recursive (With calculated recurrence):", end=" ")
startTime2 = time()
print(brute_force_rec(len(v) - 1, v, value))
elapsedTime = time() - startTime2
print("Execution time:", elapsedTime * 1000, "milliseconds\n")
