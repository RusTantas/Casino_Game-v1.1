import random


# Создаем Класс Казино с балансом и проигрываением и выигрываем
class Casino:
    def __init__(self, balans):
        self.balans = balans

    def add_money(self, dodep):
        self.balans += dodep

    def supract_money(self, money):
        self.balans -= money


# Создаем Класс Игрок с балансом и проигрываением и выигрываем
class Player:
    def __init__(self, balans):
        self.balans = balans

    def add_money(self, dodep):
        self.balans += dodep

    def supract_money(self, money):
        self.balans -= money

    def play_game(self):
        pass


# Создаем Класс Игра с генерацией числа
class Game:
    def __init__(self):
        pass

    def generate_random_number(self, min, max):
        r_num = random.randint(min, max)
        return r_num


# вводим в ручную баланс игрока и казино
casino = Casino(100)
player = Player(100)
name = input('Привет! Как тебя зовут?\n')
print(
    'Отлично, {0}, я предагаю игру я загадал число между 1 и 20. Сможешь угадать? против тебя будет играть казино'.format(
        name))

print("Баланс Казино: ", casino.balans)
print("Баланс {0}: ".format(name), player.balans)

# Делаем цикл пока  либо у казино либо у игрока не закончатся деньги
while casino.balans > 0 and player.balans > 0:
    game = Game()
    # Генерим число которое надо угадать
    r_num = game.generate_random_number(10, 20)
    print("")
    #    print("Угадываем числр: ", r_num)     # Для проверки работы программы
    # Вывлдим баланс играков

    # Генерим число которое предполагает казино
    casino_number = random.randint(1, 20)
    print("казино предполагает что это число: ", casino_number)
    # Вводим свое число
    guess = int(input('Введи число: '))
    print("Угадываемое число было: ", r_num)
    # Смотрим кто ближе к ответу
    guess_chans = abs(r_num - guess)
    casino_number_chans = abs(r_num - casino_number)
    # для проверки работы программы
    #    print("результат игрока: ", guess_chans)
    #    print("результат казино: ", casino_number_chans)
    # Определяем кому зачислить деньги
    if guess_chans < casino_number_chans:
        casino.supract_money(50)
        player.add_money(50)
        print("{0} выйграл".format(name))

    elif guess_chans > casino_number_chans:
        player.supract_money(50)
        casino.add_money(50)
        print("Казино выйграла")

    else:
        print("Нечья")

    # Повторно выводим баланс
    print("Баланс Казино: ", casino.balans)
    print("Баланс {0}: ".format(name), player.balans)
# Определям кто выйграл в общей игре
else:
    if casino.balans <= 0:
        print("")
        print("Казино проигралло")
    else:
        print("")
        print("{0} проиграл".format(name))
# Для проверки
# print(casino.balans)
# print(player.balans)
# casino.supract_money(100)
# player.add_money(100)
