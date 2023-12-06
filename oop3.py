# Наследование
# Это - суперкласс(родительский класс)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Какой-то звук"
    
    def __str__(self) -> str:
        return "Это суперкласс Animal"
    
# Это - подкласс(дочерний класс)
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        return f"{self.name}: Миау Мияау"
    
    def __str__(self) -> str:
        return f"Я кот {self.name}"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sound(self):
        return f"{self.name}: Гав гав"
    
    def __str__(self) -> str:
        return f"Я собака {self.name}"

cat1 = Cat("Dobby")
dog1 = Dog("Rex")

# print(cat1.name)
print(cat1.sound())
print(dog1.sound())