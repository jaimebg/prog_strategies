# Given an array return max sum of not adjacent values.
# v = 3 10 3 1 2; res = 12
from time import time


def rob_top_down(v, i):
    if i < 0:
        return 0

    rob_this_house = v[i] + rob_top_down(v, i - 2)
    dont_rob_this_house = rob_top_down(v, i - 1)
    return max(rob_this_house, dont_rob_this_house)


def rob_bottom_up(v):
    res = [v[0], max(v[0], v[1])]

    for i in range(2, len(v)):
        rob_this_house = v[i] + res[i - 2]
        dont_rob_this_house = res[i - 1]
        res.append(max(rob_this_house, dont_rob_this_house))
    return res[-1]


a = [3, 10, 3, 1, 2]
print("Memoization (Top-Down):", end=" ")
startTime = time()
print(rob_top_down(a, len(a) - 1))
elapsedTime = time() - startTime
print("Execution time:", elapsedTime * 1000, "milliseconds\n")
print("Tabulation (Bottom-Up):", end=" ")
startTime = time()
print(rob_bottom_up(a))
elapsedTime = time() - startTime
print("Execution time:", elapsedTime * 1000, "milliseconds\n")


