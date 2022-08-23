def main():
    repeat = 1
    height = int(input("Wie hoch soll der Baum sein?: "))
    for x in range(height):
        if repeat >= height:
            break
        if repeat < height:
            print(" " * int((height - repeat)) + "X " * repeat)
        repeat = repeat + 1
    print(" " * (height-1) + "X")


if __name__ == "__main__":
    main()
