"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

var_first_int = int(input('Введите первое целое число диапазона:'))
var_last_int = int(input('Введите второе целое число диапазона:'))

if var_first_int < var_last_int:
    rand_int = random.randint(var_first_int, var_last_int)
else:
    rand_int = random.randint(var_last_int, var_first_int)

print(rand_int, end='\n\n')

var_first_float = float(input('Введите первое дробное число диапазона:'))
var_last_float = float(input('Введите второе дробное число диапазона:'))

if var_first_float < var_last_float:
    rand_float = random.uniform(var_first_float, var_last_float)
else:
    rand_float = random.uniform(var_last_float, var_first_float)

print(rand_float, end='\n\n')

var_first_char = input('Введите первую букву диапазона:')
var_last_char = input('Введите вторую букву диапазона:')

if ord(var_first_char) < ord(var_last_char):
    rand_char = chr(random.randint(ord(var_first_char), ord(var_last_char)))
else:
    rand_char = chr(random.randint(ord(var_last_char), ord(var_first_char)))

print(rand_char, end='\n\n')
