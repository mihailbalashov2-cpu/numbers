from random import *

# Основные функции
def yes_no(n):
    if n.lower() == "y":
        return True
    elif n.lower() == 'n':
        return quit('Хорошо, если передумаете напишите /start')
    return print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n')


def random(first,last):
    return randint(first,last)

def is_valid():
    pass