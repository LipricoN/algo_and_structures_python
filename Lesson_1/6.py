# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

var_char_code = int(input('Введите порядковый номер буквы в алфавите: '))

print('\nГде-то мы потеряли букву Ё!\n')

if var_char_code > 32 or var_char_code < 1:
    print('Ни в русском, ни в английском алфавите нет такой буквы!')
elif var_char_code > 0 and var_char_code > 26:
    var_char_rus = chr(var_char_code + 1071)
    print(f'В русском алфавить это букв "{var_char_rus}", в английском алфавите такой буквы нет.')
elif 0 < var_char_code <= 26:
    var_char_rus = chr(var_char_code + 1071)
    var_char_eng = chr(var_char_code + 96)
    print(f'В русском алфавить это букв "{var_char_rus}", в английском - "{var_char_eng}".')
else:
    print('Возможно вы китаец :)')
