from math import ceil, floor, trunc, sqrt, factorial
import random

n = float(input('Digite um numero: '))
n1 = float(input('Digite um numero decimal: '))
print('Arredondamento para cima: {}'.format(ceil(n1)))
print('Arredondamento para baixo: {}'.format(floor(n1)))
print('Corta numeros decimais: {}'.format(trunc(n1)))
print('Elevação: {}'.format(pow(n, 2)))
print('Raiz quadrada: {}'.format(sqrt(n)))
print('Fatorial: {}'.format(factorial(n)))
print()
n2 = random.random()
print(n2)
n2 = random.randint(0, 10)
print(n2)
