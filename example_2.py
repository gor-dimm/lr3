# Составить UML-диаграмму деятельности и программу для решения задачи: склавиатуры вводится номер месяца от 1 до 12,
# необходимо для этого номера месяца вывести наименование времени года
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))
if n == 1 or n == 2 or n == 12:
    print("Зима")
elif n == 3 or n == 4 or n == 5:
    print("Весна")
elif n == 6 or n == 7 or n == 8:
    print("Лето")
else:
    print("Ошибка!", file=sys.stderr)
exit(1)
