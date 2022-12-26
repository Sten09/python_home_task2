# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Без работы с методами строк.

#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

sum = int(0)
number = float(input('Введите число: '))
if number < 0:
    number = number * -1
str_number = str(number)
number = number * (10 ** (abs(str_number.find('.') - len(str_number)) - 1))
while number % 10 > 0:
    sum += number % 10
    number = number // 10
print(int(sum))
