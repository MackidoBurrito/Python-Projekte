def num(num):
    max_number = {}

    def name(a_func):
        def randomizer():
            numb = num
            x = 0
            while 0 < numb:
                max_number[x] = x
                x += 1
                numb -= 1
            x = 0
            for i in max_number:
                x += 1
                return max_number[x]
            print(max_number)
            print(max_number[0])
            print(max_number[1])
            print(max_number[2])
            print(max_number[3])
            a_func()
        return randomizer
    return name


@num(5)
def printer():
    print("Hallo")


def main():
    printer()


if __name__ == "__main__":
    main()
