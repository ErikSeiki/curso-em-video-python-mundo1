import random
import time

na = random.randint(0, 5)
print("-=-"*20)
print("Estou pensando em um numero de 0 a 5. Tente adivinhar...")
print("-=-"*20)
ne = int(input("Em que numero pensei? "))
print("Processando...")
time.sleep(2)
if na == ne:
    print("Parabens! Voce ganhou")
else:
    print("Eu ganhei, pensei no numero {}, não numero {}".format(na,ne))
