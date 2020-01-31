n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
# outra forma de elevar pow(n1, n2)
ra = n1 ** (1 / n2)
di = n1 // n2
r = n1 % n2

print("Soma de {} e {} é: {}".format(n1, n2, s))
print("Subtração de {} e {} é: {}".format(n1, n2, su))
print("Mulplicação de {} e {} é: {}".format(n1, n2, m))
print("Divisão de {} por {} é: {:.2f}".format(n1, n2, d))
print("Eleveção de {} ao {} é: {}".format(n1, n2, p))
print("Raiz de {} ao {} é: {}".format(n1, n2, ra))
print("Divisão Inteira de {} por {} é: {}".format(n1, n2, di))
print("Resto da divisão de {} por {} é: {}".format(n1, n2, r))

nome = input("Digite seu nome: ")
print(nome * 5)
print("Olá! {:20}!".format(nome))
print("Olá! {:>20}!".format(nome))
print("Olá! {:<20}!".format(nome))
print("Olá! {:^20}!".format(nome))
print("Olá! {:_^20}!".format(nome))
print("Acabou", end=" ")
print("essa poha\nSera?")
