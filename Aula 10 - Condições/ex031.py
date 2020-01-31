km = float(input("Digite uma distancia: "))
if km <= 200:
    print("A viagem custa R${:.2f}".format(km * 0.5))
else:
    print("A viagem custa R${:.2f}".format(km * 0.45))
