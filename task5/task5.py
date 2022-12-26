# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

n = int(input('Размер массива: '))
lst = []
for i in range(n):
    x = int(input('Введите число массива: '))
    lst.append(x)
print(lst)
import datetime
for i in range(0, len(lst)):
    j = datetime.datetime.now().microsecond % len(lst) - 1
    lst[i], lst[j] = lst[j], lst[i]
print(lst)