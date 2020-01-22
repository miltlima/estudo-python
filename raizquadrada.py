import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b ** 2 - 4*a*c)
# Formula de bhaskara
if delta == 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    print("A primeira raiz é ", x1)
else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("A primeira raiz é ", x1)
        print("A segunda raiz é ", x2)
