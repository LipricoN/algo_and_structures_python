"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from random import randint
from pympler import asizeof

class MyClassSlots():
    __slots__ = ['mass_1', 'mass_2', 'plug_1', 'plug_2']
    
    def __init__(self, mass_1, mass_2, plug_1=0, plug_2=0):
        self.mass_1 = mass_1
        self.mass_2 = mass_2
        self.plug_1 = plug_1
        self.plug_2 = plug_2
    
    def summ_mass(self):
        summ = []
        for i in range(len(self.mass_1)):
            summ.append(self.mass_1[i]+self.mass_2[i])
        return summ
    

class MyClassNotSlots():
    def __init__(self, mass_1, mass_2, plug_1=0, plug_2=0):
        self.mass_1 = mass_1
        self.mass_2 = mass_2
        self.plug_1 = plug_1
        self.plug_2 = plug_2        
    
    def summ_mass(self):
        summ = []
        for i in range(len(self.mass_1)):
            summ.append(self.mass_1[i]+self.mass_2[i])
        return summ
    

if __name__ == '__main__':
    print('Нахождение суммы элементов двух списков.')
    num = int(input('Введите размер списка: '))
    
    mass_1 = [randint(0, 1000) for _ in range(num)]
    mass_2 = [randint(0, 1000) for _ in range(num)]
    
    print(f'\nДаны два списка:\n'
          f'{mass_1}\n'
          f'{mass_2}\n')
    
    summ_one = MyClassNotSlots(mass_1, mass_2)
    summ_two = MyClassSlots(mass_1, mass_2, 1, 2)
    
    print(f'Сумма элементов списков равна: {summ_one.summ_mass()}', end='\n\n')
    
    try:
        print(f'Словарь атрибутов summ_one:\n {summ_one.__dict__}', end='\n\n')
    except AttributeError:
        print('Экземпляр класса MyClassNotSlots не имеет словоря атрибутов!', end='\n\n')
    
    try:
        print(f'Словарь атрибутов summ_one:\n {summ_two.__dict__}', end='\n\n')
    except AttributeError:
        print('Экземпляр класса MyClassSlots не имеет словоря атрибутов!', end='\n\n')
        
    print(f'Экземпляр класса MyClassNotSlots занимает {asizeof.asizeof(summ_one)} байт')
    print(f'Экземпляр класса MyClassSlots занимает {asizeof.asizeof(summ_two)} байт')
    