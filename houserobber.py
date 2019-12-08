# Given an array return max sum of not adjacent values.
# v = 3 10 3 1 2; res = 12


def rob_top_down(v, i):
    if len(v) == 1:
        return v[i]
    if i < 0 or i > len(v):
        return 0

    rob_this_house = v[i] + rob_top_down(v, i - 2)
    dont_rob_this_house = rob_top_down(v, i - 1)

    return max(rob_this_house, dont_rob_this_house)

i = 2

def rob_bottom_up(v):
    global i
    if len(v) == 1:
        return v[0]

    res = [None] * (len(v) + 1)

    # base cases
    res[0] = v[0]
    res[1] = max(v[0], v[1])
    
    for house in v:
        rob_this_house = v[i] + res[i - 2]
        dont_rob_this_house = res[i - 1]
        res[i] = max(rob_this_house, dont_rob_this_house)
        i = i + 1
    return res[-1]


a = [3, 10, 3, 1, 2]
print(rob_top_down(a, len(a) - 1))
print(rob_bottom_up(a))
