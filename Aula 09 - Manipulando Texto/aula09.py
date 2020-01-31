frase = "Mano do seu Cara chato"
print(frase)
print(frase[2])
print(frase[1:21])
print(frase[1:21:2])
print(frase[5:])
print(frase[:5])
print(frase[5::2])
print(frase[::2])
print(len(frase))
print(frase.count("Mano"))
print(frase.count('a', 0, 18))
print(frase.find("Cara"))
print(frase.find("cara"))
print("Mano" in frase)
print(frase.replace("chato", "babaca"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = "   Mano do ceu  "
print(frase2)
print(len(frase2))
a = frase2.strip()
print(a)
print(len(a))
b = frase2.rstrip()
print(b)
print(len(b))
c = frase2.lstrip()
print(c)
print(len(c))

print(frase.split())
frase3 = "1,2,3"
print(frase3.split(","))
print(frase3.split(",", maxsplit=1))

frase4 = frase.split()
print(frase4)
print("-".join(frase4))
print(" ".join(frase4))
print("".join(frase4))

print("")
print("""O menino quer um burrinho
para passear.
Um burrinho manso,
que não corra nem pule,
mas que saiba conversar.

O menino quer um burrinho
que saiba dizer
o nome dos rios,
das montanhas, das flores,
– de tudo o que aparecer.

O menino quer um burrinho
que saiba inventar histórias bonitas
com pessoas e bichos
e com barquinhos no mar.

E os dois sairão pelo mundo
que é como um jardim
apenas mais largo
e talvez mais comprido
e que não tenha fim.

(Quem souber de um burrinho desses,
pode escrever
para a Ruas das Casas,
Número das Portas,
ao Menino Azul que não sabe ler.)""")

print(frase.upper().count("O"))
