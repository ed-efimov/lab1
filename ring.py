#Подключаем модуль math для того, чтобы использовать число Пи
import math


#Создаём переменную для внешнего радиуса кольца
radius_outside = None

#Вводим значение внешнего радиуса кольца и проверяем его на то, чтобы оно было числом и не меньше нуля
while radius_outside == None:
    try:
        radius_outside = float(input("Введите внешний радиус кольца: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте ввести ещё раз внешний радиус кольца")
        continue
    if radius_outside < 0:
        radius_outside = None
        print("Вы ввели число меньше нуля. Попробуйте ввести ещё раз внешний радиус кольца")


#Создаём переменную для внутреннего радиуса кольца
radius_inside = None

#Вводим значение внутреннего радиуса кольца и проверяем его на то, чтобы оно было числом, не меньше нуля и не больше внешнего радиуса
while radius_inside == None:
    try:
        radius_inside = float(input("Введите внутренний радиус кольца: "))
    except ValueError:
        print("Вы ввели не число. Попробуйте ввести ещё раз внутрений радиус кольца")
        continue
    if radius_inside < 0:
        radius_inside = None
        print("Вы ввели число меньше нуля. Попробуйте ввести ещё раз внешний радиус кольца")
        continue
    if radius_inside > radius_outside:
        radius_inside = None
        print("Вы ввели значение радиуса внутреннего кольца больше чем внешнего. Попробуйте ввести ещё раз внешний радиус кольца")


#Считаем площадь кольца
square_ring = math.pi * (radius_outside ** 2 - radius_inside ** 2)


#Выводим площадь кольца
print("Площадь кольца:", square_ring)