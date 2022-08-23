import random


def main():
    while True:
        x = input("Bitte eingeben wie viele Seiten geworfen werden: ")
        if not x.isnumeric():
            print("Bitte Zahl eingeben")
            break
        x = int(x)
        if x <= 0:
            print("Zu kleine Eingabe")
            break
        ergebniss = random.randrange(1, x+1)
        print(ergebniss)
        y = input("Weiter würfeln(ja oder nein): ")
        if y == "nein" or y == "Nein":
            print("Danke fürs spielen")
            break
        if y != "nein" and y != "Nein" and y != "ja" and y != "Ja":
            print("Falsche Eingabe")
            break


if __name__ == "__main__":
    main()
