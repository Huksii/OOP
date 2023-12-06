# Принцип ИНКАПСУЛЯЦИИ, полиморфизма, наследование

# class Myclass:
#     def __init__(self) -> None:
#         self.public_attribute = 50
#         self._protected_attribute = 40
#         self.__private_attribute = 30
#         # Виды инкапсуляции:
#         # public = name - можно вызвать где угодно
#         # protected = _name - в крайнем случае
#         # private = __name - нельзя вызывать вне класса

#     def public_method(self):
#         return "Это - открытый метод"
    
#     def _protected_method(self):
#         return "Это - защищённый метод"
    
#     def __private_method(self):
#         return "Это - приватный метод"
    
#     def __str__(self) -> str:
#         return "Инкапсуляция"
    
# obj = Myclass()

# print(obj.public_attribute)
# print(obj.public_method())
# print(obj._protected_attribute)    
# print(obj._protected_method())

class Tefalle:
    """
    Базовый класс для представления электрического чайника.
    Attributes: 
        name (str): Имя чайника

    Methodes:
        turn_on: Метод для включения чайника, запускающий процесс кипения воды 
        __boil: Внутренний метод, представляющий процесс закипания воды
        __done: Внутренний метод, завершающий процесс кипечения
        _turn_off: Внутренний метод, представляющий выключение чайника

    Example:
        # Создание экземпляра чайника
        teff = Tefalle("Тефаль 1")

        # Включение чайника
        teff.turn_on()

    Note:
        - Метод turn_on включает чайник и выводит информацию 
        о процессе кипячения воды.
        - Методы __boil, __done и _turn_off предназначены 
        для внутреннего использования и не предназначены
          для вызова напрямую извне класса.
        - Процесс кипячения воды симулируется с использованием 
        внутренних методов __boil и __done.
    """
    def __init__(self, name):
        self.name = name
    
    def turn_on(self) -> str:
        """
        Метод для включения чайника и запуска процесса кипечения воды.

        Returns:
            str: Строка, представляющая процесс включения чайника и кипечения воды

        Example:
        teff = Tefalle("Тефаль 1")
        teff.turn_on() 
        """
        print(f"Включение")
        print(self.__boil())
        print(self.__done())
        print(self._turn_off())
    
    def __boil(self):
        """
        Внутренний метод, представляющий процесс закипания воды.

        Returns:
            str: Строка, представляющая стадию закипания воды.

        Note:
            Этот метод предназначен для внутреннего использования и не следует вызывать напрямую
        """
        return f"Вода на стадии кипения"
    
    def __done(self):
        """
        Внутренний метод, представляющий завершение кипячения воды.

        Returns:
            str: Строка, представляющая завершение процесса кипячения воды.

        Note:
            Этот метод предназначен для внутреннего использования и не следует вызывать напрямую.
        """
        return f"Вода закипела"
    
    def _turn_off(self):
        """
        Внутренний метод, представляющий выключение чайника.

        Returns:
            str: Строка, представляющая процесс выключения.

        Note:
            Этот метод предназначен для внутреннего использования и не следует вызывать нарямую.
        """
        return f"Выключение"
    
    def __str__(self):
        return f"Тефаль {self.name}"
    
Чайник = Tefalle("Тефаль 1")
Чайник2 = Tefalle("Тефаль 2")

Чайник.turn_on()
print(Чайник.__boil())
print(Чайник._turn_off())

напечатать = print
сделать_циврой = int
переменная_где_будет_стринг = input
проверить_тип_переменной = type
тут_текст_который_стал_циврой = переменная_где_будет_стринг(
        "Напишите цивру: "
    )

напечатать(
    сделать_циврой(
                тут_текст_который_стал_циврой
            )
        )
напечатать(
    проверить_тип_переменной(
        сделать_циврой(
                тут_текст_который_стал_циврой
            )
        )
    )

from datetime import date, datetime

