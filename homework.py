class Bank:
    def __init__(self, balance, password):
        self.balance = balance
        self.password = password

    def check_password(self):
        count_digit = 0
        count_upper = 0
        count_symbol = 0
        for i in self.password:
            if i.isdigit():
                count_digit +=1

            if i.isupper():
                count_upper +=1

            if i in "!@#$%^&*":
                count_symbol +=1

        if count_digit > 2 and count_upper > 0 and count_symbol > 0 and len(self.password)>= 10:
            return "Отличный пароль"
        elif count_digit == 0:
            return "Пароль должен содержать минимум 2 цифры"
        elif count_upper == 0:
            return "В пароле хотя бы одна буква должна быть заглавной"
        elif count_symbol == 0:
            return "Попробуйте добавить какие-нибудь символы (!@#$%^&*) для надёжности пароля"
        else:
            return "Ваш пароль слишком короткий, длина должна быть не менее 10 символов"

    def check_balance(self):
        return f"Ваш баланс: {self.balance}"

    def deposit(self, a: int):
        new_balance = self.balance + a
        return f"Вы пополнили счёт на {a}, и теперь ваш баланс равен {new_balance}"

    def withdraw(self, p: int):
        new_balance = self.balance - p
        return f"Вы сняли с вашего счёта {p}, и теперь ваш баланс равен {new_balance}"
    
    def __str__(self) -> str:
        return "Это суперкласс Bank"


class Sber(Bank):
    def __init__(self, balance, password):
        super().__init__(balance, password)

    def deposit(self, percent: int):
        diff = self.balance * percent / 100
        self.balance += diff
        return f"Ваш сберегательный счёт пополнился на {int(diff)}, теперь ваш баланс {int(self.balance+diff)}"
    
    def __str__(self) -> str:
        return "Это подкласс Sber"



client1 = Bank(15000, "Qwer153t@")
client2 = Bank(28000, "Qwerty123!@#")

# print(client1.check_password())
# print(client2.check_password())

# print(client1.deposit(5000))
# print(client2.withdraw(3000))

sber1 = Sber(50000, "Qwerty123$")

# print(sber1.deposit(15))