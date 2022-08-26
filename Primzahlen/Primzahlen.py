def main():
    usernumber = input("Bis wohin sollen Primzahlen berechnet werden: ")
    if not usernumber.isnumeric():
        print("Falsche Eingabe. Bitte Zahl eingeben")
        return
    else:
        usernumber = int(usernumber)
    if usernumber >= 2:
        numberrange = range(2, usernumber + 1, 1)
    else:
        print("Bitte Zahl über 1 eingeben")
        return
    for number in numberrange:
        i = 2
        isprime = True
        while i <= number**0.5:
            divisible = number % i == 0
            i += 1
            if divisible:
                isprime = False
                break
        if isprime:
            print(number)


if __name__ == "__main__":
    main()
