import math
a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"As raízes da equação são x1 = {raiz1} e x2 = {raiz2}")
elif discriminante == 0:
    raiz = -b / (2*a)
    print(f"A equação tem uma raiz real: x = {raiz}")
else:
    print("A equação não tem raízes reais, pois o discriminante é negativo.")
