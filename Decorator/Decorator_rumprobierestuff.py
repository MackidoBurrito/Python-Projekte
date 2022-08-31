def wrapper(a_func):
    def wrap():
        for x in range(0, 5):
            print("Hallo")
            a_func()
            print("Tschöö")
    return wrap


@wrapper
def beispiel():
    print("Alles klaro?")


@wrapper
def anderes_beispiel():
    print("Burr")
    print("Burr")


beispiel()
anderes_beispiel()
