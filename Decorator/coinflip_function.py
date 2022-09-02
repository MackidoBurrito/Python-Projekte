import random


def name(a_func):
    coinflip = {}

    def randomizer():
        if random.randrange(0, 2) == 0:
            coinflip["0"] = 1
        if "0" not in coinflip:
            result = "Glück gehabt"
        else:
            result = "ERROR!!!!!!!!!!"
        a_func(result)
    return randomizer


@name
def printer(result):
    print(result)
    return


def main():
    printer()
    printer()
    printer()
    printer()
    printer()
    printer()
    printer()
    printer()
    printer()
    printer()


if __name__ == "__main__":
    main()
