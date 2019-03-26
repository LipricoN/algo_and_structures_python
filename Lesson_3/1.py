# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

seq = [x for x in range(2, 100)]
div = {x: 0 for x in range(2, 10)}

for d in div.keys():
    for s in seq:
        if s % d == 0:
            div[d] += 1

for d in div.keys():
    print(f'Числу {d} в диапазоне от 2 до 99 кратно {div[d]} чисел.')