score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10
}
while True:
    endscore = 0
    userword = input("Bitte Wort eingeben: ").lower()
    for x in userword:
        worth = score.get(x)
        if worth is None:
            worth += 0
        endscore = endscore + worth
    print(endscore)
    repeat = input("Noch ein Wort berechnen(ja oder nein): ").lower()
    if repeat != "nein" and repeat != "ja":
        print("Fehlerhafte Eingabe")
        break
    if repeat == "nein":
        print("Auf Wiedersehen")
        break
