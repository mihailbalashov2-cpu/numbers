from random import *

# Основные функции
def play():
    while True:
        # Начало
        start_game()

        # Ввод данных
        x, y = input_user()

        # Основная логика игры
        logic_game(x, y)

def start_game():
    rules = ("Правила:"'\n'
          "1.Программа загадывает число в диапозоне от x(включительно) до y(включительно)"'\n'
          "2.Необходимо угадать это число"'\n'
          "3.Диапазоны x и y вы выбираете сами."'\n'
          "4.При неправильном ответе программа подскажет 'больше' или 'меньше' ")

    while True:
        print(f'Хотите начать? {'\n'}Y-Да/N-Нет')
        chose = input()
        if yes_no(chose):
            break

def input_user():
    print('Введите значение x = ', end="")
    x = input()
    while not is_valid(x):
        print('Введите значение x = ', end="")
        x = input()
    x = int(x)
    while True:
        print('Введите значение y = ', end="")
        y = input()
        while not is_valid(y):
            print('Введите значение y = ', end="")
            y = input()
        y = int(y)
        if x <= y:
            break
        else:
            print("Значения х не может быть больше значения y")
    return x,y

def logic_game(x,y):
        print(f'Загадываю число от {x} до {y}...')
        mysterious_number = random(int(x), int(y))
        print('Готово!\n'
              'Пора угадывать!\n')

        print("Введите предпологаемое число: ", end="")
        number = input()
        while not is_valid(number):

            number = input()
        number = int(number)
        total = 1

        while number != mysterious_number:
            print(['Ваше число меньше загаданного, попробуйте еще разок',
                   'Ваше число больше загаданного, попробуйте еще разок'][number > mysterious_number])
            print("Введите предпологаемое число: ", end="")
            number = input()
            while not is_valid(number):
                print("Введите предпологаемое число: ", end="")
                number = input()
            number = int(number)
            total += 1

        print(
            f'Поздравляю!!!Число угадано!На это понадобилось: {total} {['попытка', 'попытки', 'попытки', 'попытки', "попыток"][total - 1]}')

def yes_no(n):
    if n.lower() == "y" or n.lower() == "н":
        return True
    elif n.lower() == 'n' or n.lower() == 'т':
        return quit('Всего доброго!')
    return print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n')

def random(first,last):
    return randint(first,last)

def is_valid(digit):
    if digit.isdigit():
        return True
    return print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n')

#Функции GUI
def button_click():
    start_game()
    result_text.set(start_game())