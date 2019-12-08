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


def tab(m, n):
    array = [[1 for x in range(n)] for x in range(m)]
    if m == 0 or n == 0:
        array[m][n] = 1

    for i in range(m):
        for j in range(n):
            array[i][j] = array[i-1][j] + array[i-1][j-1] + array[i][j-1]
    return array[m-1][n-1]


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
