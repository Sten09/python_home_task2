# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

#in
#6

#out
#[2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
#14.071

n = int(input('Введите число: '))
lst = []
x = 1
for i in range(n):
    lst.append((1+(1/x))**x)
    x += 1
sum = 0
for i in lst:
    sum = sum + i
print('сумма =', round(sum, 2))