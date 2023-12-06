# class Furniture:
#     def __init__(self, name, area, made_in, price):
#         self.name = name
#         self.area = area
#         self.made_in = made_in
#         self.price = price

#     def get_info(self):
#         print(f'Название: {self.name}')
#         print(f'Площадь: {self.area}')
#         print(f'Страна: {self.made_in}')
#         print(f'Цена: {self.price}')
#         print()


# class Home:
#     def __init__(self, count_floors, style, area) -> None:
#         self.count_floors = count_floors
#         self.style = style
#         self.area = area
#         self.price = self.area * 600000  # 60 лямов
#         self.furnitures = []

#     def get_info(self):
#         print(f'Количество этажей: {self.count_floors}')
#         print(f'Стиль: {self.style}')
#         print(f'Количество area: {self.area}')
#         print(f'Цена: {self.price}')
#         print()

#     def rise_price(self, percent: int):
#         diff = self.price * percent / 100
#         self.price += diff
#         print(f'Цена выросла на {diff}')

#     def low_price(self, percent: int):
#         diff = self.price * percent / 100
#         self.price -= diff
#         print(f'Цена упала на {diff}')
    
#     def add_furniture(self, furniture, count = 1):
#         for i in range(count):
#             self.furnitures.append(x)
#         print(f'Добавлен {count} {furniture.name} в {self.style} дом')
#         print()

#     def get_furniture_area(self):
#         furniture_area = 0
#         for i in self.furnitures:
#             furniture_area += i.area
#         print(f'Площадь мебелей в квартире {furniture_area}')
#         print()


# class CompareHomes:
#     def compare(self, home1, home2):
#         if home1.price > home2.price:
#             print(f'{home1.style} цена больше {home2.style}')
#         elif home1.price < home2.price:
#             print(f'{home1.style} цена меньше {home2.style}')
#         else:
#             print(f'{home1.style} цена равна {home2.style}')
#         print()
    
# shkaf = Furniture('Шкаф', 4, 'Россия', 80000)
# stol = Furniture('Стол', 2,'Казахстан', 40000)
# bed = Furniture('Кровать', 5, 'Россия', 100000)


# h1 = Home(3, 'Квартирный', 100)
# h1.add_furniture(shkaf, 5)
# h1.get_furniture_area()

# h1.add_furniture(stol, 3)
# h1.add_furniture(shkaf)




# h2 = Home(2, 'Комнатный', 80)

# s = CompareHomes()
# s.compare(h1, h2)




# h1.rise_price(4)
# h1.low_price(6)
# h1.get_info()


