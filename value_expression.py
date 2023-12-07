#Подключаем модуль math для того, чтобы использовать модуль и корень числа
import math


#Создаем переменную x
x = None

#Вводим значение переменной x и проверяем его на то, чтобы оно было числом
while x == None:
    try:
        x = float(input("Введите переменную x: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте ввести ещё раз переменную x")


#Создаем переменную y(x)
y = None

#Проверяем делитель дроби на то, чтобы он был отличен от нуля и подкоренное выражение не было меньше нуля
try:
    y = math.fabs(2 * x**3 + 6 * x**2 - math.sqrt(x)) + 3 / (2 * x**3 + 6 * x**2 - math.sqrt(x))
except ZeroDivisionError:
    print("Знаменатель дроби равен нулю. На ноль делить нельзя")
except ValueError:
    print("Нельзя извлекать из под корня чётной степени отрицательное число")


#Если все предыдущие условия соблюдены, то выводим y(x)
if y != None:
    if y == int(y):
        y = int(y)

    print(y)