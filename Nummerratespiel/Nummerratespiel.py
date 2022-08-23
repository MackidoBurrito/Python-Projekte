import random


def ratespiel():
    zahlenreichweite = input("Zahlenreichweite festlegen: ")
    zahlenreichweite = int(zahlenreichweite)
    if zahlenreichweite <= 1:
        print("Bitte höhere Zahl auswählen")
        exit()
    ergebniss = random.randrange(1, zahlenreichweite + 1)
    zähler = 0
    while True:
        eingabe = input("Bitte Zahl eingeben: ")
        eingabe = int(eingabe)
        if ergebniss == eingabe:
            print("*****Herzlichen Glückwunsch*****")
            break
        if ergebniss < eingabe:
            print("Die gesuchte Zahl ist niedriger")
        if ergebniss > eingabe:
            print("Die gesuchte Zahl ist höher")
        if ergebniss != eingabe:
            zähler = zähler + 1
        if zähler >= 5:
            print("Versuche aufgebraucht")
            break


def wiederspielloop():
    while True:
        ratespiel()
        wiederholung = input("Nochmal spielen (ja oder nein?): ")
        if wiederholung == "nein" or wiederholung == "Nein":
            print("Danke fürs spielen")
            break
        if wiederholung != "nein" and wiederholung != "Nein":
            if wiederholung != "ja" and wiederholung != "Ja":
                print("Falsche Eingabe")
                break


if __name__ == "__main__":
    wiederspielloop()
