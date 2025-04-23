"""Решение квадратного уравнения"""

a = int(input("Введите коэффициент a"))
b = int(input("Введите коэффициент b"))
c = int(input("Введите коэффициент c"))

disk = b**2 - 4 * a * c
if disk > 0:
    x1 = (-b + disk**0.5) / 2 * a
    x2 = (-b - disk**0.5) / 2 * a
    print("x1=", x1, "x2=", x2)
if disk == 0:
    x = -b/2*a
    print('x=', x)
if disk < 0:
    print("Корней нет")