class Life:
    """
    Класс Life представляет информацию о днях, прожитых с момента дня рождения.

    Attributes:
        name (str): Имя человека.
        date_birth (date): День рождения в формате "ГГГГ.ММ.ДД".
        today (date): Текущая дата.

    Methods:
        days: Возвращает количество дней, прожитых с момента дня рождения.

    Example:
        # Создание экземпляров класса Life
        p3 = Life("Virineya", "2012.09.27")
        p4 = Life("Marselle", "2003.05.01")

        # Вывод информации о количестве дней, прожитых с момента дня рождения
        print(p3.days())  # Выведет количество дней, прожитых Virineya
        print(p4.days())  # Выведет количество дней, прожитых Marselle
    """
    def __init__(self, name, date_birth):
        self.name = name
        self.date_birth = datetime.strptime(date_birth, "%Y.%m.%d").date()
        self.today = date.today()
    
    def days(self):
        """
        Метод возвращает количество дней, прожитых с момента дня рождения.

        Returns:
            str: Строка, представляющая количество дней, прожитых с момента дня рождения.

        Example:
            p3 = Life("Virineya", "2012.09.27")
            p4 = Life("Marselle", "2003.05.01")
            print(p3.days())  # Выведет количество дней, прожитых Virineya
            print(p4.days())  # Выведет количество дней, прожитых Marselle
        """
        days_lived = (self.today - self.date_birth).days
        return f"{self.name} has {days_lived} days behind"

# Пример использования:
p3 = Life("Virineya", "2012.09.27")
p4 = Life("Marselle", "2003.05.01")

print(p3.days())  # Выведет количество дней, прожитых Virineya
print(p4.days())  # Выведет количество дней, прожитых Marselle

class Second:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_sec(self):
        """
        Метод для вычисления общего количества секунд.

        Returns:
            int: Общее количество секунд во времени.

        Example:
            time = Second(14, 46, 8)
            total_seconds = time.total_sec()
            print(total_seconds)  # Выведет общее количество секунд во времени
        """
        total = self.hours * 3600 + self.minutes * 60 + self.seconds
        return total

    def __str__(self):
        """
        Магический метод для представления объекта в виде строки.

        Returns:
            str: Строка, представляющая время в формате "ЧЧ:ММ:СС".

        Example:
            time = Second(14, 46, 8)
            print(time)  # Выведет "14:46:08"
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Пример использования:
time = Second(14, 46, 8)
total_seconds = time.total_sec()
print(f"Общее количество секунд: {total_seconds}")
print(time)  # Выведет "14:46:08"


class Furniture:
    def __init__(self, name, area, made_in, price):
        self.name = name
        self.area = area
        self.made_in = made_in
        self.price = price

    def get_info(self):
        print(f'Название: {self.name}')
        print(f'Площадь: {self.area}')
        print(f'Страна: {self.made_in}')
        print(f'Цена: {self.price}')
        print()


class Home:
    def __init__(self, count_floors, style, area) -> None:
        self.count_floors = count_floors
        self.style = style
        self.area = area
        self.price = self.area * 600000  # 60 лямов

    def get_info(self):
        print(f'Количество этажей: {self.count_floors}')
        print(f'Стиль: {self.style}')
        print(f'Количество area: {self.area}')
        print(f'Цена: {self.price}')
        print()

    def rise_price(self, percent: int):
        diff = self.price * percent / 100
        self.price += diff
        print(f'Цена выросла на {diff}')

    def low_price(self, percent: int):
        diff = self.price * percent / 100
        self.price -= diff
        print(f'Цена упала на {diff}')
    
    def add_furniture(self, furniture, count = 1):
        for i in range(count):
            self.furniture.append(furniture)
        print(f'Добавлен {count} {furniture.name}')
        print()


class CompareHomes:
    def compare(self, home1, home2):
        if home1.price > home2.price:
            print(f'{home1.style} цена больше {home2.style}')
        elif home1.price < home2.price:
            print(f'{home1.style} цена меньше {home2.style}')
        else:
            print(f'{home1.style} цена равна {home2.style}')
        print()
    
shkaf = Furniture('Шкаф', 4, 'Россия', 80000)
stol = Furniture('Стол', 2,'Казахстан', 40000)
bed = Furniture('Кровать', 5, 'Россия', 100000)


h1 = Home(3, 'Квартирный', 100)


h1.add_furniture(stol, 3)




# h2 = Home(2, 'Комнатный', 80)

# s = CompareHomes()
# s.compare(h1, h2)




# h1.rise_price(4)
# h1.low_price(6)
# h1.get_info()







# h3 = Home(2, 'Коттеджный', 10, 1000000)
# h4 = Home(3, 'Квартирный', 5, 500000)
# h5 = Home(2, 'Квартирный', 5, 500000)
# h6 = Home(2, 'Квартирный', 5, 500000)
