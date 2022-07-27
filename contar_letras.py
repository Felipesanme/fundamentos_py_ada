
def contar(letra:str, cadena:str) -> int:
    num_vec = 0
    tup_cadena = tuple(cadena)
    for _ in range(len(cadena)):
        if letra == tup_cadena[_]:
            num_vec += 1
    print(num_vec)

def main():

    letra = input()
    cadena = input()

    contar (letra,cadena)

if __name__ == "__main__":
    main()