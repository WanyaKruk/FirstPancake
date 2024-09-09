# -*- coding: utf-8 -*-
"""lesson1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XsjzwfFlIBpftH8MeHxO2ZZtPyj78JRZ
"""

# Введение в язык программирования Python

print("Привет, МИР!")

# Переменные и операции
x = 3
y = 2

# условные операторы
sum = x + y
if x > y:
    print("x больше y")
elif x < y:
    print("x меньше y")
else:
    print("x равно y")
print(sum)

# циклы
for i in range(5):
    print(i)
print(i)

while x < 20:
    print(x)
    x += 3

# Функции:
def xxx(a, b):
    return (2*a)/b+1
xxx(20, 10)

xxx(10, 4)

# Списки:
numbers = [1, 2, 3, 4, 6]
numbers

firstnumber = numbers[3]
firstnumber

numbers.append(7)

numbers

numbers

# Строки
message = "Привет, мир!"

# Срез строки
partof_message = message[0:6]
partof_message

# Словари (ассоциативные массивы):
person = {"имя": "Андрей", "возраст": 30, "город": "Минск"}
name = person["имя"]
city = person["город"]
age = person["возраст"]
city, name, age

# Менеджер пакетов. Виртуальное окружение
# В гугл колаб уже есть среда выполнения



!pip list



!pip freeze > requirements.txt

import pandas as pd

