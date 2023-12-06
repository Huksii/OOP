# class Myobject:

#     def __init__(self, a, b):
        
#         self.a = a
#         self.b = b

#     def mmm(self):
#         self.a = 6
#         return self.a

# myobject = Myobject(5 , 8)

# print(myobject.a)
# print(myobject.mmm())
# # "" = str()

# class МойКласс:
#     def __init__(self, аргумент1, аргумент2):
#         self.атрибут1 = аргумент1
#         self.атрибут2 = аргумент2
    
#     def метод(self):
#         print("Это метод объекта")

# объект = МойКласс("значение1", "значение2")

# print(объект.атрибут1)

from datetime import datetime

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.year = datetime.now().year

#     def get_name(self):
#         return f"Меня зовут {self.name}"

#     def rename(self, old_name, new_name):
#         if self.name == old_name:
#             self.name = new_name
#             return f"Имя {old_name} изменено на {new_name}"
#         else:
#             return f"{self.name} не равен {old_name}"
        
#     def dr(self, birth_date):
#         self.age = self.year - birth_date
#         return f"Вам исполнилось {self.age}"

# people = Person("Ералы", 25)
# people2 = Person("Марсель", 20)

# # print(people.name)
# # print(people.age)
# # print(people2.get_name())
# # print(people.rename("Ералы","Yeraly"))
# # print(people.name)
# print(people.dr(1998))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.year = age

#     def morning(self):
#         if self.year is not None:
#             return f"Кошка {self.name} проснулась"
#         else:
#             return f"Кошка {self.name} ушла х_х"

#     def meal(self):
#         if self.year is not None:
#             return f"Кошка {self.name} кушает"
#         else:
#             return f"Кошка {self.name} больше кушать не может"
    
#     def player(self):
#         if self.year is not None:
#             if self.age <=5:
#                 return f"Кошка {self.name} играет"
#             else:
#                 return f"Кошка {self.name} уже стал папой"
#         else:
#             return f"Кошка {self.name} больше не играет"
    
#     def night(self):
#         if self.year is not None:
#             self.age += 1
#             if self.age == 7:
#                 self.year = None
#             return f"Кошка {self.name} спит"
#         else:
#             return f"Кошка {self.name} стала спящей красавицей"
        
#     def __str__(self) -> str:
#         return f"Это кошка по имени {self.name}"           #Возвращает сам экземпляр а не информацию объекта print(cat)
    
# cat = Cat("Муняня", 1)
# cat1 = Cat("Давинчи", 2)

# print(cat)

# for i in range(1,10):
#     print(cat.morning())
#     print(cat.meal())
#     print(cat.player())
#     print(cat.night())

#     print(cat1.morning())
#     print(cat1.meal())
#     print(cat1.player())
#     print(cat1.night())


# Создание класса и экземпляра:

# Создайте класс Car, у которого есть атрибуты make (марка) и model (модель).
# Создайте экземпляр класса Car для вашей мечтаемой машины и выведите ее марку и модель.
# Добавление методов:

# Расширьте класс Car, добавив метод start(), который выводит сообщение "Двигатель запущен" и метод stop(), который выводит сообщение "Двигатель остановлен".
# Создайте экземпляр класса Car и вызовите методы start() и stop().
# Изменение атрибутов:

# Добавьте атрибут mileage (пробег) к классу Car и установите начальное значение равным 0.
# Создайте метод drive(miles), который увеличивает mileage на указанное количество миль.
# Вызовите метод drive(100) для экземпляра класса Car и выведите текущий пробег.
# Сравнение объектов:

# Создайте два экземпляра класса Car с разными марками и моделями.
# Напишите метод is_same_car(other_car), который сравнивает марку и модель текущей машины с другой машиной (переданной в качестве аргумента).
# Вызовите метод is_same_car() для сравнения двух машин.
# Использование __str__:

# Переопределите магический метод __str__ в классе Car так, чтобы он возвращал строку, представляющую машину в виде "Марка: [марка], Модель: [модель], Пробег: [пробег]".
# Выведите экземпляр класса Car с помощью print().
# Дополнительное задание:

# Придумайте свой класс, создайте несколько экземпляров и опишите, какие атрибуты и методы он должен иметь, и как они могут быть использованы.

class Car:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        self.mileage = 0
    
    def start(self):
        return "Двигатель запущен"
    
    def stop(self):
        return "Двигатель остановлен"
    
    def drive(self, miles):
        self.mileage += miles
        return f"Пробег увиличился на {miles} миль"
    
    def is_same_car(self, other_car):
        return self.make == other_car.make and self.model == other_car.model
    
    def __str__(self) -> str:
        return f"Марка: {self.make}, Модель: {self.model}, Пробег: {self.mileage}"
    

my_car = Car("Toyota", "Camry")
my_car2 = Car("Tesla", "Model 3")

print(my_car.start())
print(my_car.drive(100))

if my_car.is_same_car(my_car2):
    print("Это одна и та же машина")
else:
    print("Это разные машины")

print(my_car.stop())