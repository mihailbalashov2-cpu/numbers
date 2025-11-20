from random import *

# Основные функции
def yes_no(n):
    if n.lower() == "y" or n.lower() == "н":
        return True
    elif n.lower() == 'n' or n.lower() == 'т':
        return quit('Хорошо, если передумаете напишите /start')
    return print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n')


def random(first,last):
    return randint(first,last)

def is_valid(digit):
    if digit.isdigit():
        return True
    return ValueError(print("-" * 27,'Введите корректные значения', "-" * 27, sep='\n'))