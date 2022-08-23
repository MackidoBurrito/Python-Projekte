def main():
    namelist = []
    txt_file = open("Namenliste.txt", "r")
    raw_namelist = txt_file.read()
    txt_file.close()
    raw_namelist = raw_namelist.split(",")

    for i in raw_namelist:
        namelist.append(i.replace('"', ""))

    namelist.sort()
    for i in namelist:
        print(i)

    print(len(namelist))


if __name__ == "__main__":
    main()
