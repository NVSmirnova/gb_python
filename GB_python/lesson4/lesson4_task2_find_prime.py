import math
import cProfile

def find_prime(n):
    if n == 1:
        return 2

    num = 3

    while True:
        isprime = True

        for x in range(2, int(math.sqrt(num) + 1)):
            if num % x == 0:
                isprime = False
                break

        if isprime:
            n -= 1
            if n <= 1:
                break

        num += 1

    return num

# print(find_prime(15))

# "lesson4_task2_find_prime.find_prime(5)"
# 100 loops, best of 5: 8.63 usec per loop

# "lesson4_task2_find_prime.find_prime(10)"
# 100 loops, best of 5: 19.3 usec per loop

# "lesson4_task2_find_prime.find_prime(15)"
# 100 loops, best of 5: 33.1 usec per loop

# "lesson4_task2_find_prime.find_prime(20)"
# 100 loops, best of 5: 50.9 usec per loop

# "lesson4_task2_find_prime.find_prime(50)"
# 100 loops, best of 5: 167 usec per loop

# "lesson4_task2_find_prime.find_prime(100)"
# 100 loops, best of 5: 434 usec per loop

# "lesson4_task2_find_prime.find_prime(1000)"
# 100 loops, best of 5: 9.15 msec per loop

# "lesson4_task2_find_prime.find_prime(5000)"
# 100 loops, best of 5: 79.9 msec per loop

# "lesson4_task2_find_prime.find_prime(10000)"
# 100 loops, best of 5: 215 msec per loop

# "lesson4_task2_find_prime.find_prime(50000)"
# 100 loops, best of 5: 2.48 sec per loop

# "lesson4_task2_find_prime.find_prime(100000)"
# 100 loops, best of 5: 7.2 sec per loop


# cProfile.run('find_prime(50000)')

# 1    0.010    0.010    0.011    0.011 lesson4_task2_find_prime.py:4(find_prime)
# 7917    0.001    0.000    0.001    0.000 {built-in method math.sqrt} 1000

# 1    0.096    0.096    0.104    0.104 lesson4_task2_find_prime.py:4(find_prime)
# 48609    0.008    0.000    0.008    0.000 {built-in method math.sqrt} 5000

# 1    0.245    0.245    0.261    0.261 lesson4_task2_find_prime.py:4(find_prime)
# 104727    0.017    0.000    0.017    0.000 {built-in method math.sqrt} 10000

# 1    2.650    2.650    2.747    2.747 lesson4_task2_find_prime.py:4(find_prime)
# 611951    0.097    0.000    0.097    0.000 {built-in method math.sqrt} 50000

# 1    7.356    7.356    7.547    7.547 lesson4_task2_find_prime.py:4(find_prime)
# 1299707    0.191    0.000    0.191    0.000 {built-in method math.sqrt} 100000