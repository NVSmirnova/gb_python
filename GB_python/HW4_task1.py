#урок 3 задача 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import cProfile
import random
import timeit

#var 1
def change_min_max_cycle(SIZE):
    test_arr = [random.randint(-100, 100) for i in range(SIZE)]
    ind_min = 0
    ind_max = 0
    for i in range(SIZE):
        if test_arr[i] < test_arr[ind_min]:
            ind_min = i
        if test_arr[i] > test_arr[ind_max]:
            ind_max = i
    test_arr[ind_max], test_arr[ind_min] = test_arr[ind_min], test_arr[ind_max]
    return test_arr

#5      1000 loops, best of 5: 5.2 usec per loop
#10     1000 loops, best of 5: 9.77 usec per loop
#100    1000 loops, best of 5: 89.7 usec per loop
#1000   1000 loops, best of 5: 914 usec per loop

#cProfile.run('change_min_max_cycle(10000)')


#var 2
def change_min_max(SIZE):
    test_arr = [random.randint(-100, 100) for i in range(SIZE)]
    ind_min = test_arr.index(min(test_arr))
    ind_max = test_arr.index(max(test_arr))
    test_arr[ind_max], test_arr[ind_min] = test_arr[ind_min], test_arr[ind_max]
    return test_arr

#5      1000 loops, best of 5: 4.89 usec per loop
#10     1000 loops, best of 5: 9.29 usec per loop
#100    1000 loops, best of 5: 86 usec per loop
#1000   1000 loops, best of 5: 840 usec per loop

#cProfile.run('change_min_max(10000)')

#Вывод: время работы обоих функций возрастает линейно в зависимости от размера исходного массива.
#Хоть первая функция обходит весь массив 1 раз, а вторая функция - 2 раза, время работы обоих фнкций примерно одинаковое.

##########################

#Урок 3 задание 7
#7. В одномерном массиве целых чисел определить два наименьших элемента.
#Они могут быть как равны между собой (оба минимальны), так и различаться.


def find_2min_cycle(test_ar):
    test_arr = test_ar.copy()
    otv = []
    for i in range(2):
        ind_min = 0
        for i in range(len(test_arr)):
            if test_arr[i] < test_arr[ind_min]:
                ind_min = i
        otv.append(test_arr[ind_min])
        test_arr.remove(test_arr[ind_min])
    return otv

def find_2min(test_ar):
    test_arr = test_ar.copy()
    otv = []
    for i in range(2):
        otv.append(min(test_arr))
        test_arr.remove(otv[i])
    return otv

def test_find_2min_cycle(SIZE):
    test_arr = [random.randint(-100, 100) for i in range(SIZE)]
    return find_2min_cycle(test_arr)

#5      1000 loops, best of 5: 5.89 usec per loop
#10     1000 loops, best of 5: 10.6 usec per loop
#100    1000 loops, best of 5: 93 usec per loop
#1000   1000 loops, best of 5: 970 usec per loop
#10000  1000 loops, best of 5: 9.67 msec per loop

def test_find_2min(SIZE):
    test_arr = [random.randint(-100, 100) for i in range(SIZE)]
    return find_2min(test_arr)

#5      1000 loops, best of 5: 5.29 usec per loop
#10     1000 loops, best of 5: 11 usec per loop
#100    1000 loops, best of 5: 86.8 usec per loop
#1000   1000 loops, best of 5: 864 usec per loop
#10000  1000 loops, best of 5: 8.48 msec per loop


#Вывод: время работы обоих функций возрастает линейно в зависимости от размера исходного массива.
#Время работы обоих функций примерно одинаковое, но второй вариант с использованием
# встроенных функций python работает чуть быстрее простого цикла

#cProfile.run('test_find_2min_cycle(500)')