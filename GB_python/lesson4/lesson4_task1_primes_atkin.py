import cProfile
import math

# def atkin1(n):
#     sieve = [0] * (n + 1)
#     lim = math.floor(math.sqrt(n))
#
#     for x in range(1, lim + 1):
#         for y in range(1, lim + 1):
#             a = 4 * x ** 2 + y ** 2
#             b = 3 * x ** 2 + y ** 2
#             c = 3 * x ** 2 - y ** 2
#             if a <= n and (a % 12 == 1 or a % 12 == 5):
#                 sieve[a] += 1
#             if b <= n and b % 12 == 7:
#                 sieve[b] += 1
#             if x > y and c <= n and c % 12 == 11:
#                 sieve[c] += 1
#
#     res = [2, 3]
#     for i, item in enumerate(sieve):
#         if item % 2 != 0 and i > 3:
#             j = i ** 2
#             if j < n:
#                sieve[j] = 0
#             res.append(i)
#
#     return res


# print(atkin1(100))


def atkin2(n):
    sieve = [False] * (n + 1)
    lim = int(math.floor(math.sqrt(n)))

    for x in range(1, lim + 1):
        xx = x * x
        xx3 = 3*xx
        xx4 = 4*xx
        for y in range(1, lim + 1):
            yy = y*y

            a = xx4 + yy
            b = xx3 + yy
            c = xx3 - yy
            if a <= n and (a % 12 == 1 or a % 12 == 5):
                sieve[a] = not sieve[a]
            if b <= n and b % 12 == 7:
                sieve[b] = not sieve[b]
            if x > y and c <= n and c % 12 == 11:
                sieve[c] = not sieve[c]

    res = [2, 3]
    for i, item in enumerate(sieve):
        if item == True and i > 3:
            j = i * i
            if j < n:
               sieve[j] = False
            res.append(i)

    return res


#print(atkin2(100))

# "lesson4_task1_primes_atkin.atkin1(100)"
# 1000 loops, best of 5: 172 usec per loop

# "lesson4_task1_primes_atkin.atkin1(500)"
# 1000 loops, best of 5: 833 usec per loop

# "lesson4_task1_primes_atkin.atkin1(1000)"
# 1000 loops, best of 5: 1.67 msec per loop

# "lesson4_task1_primes_atkin.atkin1(10000)"
# 1000 loops, best of 5: 17.8 msec per loop


# "lesson4_task1_primes_atkin.atkin2(100)"
# 100 loops, best of 5: 50.6 usec per loop

# "lesson4_task1_primes_atkin.atkin2(500)"
# 100 loops, best of 5: 229 usec per loop

# "lesson4_task1_primes_atkin.atkin2(1000)"
# 100 loops, best of 5: 457 usec per loop

# "lesson4_task1_primes_atkin.atkin2(10000)"
# 100 loops, best of 5: 4.72 msec per loop



# cProfile.run('atkin2(100)')


# 1    0.000    0.000    0.001    0.001 lesson4_task1_primes_atkin.py:5(atkin1) - 100
# 1    0.002    0.002    0.002    0.002 lesson4_task1_primes_atkin.py:5(atkin1) - 1000
# 1    0.021    0.021    0.021    0.021 lesson4_task1_primes_atkin.py:5(atkin1) - 10000
# 1    0.121    0.121    0.122    0.122 lesson4_task1_primes_atkin.py:5(atkin1) - 50000
# 1    0.196    0.196    0.197    0.197 lesson4_task1_primes_atkin.py:5(atkin1) - 100000
# 1    1.036    1.036    1.040    1.040 lesson4_task1_primes_atkin.py:5(atkin1) - 500000
# 1    2.046    2.046    2.053    2.053 lesson4_task1_primes_atkin.py:5(atkin1) - 1000000

# 1    0.000    0.000    0.000    0.000 lesson4_task1_primes_atkin.py:47(atkin2) - 100
# 1    0.001    0.001    0.001    0.001 lesson4_task1_primes_atkin.py:47(atkin2) - 1000
# 1    0.006    0.006    0.006    0.006 lesson4_task1_primes_atkin.py:47(atkin2) - 10000
# 1    0.042    0.042    0.043    0.043 lesson4_task1_primes_atkin.py:47(atkin2) - 50000
# 1    0.052    0.052    0.053    0.053 lesson4_task1_primes_atkin.py:47(atkin2) - 100000
# 1    0.271    0.271    0.275    0.275 lesson4_task1_primes_atkin.py:47(atkin2) - 500000
# 1    0.519    0.519    0.527    0.527 lesson4_task1_primes_atkin.py:47(atkin2) - 1000000

