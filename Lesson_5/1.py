"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict

num_com = int(input('Введите количество предприятий: '))

company = defaultdict(list)

for n in range(num_com):
    name = input(f'Введите название организации {n+1}: ')
    all_val = input('Введите прибыль за четыре квартала разделенную пробелами: ').split()
    all_val = list(map(float, all_val))
    
    tmp_val = 0
    for n in all_val:
        tmp_val += n
        company[name].append(n)
    company[name].append(tmp_val)

avg_val = 0

for key in company.keys():
    avg_val += company[key][4]

avg_val = avg_val / len(company)

print()
print(f'{"Имя/Квартал":^12}{"1":^8}{"2":^8}{"3":^8}{"4":^8}{"Год":^8}')

for key in company.keys():
    print(f'{key:<12}', end='')
    for val in company[key]:
        print(f'{val:^8}', end='')
    print()

print()
print(f'Средняя прибыль предприятий за год: {avg_val:.2f}')

min_avg = []
max_avg = []
avg_avg = []

for key in company.keys():
    if company[key][4] > avg_val:
        max_avg.append(key)
    
    if company[key][4] < avg_val:
        min_avg.append(key)
    
    if company[key][4] == avg_val:
        avg_avg.append(key)    

if max_avg:
    print(f'Предприятия, чья прибыль выше среднего: {", ".join(max_avg)}')

if max_avg:
    print(f'Предприятия, чья прибыль ниже среднего: {", ".join(min_avg)}')

if avg_avg:
    print(f'Предприятия, чья прибыль равна средней: {", ".join(avg_avg)}')