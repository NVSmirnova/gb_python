from sys import argv
from functools import reduce
skript_name, en = argv

def mult_duo(a, b):
    '''Multiplies 2 numerics'''
    return a * b

def fact(n):
    '''creates list of factorials for input list (from 1 to n)'''
    for el in range(1, n+1):
        #yield fact(el)
        yield reduce(mult_duo, range(1, el+1))

gg = fact(int(en))
print(gg)

for el in gg:
    print(el)