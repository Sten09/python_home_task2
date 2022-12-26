# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

number_elements = int(input("Введите количество элементов: "))
first_element = -number_elements
while True:
     try:
         pos_first_element = int(input("Введите позицию первого элемента: "))
         pos_second_element = int(input("Введите позицию второго элемента: "))
         if 0 <= pos_first_element <= number_elements * 2 + 1 and 0 <= pos_second_element <= number_elements * 2 + 1:
             break
         else:
             print('Эти цифры вне диапазона! Повторим:')
     except ValueError:
        print('Это не число! Повторим:')
list = []
for i in range(number_elements * 2 + 1):
    list += [first_element]
    first_element += 1
print(list)
print(f'Произведение заданных элементов {int(list[pos_first_element - 1]) * int(list[pos_second_element - 1])}')