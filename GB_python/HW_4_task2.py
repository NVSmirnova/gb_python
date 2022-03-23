import cProfile
import functools
import timeit

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

def resheto(n):
    sieve = [i for i in range(10 * n)]
    sieve[1] = 0
    for i in range(2, 10 * n):
        if sieve[i] != 0:
            j = i * 2
            while j < 10 * n:
                sieve[j] = 0
                j += i
    result = [0] + [i for i in sieve if i != 0]
    return result[n]
#5      1000 loops, best of 5: 11.5 usec per loop
#10     1000 loops, best of 5: 24.3 usec per loop
#100    1000 loops, best of 5: 323 usec per loop
#500    1000 loops, best of 5: 1.83 msec per loop

#cProfile.run('resheto(100)')

def resheto_dict(n):
    sieve_dict = {0:0, 1:2}
    def _resheto_dict(n):
        if n in sieve_dict:
            return sieve_dict[n]
        sieve_dict[n] = resheto(n)
        return sieve_dict[n]

    return _resheto_dict(n)


#5      1000 loops, best of 5: 12 usec per loop
#10     1000 loops, best of 5: 24.8 usec per loop
#100    1000 loops, best of 5: 319 usec per loop
#500    1000 loops, best of 5: 1.76 msec per loop

#cProfile.run('resheto_dict(100)')

#print(resheto(5))
#print(resheto_dict(50))

#@functools.lru_cache()
def simple_num(n):
    result = [None] * (n+1)
    num = 2
    i = 1
    while result[n] == None:
        #print(f'num is {num}')
        ost = [num % i for i in range (2, num)]
        ost_0 = [i for i in ost if i == 0]
        #print(f'sum is {sum(ost)} ost is {ost}')
        if len(ost_0) == 0:
            result[i] = num
            i += 1
        #print(f'res is {result}')
        num += 1
    return result[n]

#5      1000 loops, best of 5: 9.53 usec per loop   ncalls = 10
#10     1000 loops, best of 5: 43.7 usec per loop   ncalls = 28
#100    1000 loops, best of 5: 11 msec per loop     ncalls = 540
#500    10 loops, best of 5: 506 msec per loop      ncalls = 3570

#with @functools.lru_cach()
#5      1000 loops, best of 5: 116 nsec per loop
#10     1000 loops, best of 5: 115 nsec per loop
#100    1000 loops, best of 5: 81.8 nsec per loop
#500    100 loops, best of 5: 83.3 nsec per loop
#:0: UserWarning: The test results are likely unreliable. The worst time (5.26 msec) was more than four times slower than the best time (83.3 nsec).


#print(simple_num(5))

#cProfile.run('simple_num(10)')

#Вывод: быстрее всего работает второй алгоритм (не решето, а функция simple_num)
# с использованием кэширования вычислений (@functools.lru_cache()). Однако, без кэширования данный алгоритм работает оооочень долго и
# вызывает функцию (ncalls в cProfile) больше одного раза.