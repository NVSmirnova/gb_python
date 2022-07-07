import cProfile
import math


def erath(n):
  sieve = [i for i in range(n)]
  sieve[1] = 0
  lim = math.floor(math.sqrt(n))

  for i in range(2, lim + 1):
    if sieve[i] != 0:
      j = i * 2
      while j < n:
        sieve[j] = 0
        j += i

  result = [i for i in sieve if i != 0]
  return result


#print(erath(1000))

# "lesson4_task1_primes.erath(100)"
# 1000 loops, best of 5: 17.6 usec per loop

# "lesson4_task1_primes.erath(500)"
# 1000 loops, best of 5: 101 usec per loop

# "lesson4_task1_primes.erath(1000)"
# 1000 loops, best of 5: 215 usec per loop

# "lesson4_task1_primes.erath(10000)"
# 1000 loops, best of 5: 2.47 msec per loop

# "lesson4_task1_primes.erath(100000)"
# 1000 loops, best of 5: 28.3 msec per loop

cProfile.run('erath(1000000000)')

# 1    0.000    0.000    0.000    0.000 lesson4_task1_primes_erath.py:6(erath) 100
# 1    0.000    0.000    0.001    0.001 lesson4_task1_primes_erath.py:6(erath) 500
# 1    0.000    0.000    0.000    0.000 lesson4_task1_primes_erath.py:6(erath) 1000
# 1    0.002    0.002    0.003    0.003 lesson4_task1_primes_erath.py:6(erath) 10000
# 1    0.018    0.018    0.025    0.025 lesson4_task1_primes_erath.py:6(erath) 50000
# 1    0.025    0.025    0.034    0.034 lesson4_task1_primes_erath.py:6(erath) 100000
# 1    0.140    0.140    0.196    0.196 lesson4_task1_primes_erath.py:6(erath) 500000
# 1    0.298    0.298    0.400    0.400 lesson4_task1_primes_erath.py:6(erath) 1000000
# 1    3.321    3.321    4.368    4.368 lesson4_task1_primes_erath.py:6(erath) 10000000

