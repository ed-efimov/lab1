#Создаём переменную числа
number = None

#Вводим число и проверяем его на то, чтобы оно было целым числом
while number == None:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        number = None
        print("Вы ввели не целое число или вообще не число. Попробуйте ещё раз ввести целое число")


#Выводим следующее и предыдущее числа
print("The next number for the number ", number, " is ", number + 1, '.', sep='')
print("The previous number for the number ", number, " is ", number - 1, '.', sep='')