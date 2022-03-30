#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача
# решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
#Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.



# num1 = input().upper()
num1 = 'a2'.upper()
a = [el for el in num1]

# num2 = input().upper()
num2 = 'fffc4f'.upper()
b = [el for el in num2]

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
ten_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_to_ten(list, dict):
    otv = []
    for el in list:
        otv.append(dict[el])
    return otv


# sum
def hex_sum(a, b):
    ''' add 2 numbers in 16x format'''
    a = a[::-1]
    b = b[::-1]

    a, b = hex_to_ten(a, hex_dict), hex_to_ten(b, hex_dict)
    size = max(len(a), len(b))
    a.extend([0] * (size - len(a)))
    b.extend([0] * (size - len(b)))

    sum = []
    rest = 0
    for i in range(min(len(a), len(b))):
        c = a[i] + b[i]
        sum.append((c + rest) % 16)
        rest = (c + rest) // 16

    if rest > 0:
        sum.append(rest)

    print(f'{a[::-1]} + \n{b[::-1]} = \n{sum[::-1]}')
    sum = hex_to_ten(sum, ten_dict)
    sum = sum[::-1]
    print(sum)

    return (sum)


# multiply
def hex_multiply(a, b):
    ''' add 2 numbers in 16x format'''
    a = a[::-1]
    b = b[::-1]

    a, b = hex_to_ten(a, hex_dict), hex_to_ten(b, hex_dict)
    size = len(a) + len(b) + 2

    # a is always longer then b
    if len(b) > len(a):
        a, b = b, a

    otv = [[0] * size for i in range(len(b))]
    otv_vec = [0] * size
    # print(a, b)

    for i in range(0, len(b)):
        rest = 0
        for j in range(len(a)):
            c = a[j] * b[i]
            otv[i][j + i] = (c + rest) % 16
            rest = (c + rest) // 16
            # print(f'{a[j]} * {b[i]} = {otv} NNNN rest {rest}')
        otv[i][j + i + 1] = rest
        # print("888"*50)
        # print(otv)
    # print(otv)

    rest = 0
    for j in range(len(otv_vec)):
        sum = 0
        for i in range(len(b)):
            sum += otv[i][j]
        otv_vec[j] = (sum + rest) % 16
        rest = (sum + rest) // 16

    print("888" * 10)
    print(f'{a[::-1]} * \n{b[::-1]} = \n{otv_vec[::-1]}')
    proizv = hex_to_ten(otv_vec, ten_dict)
    proizv = proizv[::-1]

    while proizv[0] == '0':
        proizv.pop(0)
    return proizv


###run function for sum
sum_ab = hex_sum(a, b)

numstr = ''
for el in sum_ab:
    numstr += str(el)

# check function for sum
ss = int(num1, 16) + int(num2, 16)
sss = hex(ss).upper()[2:]

is_correct = numstr == sss
print(
    f'RESULT IS {is_correct}. \nresult for sum of {a} and {b} \nwith hex-function is {sss} \nand with homemade fuction is {numstr}.')

####run function for multiply
print("#" * 20)

proizv = hex_multiply(a, b)

numstr = ''
for el in proizv:
    numstr += str(el)

# check function for multiply
ss = int(num1, 16) * int(num2, 16)
sss = hex(ss).upper()[2:]

is_correct = numstr == sss
print(
    f'RESULT IS {is_correct}. \nresult for multiply {a} and {b} \nwith hex-function is {sss} \nand with homemade fuction is {proizv}.')  #
