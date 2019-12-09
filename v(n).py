# V(1) = 1
# V(2) = 1
# V(n) = V (V (n-1)) + V(n – V(n-1))

cache = {}


def mem(n):
    if n == 1 or n == 2:
        return 1

    if n not in cache:
        cache[n] = mem(mem(n-1)) + mem(n - mem(n-1))
    return cache[n]


array = []


def tab(n):
    if n == 1 or n == 2:
        return 1

    array.append(tab(tab(n-1)) + tab(n - tab(n-1)))
    return array[-1]

    # array = [1, 1]
    #
    # for i in range(3, n):
    #     #array.append(array[array[i-1]] + array[i - array[i-1]])
    #     array[i] = array[array[i-1]] + array[i - array[i-1]]
    # return array[-1]


print("Memoization: ")
print(mem(10))
print(mem(8))
print(mem(5))
print(mem(4))
print(mem(3))
print(mem(2))
print(mem(1))
print("Tabulation: ")
print(tab(10))
print(tab(8))
print(tab(5))
print(tab(4))
print(tab(3))
print(tab(2))
print(tab(1))
