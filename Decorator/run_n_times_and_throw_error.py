
def name(num):
    numb = {}

    def counter(a_func):

        def func():
            if "0" not in numb:
                numb["0"] = 1
            elif num > numb["0"]:
                numb["0"] += 1
            else:
                print("FEHLER. Maximum erreicht")
                return None
            a_func()
        return func
    return counter


@name(6)
def printer():
    print("Hallo")


def main():
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
