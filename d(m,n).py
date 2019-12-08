# d(m,n) = 1       if m or n == 0
# d(m,n) = d(m-1,n) + d(m-1, n-1) + d(m, n-1)

cache = {}


def mem(m, n):
    if m == 0 or n == 0:
        return 1

    key = str(m) + "|" + str(n)
    if key not in cache:
        cache[key] = mem(m-1, n) + mem(m-1, n-1) + mem(m, n-1)
    return cache[key]


array = []


def tab(m, n):
    if m == 0 or n == 0:
        return 1

    array.append(tab(m-1, n) + tab(m-1, n-1) + tab(m, n-1))
    return array[-1]


print("Memoization: ")
print(mem(5, 5))
print(mem(4, 5))
print(mem(5, 4))
print(mem(3, 4))
print(mem(4, 3))
print("Tabulation: ")
print(tab(5, 5))
print(tab(4, 5))
print(tab(5, 4))
print(tab(3, 4))
print(tab(4, 3))
