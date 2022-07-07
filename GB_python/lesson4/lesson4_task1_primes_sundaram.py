import timeit
import cProfile

def sundaram(n):
    lim = int((n - 1) / 2)
    marked = [0] * (lim + 1)
    res = []

    for i in range(1, lim + 1):
        j = i
        while ((i + j + 2 * i * j) <= lim):
            marked[i + j + 2 * i * j] = 1
            j += 1

    if (n > 2):
        res.append(2)

    for i in range(1, lim + 1):
        if (marked[i] == 0):
            res.append(2 * i + 1)
    return res

# print(sundaram(100))

cProfile.run('sundaram(1000000)')

# 1    0.000    0.000    0.000    0.000 lesson4_task1_primes_sundaram.py:4(sundaram)
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} - 100

# 1    0.000    0.000    0.000    0.000 lesson4_task1_primes_sundaram.py:4(sundaram)
# 168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} - 1000

# 1    0.010    0.010    0.010    0.010 lesson4_task1_primes_sundaram.py:4(sundaram)
# 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects -  10000

# 1    0.026    0.026    0.026    0.026 lesson4_task1_primes_sundaram.py:4(sundaram)
# 5133    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} - 50000

# 1    0.056    0.056    0.056    0.056 lesson4_task1_primes_sundaram.py:4(sundaram)
# 9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects} - 100000

# 1    0.328    0.328    0.332    0.332 lesson4_task1_primes_sundaram.py:4(sundaram)
# 41538    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects} - 500000

# 1    0.668    0.668    0.675    0.675 lesson4_task1_primes_sundaram.py:4(sundaram)
# 78498    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects} - 1000000