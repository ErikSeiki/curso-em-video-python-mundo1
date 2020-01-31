n = str(input("Digite o nome completo: ")).strip()
ns = n.split()
un = len(ns)
print("Seu primeiro nome: {} \nSeu ultimo nome: {}".format(ns[0], ns[un-1]))

