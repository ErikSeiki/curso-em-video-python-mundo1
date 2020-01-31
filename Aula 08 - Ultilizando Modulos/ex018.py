import math

n = float(input("Digite um angulo: "))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print("O seno de {} é {:.2f}, coseno {:.2f} e a tangete é {:.2f}".format(n, sen, cos, tg))