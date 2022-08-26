def main():
    Primzahlen = [1]
    Eingabezahl = input("Bis wohin sollen Primzahlen berechnet werden: ")
    if not Eingabezahl.isnumeric():
        print("Falsche Eingabe. Bitte Zahl eingeben")
    else:
        Eingabezahl = int(Eingabezahl)
        Eingabezahl -= 1
        x = 1
        while x <= Eingabezahl:
            x += 1
            Primzahlen.append(x)
    print(Primzahlen)
    return 5 % 2 == 0
    print(Primzahlen)


main()
