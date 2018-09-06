__author__ = 'Воронов Лев Сергеевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = 4284

divider2 = 1
i = 1
while i < 10:

    divider1 = 10**i
    result = number % divider1 // divider2

    if not result:
        break

    print(result)
    divider2 = divider1
    i += 1



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))

print('A = ', A, 'B = ', B)

C = A
A = B
B = C

print("Меняем местами:")
print('A = ', A, 'B = ', B)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Сколько вам лет? '))

if age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")