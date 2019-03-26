"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа.  Например, пользователь ввёл A2 и C4F. Сохранить их как[‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

class HexOperations():
    def __init__(self, hex_deque):
        self.num = hex_deque
        self.summ = deque()
        self.mult = deque()
    
    def __add__(self, obj):
        num_add = self.num.copy()
        obj_add = obj.num.copy()
        
        if len(num_add) < len(obj_add):
            for i in range(len(obj_add) - len(num_add)):
                num_add.appendleft('0')
        elif len(obj_add) < len(num_add):
            for i in range(len(num_add) - len(obj_add)):
                obj_add.appendleft('0')
        
        num_add.appendleft('0')
        obj_add.appendleft('0')
        
        num_add.reverse()
        obj_add.reverse()
        for i in range(len(num_add)):
            if int(num_add[i], 16) + int(obj_add[i], 16) > 15: 
                num_add[i+1] = hex(int(num_add[i+1], 16) + 1).replace('0x', '')
                self.summ.appendleft(hex(int(num_add[i], 16) + int(obj_add[i], 16))[-1].upper())            
            else:
                self.summ.appendleft(hex(int(num_add[i], 16) + int(obj_add[i], 16))[-1].upper())
                      
        if self.summ[0] == '0':
            self.summ.popleft()
               
        return self.summ
    
    def __mul__(self, obj):
        num_mul = self.num
        obj_mult = obj.num
        
        mult_1 = ''.join(num_mul)
        mult_1 = int(mult_1, 16)
        mult_2 = ''.join(obj_mult)
        mult_2 = int(mult_2, 16)
        
        tmp_mult = mult_1 * mult_2
        tmp_mult = hex(tmp_mult)
        tmp_mult = tmp_mult.replace('0x', '')
        
        self.mult = deque(tmp_mult)
        
        for i in range(len(self.mult)):
            self.mult[i] = self.mult[i].upper()
        
        return self.mult
        
            

num_1 = deque(input('Введите первое число: '))
num_2 = deque(input('Введите первое второе: '))

print(f'Введены два шестнадцатеричных числа: {num_1}, {num_2}. Найти сумму и произведение чисел.')

num_1_hex = HexOperations(num_1)
num_2_hex = HexOperations(num_2)

print(f'Сумма чисел равна: {num_1_hex + num_2_hex}')
print(f'Произведение чисел равно: {num_1_hex * num_2_hex}')
