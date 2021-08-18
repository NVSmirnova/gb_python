import time

# task 1
print("task 1")
a = int(input("Введите целое число: "))
name = str(input("Введите имя: "))
print("My name is", name)
print("I am ", a, "years old.")

# task2
print("task 2")
x = int(input("Введите количество секунд (каждые 86400 секунд счетчик обнуляется): "))
print(time.strftime('%H:%M:%S', time.gmtime(x)))

#task 3
print("task 3")
n = input("Введите целое число: ")
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
print(n, "+", nn, "+", nnn, "=", n+nn+nnn)

#task 4
print("task 4")
m = input("Введите целое положительное число: ")
i = 0
otv = int(m[i])
while i < (len(m)):
    if int(m[i]) > otv:
        otv = int(m[i])
    i = i + 1
print(otv)

#task 5
print("task 5")
vyr = int(input("Укажите выручку: "))
izd = int(input("Укажите издержки: "))
if vyr > izd:
    print("У вас есть прибыль")
    rentab = (vyr - izd) / vyr
    print("Ваша рентабельность: ", rentab)
    sotr = int(input("Укажите количество сотрудников: "))
    prib_na_sotr = (vyr - izd) / sotr
    print("Прибыль на одного сотрудника: ", prib_na_sotr)
else:
    print("У вас только убытки")

#task 6
print("task 6")
nach_km = int(input("Укажите начальную дистанцию: "))
kon_km = int(input("Укажите конечную дистанцию: "))
den = 1
tek_km = nach_km
while tek_km < kon_km:
    tek_km = 1.1 * tek_km
    den = den + 1
print(den)


