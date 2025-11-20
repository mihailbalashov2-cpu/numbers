import time

import func as f
from func import is_valid

# Приветсвие
print("-" * 32,"Добро пожаловать в 'Угадайку'", "-" * 32, sep='\n')

#Начало
print(f"Правила:"'\n'
      "1.Программа загадывает число в диапозоне от x(включительно) до y(включительно)"'\n'
      "2.Необходимо угадать это число"'\n'
      "3.Диапазоны x и y вы выбираете сами."'\n'
      "4.При неправильном ответе программа подскажет 'больше' или 'меньше' ")

while True:
    print(f'Хотите начать? {'\n'}Y-Да/N-Нет')
    chose = input()
    if f.yes_no(chose):
        break

#Ввод данных
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
    if x < y:
        break
    else:
        print("Значения х не может быть больше значения y")

#Основная логика игры
print(f'Загадываю число от {x} до {y}...')
mysterious_number = f.random(int(x),int(y))
print(f'Готово!\n'
      f'Пора угадывать!\n')

print("Введите предпологаемое число: ", end="")
number = input()
while not is_valid(number):
    print("Введите предпологаемое число: ", end="")
    number = input()
number = int(number)
total = 1

while number != mysterious_number :
    print(['Ваше число меньше загаданного, попробуйте еще разок', 'Ваше число больше загаданного, попробуйте еще разок'] [number < mysterious_number])
    number = input()
    while not is_valid(number):
        print("Введите предпологаемое число: ", end="")
        number = input()
    number = int(number)
    total += 1

delay = 10
print(f'Поздравляю!!!Число угадано!На это понадобилось: {total} {['попытка','попытки','попытки','попытки',"попыток"] [total - 1]}')
time.sleep(delay)
