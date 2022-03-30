#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

amount_of_incorporations = int(input("amount of incorporations is:  "))

Inc = namedtuple('Inc', 'brand profit profit_mean')
profit_total = 0
my_objects = []

for i in range(amount_of_incorporations):
    name = 'inc_{}'.format(i)
    brand = input("brand:  ")
    lst = []
    for i in range(4):
        ele = int(input("profit for one quartal is:  "))
        lst.append(ele)

    profit_mean = sum(lst)/4
    profit_total += profit_mean

    my_objects.append(Inc(brand, lst, profit_mean))

profit_mean_all = profit_total/amount_of_incorporations

print(f' Full list of all corporations is \n{my_objects}\n')

print(f'profit_mean_all is {profit_mean_all}')
below_mean = []
above_mean = []
for i in range(amount_of_incorporations):
    if my_objects[i].profit_mean > profit_mean_all:
        above_mean.append(my_objects[i].brand)
    else:
        below_mean.append(my_objects[i].brand)

print(f'Corporations with mean profit BELOW mean profit total are {below_mean}')
print(f'Corporations with mean profit ABOVE mean profit total are {above_mean}')

# чужое решение
import collections

count_company = int(input('Введите количество предприятий: '))

company_dict = {input(f'Введите название {i} предприятий: '):
                    int(sum([int(input(f'Введите прибыль предприятия {i} для {j} квартала: ')) for j in range(1, 5)])/4)
                for i in range(1, count_company + 1)}
company_dict = collections.OrderedDict(sorted(company_dict.items(), key=lambda x: x[1]))

middle = 0
for company_name in company_dict:
    middle += company_dict[company_name]
middle = int(middle/len(company_dict))

print(f'\n\nВсе предприятия и их средняя прибыль за год: ')
print(*list(f'{company_name}: {company_dict[company_name]}$, ' for company_name in company_dict))
print(f'Средняя прибыль среди всех предприятий за год = {middle}$')

print('\nПредприятия, чья прибыль больше средней(для всех предприятий) за год: ', end='')
print(*list(f'{company_name}: {company_dict[company_name]}$'
            for company_name in company_dict if company_dict[company_name] > middle), sep=', ')

print('\nПредриятия, чья прибыль ниже средней(для всех предприятий) за год: ', end='')
print(*list(f'{company_name}: {company_dict[company_name]}$'
            for company_name in company_dict if company_dict[company_name] < middle), sep=', ')

###чужое решение
from collections import ChainMap
n = int(input("Введите количество предприятий: "))
k = 1
full_dict = ChainMap()
sum_profit = 0
while k <= n:
    name_firma = input(f'Введите наименование {k}го предприятия: ')
    profit = float(input(f'Введите прибыль за IV квартала {k}го предприятия: '))
    dict_spam = {'name': name_firma, 'profit': profit }
    full_dict = full_dict.new_child(dict_spam)
    k += 1
    sum_profit += profit
arg_profit = sum_profit / n
a = list()
b = list()

for i in range(n):
    c = full_dict.maps[i]['profit']
    if c > arg_profit:
        a.append(full_dict.maps[i]['name'])
    else:
        b.append(full_dict.maps[i]['name'])
print(f'Предприятия с большей прибылью, чем среднее {arg_profit}: {a} \nПредприятия с меньшей прибылью чем среднее {arg_profit}: {b}')

