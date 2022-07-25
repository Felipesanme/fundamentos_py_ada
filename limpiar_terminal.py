import os
import readchar


def func(n:int):
    k = readchar.readkey()
    cont = 1
    while cont <= 50:
        k = readchar.readkey()
        print(cont)
        os.system('cls' if os.name == 'nt' else 'clear')
        cont += 1

def main():

    func(0)

if __name__ == "__main__":
    main()
