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
    
    def __add__(self, obj):
        num_add = self.num
        obj_add = obj.num
        
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

num_1 = deque(input('Введите первое число: '))
num_2 = deque(input('Введите первое второе: '))

num_1_hex = HexOperations(num_1)
num_2_hex = HexOperations(num_2)

print(num_1_hex + num_2_hex)
