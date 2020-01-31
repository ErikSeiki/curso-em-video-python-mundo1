s = float(input("Digite o seu salario: "))
if s > 1250:
    a = (s * (10 / 100))
    print("Seu salario atual: R${:.2f}\nSeu aumento: R${:.2f}\nSeu novo salario: {:.2f}".format(s, a, s + a))
else:
    a = (s * (15 / 100))
    print("Seu salario atual: R${:.2f}\nSeu aumento: R${:.2f}\nSeu novo salario: {:.2f}".format(s, a, s + a))
