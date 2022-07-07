import math
import cProfile


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


def show_prime(n):
    num = 100
    primes = erath(num)

    while n > len(primes):
        num = num*2
        primes = erath(num)

    return primes[n - 1]

# print(show_prime(100))

# cProfile.run('show_prime(100000)')

# "lesson4_task2_erath.show_prime(5)"
# 100 loops, best of 5: 19.1 usec per loop

# "lesson4_task2_erath.show_prime(10)"
# 100 loops, best of 5: 19.6 usec per loop

# "lesson4_task2_erath.show_prime(15)"
# 100 loops, best of 5: 19.7 usec per loop

# "lesson4_task2_erath.show_prime(20)"
# 100 loops, best of 5: 19.4 usec per loop

# "lesson4_task2_erath.show_prime(50)"
# 100 loops, best of 5: 137 usec per loop

# "lesson4_task2_erath.show_prime(100)"
# 100 loops, best of 5: 299 usec per loop

# "lesson4_task2_erath2.show_prime(1000)"
# 100 loops, best of 5: 6.33 msec per loop

# "lesson4_task2_erath2.show_prime(5000)"
# 100 loops, best of 5: 26.2 msec per loop

# "lesson4_task2_erath2.show_prime(10000)"
# 100 loops, best of 5: 123 msec per loop

# "lesson4_task2_erath2.show_prime(50000)"
# 100 loops, best of 5: 581 msec per loop

# "lesson4_task2_erath2.show_prime(100000)"
# 100 loops, best of 5: 1.28 sec per loop
