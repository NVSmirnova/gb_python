#task 1
print("task1")
l1 = [0, 3.5, "trtr", True]
for i in l1:
    print(type(i))

#task2
print("task2")
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
l2c = l2.copy()
while i < len(l2)-1:
    l2c[i] = l2[i+1]
    l2c[i+1] = l2[i]
    i = i + 2
print(l2c)

#task3
print('task3')
mes = int(input("write number of month: "))
year_d = {1:'winter', 2:'winter', 12:'winter',
        3:'spring', 4:'spring', 5:'spring',
        6:'summer', 7:'summer', 8:'summer',
        9:'autumn', 10:'autumn', 11:'autumn'}
print(year_d[mes])
year_l = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
          'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print(year_l[mes-1])

#task4
print('task4')
sentence = input("write your phrase: ")
sentence = sentence.split(' ')
for num, word in enumerate(sentence, 1):
    print(f'{num} {word[:11]}')

#task5
print('task5')
reiting = [7, 6, 3, 3, 2, 2]
new_reit = int(input("write new reiting: "))
reiting_s = list(set(reiting))
reiting_s = reiting_s[::-1]
i = 0
if new_reit <= reiting[-1]:
    new_index = len(reiting)  # len(reiting)
else:
    new_index = 0
    while reiting_s[i] > new_reit:
        new_index = reiting.index(reiting_s[i])+1
        i = i + 1
reiting.insert(new_index, new_reit)
print(reiting)