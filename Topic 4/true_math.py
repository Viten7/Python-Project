# Домашняя работа по уроку "Модули и пакеты"

# результат при делении на 0 будет стремиться к бесконечности

from math import inf
def divide(first, second):
    if second != 0:
        return first / second
    else:
        return inf