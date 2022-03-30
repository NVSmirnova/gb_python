#задача считать последние 3000 ip адресов из лога,
# оставить все кроме локальных, сохранить порядок и посчитать сколько раз на какой айпи заходили.
from collections import OrderedDict, defaultdict, deque

N=3000
with open('big_log.txt', 'r', encoding='UTF-8') as f:
    log=deque(f, N)

print(log)

data=OrderedDict()
spam=defaultdict(int)

for item in log:
    ip=item[:-1] #убрали перенос строки после каждого айпишника

    if not ip.startswith('192.168'):
        spam[ip] +=1 #подсчет количества раз для айпи
        data[ip] = 1 #сохранение порядка обращения к айпи

print(spam)
print(data)

data.update(spam) #в сортированном data обновляем значения, которые теперь соответствуют количеству обращений на айпи

with open('data.txt', 'w', encoding='utf-8') as f:
    for key,value in data.items():
        f.write(f'{key} - {value}\n')
