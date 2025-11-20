import func as f

# Приветсвие
print("-" * 32,"Добро пожаловать в 'Угадайку'", "-" * 32, sep='\n')

# Начало
f.start_game()

while True:
    # Ввод данных
    x, y = f.input_user()

    # Основная логика игры
    f.logic_game(x, y)

    #Повтор игры
    print("Вы хотите сыграть еще раз?\nY-Да/N-Нет")
    f.yes_no(input())