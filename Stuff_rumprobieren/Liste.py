Liste1 = ["Hallo", "Tschüss", "Moin", "Mahlzeit", "Hola", "Bye"]
Liste2 = (("Halloooooo", "X"))
Liste3 = ["Nochmal hallo"]
print(Liste1)
print(len(Liste1))
print(type(Liste1))
print(Liste2)
print(Liste1[1])
print(Liste1[2:4])
print(Liste1[:3])
print(Liste1[2:])
if "Hallo" in Liste1:
    print("Hallo is in this list")
if "Ciao" not in Liste1:
    print("Ciao ist not in this list")
Liste1[1] = "Ciao"
print(Liste1)
Liste1[6:8] = "Hallihallo", "Bonjour"
print(Liste1)
Liste1.insert(8, "Tschöö")
print(Liste1)
Liste1.append("Mir gehen langsam die Begriffe aus")
print(Liste1)
Liste1.extend(Liste3)
print(Liste1)
Liste1.remove("Nochmal hallo")
Liste1.pop(9)
print(Liste1)
Liste3.clear()
print(Liste3)
for x in Liste1:
    print("XXXXXXXX")
