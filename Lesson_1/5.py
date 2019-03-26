# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

first_char = input('Введите первую букву: ')
second_char = input('Введите вторую букву: ')

if ord(first_char) < 1071:
    first_char_position = ord(first_char.lower()) - 96
    second_char_position = ord(second_char.lower()) - 96
else:
    print('\nГде-то мы потеряли букву Ё!\n')
    first_char_position = ord(first_char.lower()) - 1071
    second_char_position = ord(second_char.lower()) - 1071

char_dist = abs(first_char_position - second_char_position) - 1

print(f'Позиция буквы "{first_char}" в алфавите - {first_char_position}, буквы "{second_char}" - {second_char_position}'
      f', между буквами расположено {char_dist} букв')
