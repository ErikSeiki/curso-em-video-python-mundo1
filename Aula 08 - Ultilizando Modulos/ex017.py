import math

co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hp = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))

hp2 = (co ** 2 + ca ** 2) ** (1 / 2)
print("A hipotenusa é: {} ou {}".format(hp, hp2))
print("Com função: {}".format(math.hypot(co, ca)))
