# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

five = 5
six = 6
offset = 2

do_and = five & six
do_or = five | six
do_xor = five ^ six
do_inv_five = ~five
do_inv_six = ~six
do_left_offset = five << offset
do_right_offset = five >> offset


print(f'{five} & {six} = {do_and}')
print(f'{five} | {six} = {do_or}')
print(f'{five} ^ {six} = {do_xor}')
print(f'~{five} = {do_inv_five}')
print(f'~{six} = {do_inv_six}')
print(f'{five} << {offset} = {do_left_offset}')
print(f'{five} >> {offset} = {do_right_offset}')



