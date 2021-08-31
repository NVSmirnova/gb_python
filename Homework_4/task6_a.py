from sys import argv
from itertools import count
script_name, start_num, stop_num = argv
#out_list = [el for el in count(int(start_num)) if el < int(stop_num)]
for el in count(int(start_num)):
    if el > int(stop_num):
       break
    else:
        print(el)
#print(out_list)