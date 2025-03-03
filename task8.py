import math as m
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))
print(m.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * (180 / m.pi))
print(m.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * (180 / m.pi))
print(m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * (180 / m.pi))
