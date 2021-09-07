from functools import reduce
input_list = [el for el in range(100, 1001, 2)]
def mult_duo(a, b):
    return a * b
print(reduce(mult_duo, input_list))