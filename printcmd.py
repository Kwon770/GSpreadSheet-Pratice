import os


def printn(string):
    print(string)
    print()


def printnn(string):
    print()
    print(string)


def inputS():
    while True:
        _input = input()

        print("Sure ? / Y or N")
        cmd = input(' ~ ')
        if cmd == "Y" or cmd == "y":
            return _input
        else:
            print("[[ RETRY ]]")
            continue


def clear():
    os.system('clear')
