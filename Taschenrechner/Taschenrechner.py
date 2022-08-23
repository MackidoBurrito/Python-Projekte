def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):

    return x / y


while True:
    print("Methode wählen")
    print("1.Addieren")
    print("2.Subtrahieren")
    print("3.Multiplizieren")
    print("4.Dividieren")
    Methode = input("Bitte Rechenart wählen(1,2,3,4): ")

    if Methode in ("1", "2", "3", "4"):
        num1 = float(input("Bitte erste Zahl eingeben: "))
        num2 = float(input("Bitte zweite Zahl eingeben: "))

        if Methode == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        if Methode == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        if Methode == "3":
            if num1 and num2 == 0:
                print("Falsche Eingabe")
                break
            else:
                print(num1, "*", num2, "=", multiply(num1, num2))

        if Methode == "4":
            if num1 and num2 == 0:
                print("Falsche Eingabe")
                break
            else:
                print(num1, "/", num2, "=", divide(num1, num2))

        Wiederholung = input("Nochmal rechnen? (ja oder nein): ")
        if Wiederholung == "nein":
            print("Auf Wiedersehen")
            break

    else:
        print("Falsche Eingabe")
