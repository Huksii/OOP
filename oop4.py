# Полиморфизм

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def voice(self):
        return "Какой-то звук"
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def voice(self):
        return "Миаумяумияау"
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def voice(self):
        return "Гавгав"
    
class Cow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

a = Cat("Кошка")
b = Dog("Собака")
c = Cow("Корова")
d = Animal("Животные")

all_class = a, b, c, d

for i in all_class:
    print(i.name)
    print(i.voice())