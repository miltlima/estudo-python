import math
x1 = int(input("valor de x:"))
y1 = int(input("valor de y:"))
x2 = int(input("valor de x:"))
y2 = int(input("valor de y:"))
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
if d >= 10:
    print("longe")
else:
    print("perto")