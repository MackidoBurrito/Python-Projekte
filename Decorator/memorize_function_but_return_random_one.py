import random


def name(a_func):
    results = []

    def randomizer(showlist=False):
        if "Nice" not in results and "Quatsch" not in results:
            results.append("Nice")
        else:
            results.append("Quatsch")
        a_func(random.choice(results))
        if showlist:
            print(results)
    return randomizer


@name
def printer(results):
    print(results)
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
    printer(showlist=True)


if __name__ == "__main__":
    main()
