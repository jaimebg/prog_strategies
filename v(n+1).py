# V(1) = 1
# V(n+1) = 1 + V (n + 1 – V( V(n) ) )

cache = {}


def mem(n):
    if n == 1:
        return 1

    if n not in cache:
        cache[n] = 1 + mem(n - mem(mem(n-1)))
    return cache[n]


def tab(n):
    array = [1]

    for i in range(1, n):
        array.append(1 + array(i - array[array[i-1]]))
    return array[-1]

    # if n == 1:
    #     return 1
    #
    # array.append(1 + tab(n - tab(tab(n-1))))
    # return array[-1]


print("Memoization: ")
print(mem(5))
print(mem(4))
print(mem(3))
print(mem(2))
print(mem(1))
print("Tabulation: ")
print(tab(5))
print(tab(4))
print(tab(3))
print(tab(2))
print(tab(1))
