# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

mass = [randint(0, 20) for _ in range(randint(30, 100))]

print(f'Дан массив:\n\n {mass}\n\n'
      f'Какое число в массиве встречается чаще всего?\n')

count = {x: 0 for x in set(mass)}

for key in count.keys():
    for m in mass:
        if key == m:
            count[key] += 1

often_key = None
often_val = None
for key, val in count.items():
    if often_val is None or often_val < val:
        often_key = key
        often_val = val

print(f'Число {often_key} встречается чаще всего в массиве, {often_val} раз')