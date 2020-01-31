km = int(input("Digite uma velocidade: "))
if km > 80:
    print("Voce foi mutado!")
    kmn = (km - 80)*7
    print("Voce deve R${:.2f}".format(kmn))
