"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile

def find_nat_num_self(num):
    '''
    Поиск i-го по счёту простого числа без использования «Решета Эратосфена»
    '''
    nat_num = []
    counter = 2
    while len(nat_num) < num:
        for i in range(1, counter):
            if i == counter-1:
                nat_num.append(counter)
            
            if counter % i == 0 and i != 1:
                break
        
        counter += 1
    return(nat_num[-1])

def find_nat_num_eratosfen(num):
    last_num = 50000
    lst =  [n for n in range(last_num)]
    lst[1] = None
    
    m = 2
    while m < last_num:
        if lst[m] != None:
            j = m * 2
            while j < last_num:
                lst[j] = None
                j = j + m
        m += 1
    
    counter = 0
    nat_num = 0
    for i in range(len(lst)):
        if lst[i] and counter < num - 1:
            counter += 1
        elif lst[i] and counter == num - 1:
            nat_num = lst[i]
            break            
              
    return nat_num
 
num = int(input('Введите номер i-го простого числа для поиска: '))
print(f'Простое число {num} найдено без использования «Решета Эратосфена»: {find_nat_num_self(num)}')
print(f'Простое число {num} найдено c использованием «Решета Эратосфена»: {find_nat_num_eratosfen(num)}')

'''
При поиске простых чисел из первых двух сотен алгоритм без использования
«Решета Эратосфена» работает быстрее (при поиске в диапазоне от 0 до 50000, при уменьшении
числа время вычислений «Решета Эратосфена» значительно снижается), примерно на 250 простом
числе время выполнения обоих алгоритмов сравнивается (у меня около 0,082 с), далее время
выполнения алгоритма без «Решета Эратосфена» прямо пропорционально увеличению порядкового
номера простого числа, алгоритм «Решета Эратосфена» почти не изменяет скорость выполнения
и незначительно зависет от скорости поиска в списке с None и простыим числами
'''
cProfile.run('find_nat_num_self(num)')
cProfile.run('find_nat_num_eratosfen(num)')

