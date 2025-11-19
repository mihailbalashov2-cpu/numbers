import func as f
import time

# Приветсвие
print("-" * 32,"Добро пожаловать в 'Угадайку'", "-" * 32, sep='\n')

#Начало
print(f"Правила:"'\n'
      "1.Программа загадывает число в диапозоне от x(включительно) до y(включительно)"'\n'
      "2.Необходимо угадать это число"'\n'
      "3.Диапазоны x и y вы выбираете сами."'\n'
      "4.При неправильном ответа программа подскажет 'больше' или 'меньше' ")

while True:
    print(f'Хотите начать? {'\n'}Y-Да/N-Нет')
    chose = input()
    if f.yes_no(chose):
        break
    elif f.yes_no(chose) == 0:
        quit('Хорошо, если передумаете напиши /start')
    else:
        print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n')

#Ввод данных
print('Введите значение x = ', end="")
x = int(input())
print('Введите значение y = ', end="")
y = int(input())

#Основная логика игры
print(f'Загадываю число от {x} до {y}...')
mysterious_number = f.random(x,y)
print(f'Готово!\n'
      f'Пора угадывать число')

number = int(input())
total = 1
while number != mysterious_number:
    print(["Меньше", "Больше"] [number < mysterious_number])
    number = int(input())
    total += 1

delay = 10
print(f'Поздравляю!!!Число угадано!На это понадобилось: {total} {['попытка','попытки','попытки','попытки',"попыток"] [total - 1]}')
time.sleep(delay)
