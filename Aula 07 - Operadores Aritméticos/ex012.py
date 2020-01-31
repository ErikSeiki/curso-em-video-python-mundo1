p = float(input("Digite o preço R$"))
pr = int(input("Digite um porcentagem do desconto: "))
d = p*pr/100
pcd = p - d
print("Preço com disconto é de R${:.2f}".format(pcd))
