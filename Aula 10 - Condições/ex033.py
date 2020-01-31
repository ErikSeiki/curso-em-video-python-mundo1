n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3
M = n1
if n2 > n1 and n2 > n3:
    M = n2
if n3 > n1 and n3 > n2:
    M = n3
print("O maior numero é {} e o menor é {}".format(M, m))
print()
