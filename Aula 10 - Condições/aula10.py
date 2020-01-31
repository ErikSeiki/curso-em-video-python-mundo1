ac = int(input("Digite quantos anos seu carro tem: "))
if ac <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")
print("--Fim--")

tem = int(input("Digite quantos anos seu carro tem: "))
print("Seu carro é novo" if tem <= 3 else "Seu carro é velho")
print("--Fim--")

nome = input("Qual é o seu nome: ")
print("Bom dia {}".format(nome))
if nome == "Erik":
    print("Que nome bonito")
else:
    print("Seu nome é normal")
print()
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("Sua media foi de {:.1f}".format(m))
if m >= 6:
    print("Sua media foi boa. Parabens!")
else:
    print("Sua media foi ruim. Estude mais!")