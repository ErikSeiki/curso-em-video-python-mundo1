m = float(input("Digite uma quantidade me metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(
    "Quilômetros: {} km\nHectômetros: {} hm\nDecâmetro: {} dam\nMetros: {}\nDecímetro: {} dm\nCentímentros: {} cm\nMilímentros {} mm".format(
        km, hm, dam, m, dm, cm, mm))
