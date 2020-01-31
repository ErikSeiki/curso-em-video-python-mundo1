d = int(input("Quantos dias alugados? "))
km = float(input("Quantos quilômetros rodados?"))
p = d * 60 + km * 0.15
print("você tem a pagar R${:.2f}".format(p))
