from sys import argv
from itertools import cycle
script_name, amount_of_rep, *string_to_repeat = argv
c = 0
for el in cycle(string_to_repeat):
    if c >= int(amount_of_rep) * len(string_to_repeat):
       break
    else:
        print(el)
    c += 1