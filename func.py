from random import *

# Основные функции
def yes_no(n):
    if n.lower() == "y":
        return True
    elif n.lower() == 'n':
        return False
    else:
        return None

def random(first,last):
    return randint(first,last)