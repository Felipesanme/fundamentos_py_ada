import sys

def main():
    for line in sys.stdin:
        _, x = list(map(int, line.split()))  # la barra baja _ me ayuda a ignorar valores de retorno
        coefs = list(map(int, input().split()))

    #         res = 0
    #         exp = 0
    #         for n in reversed(range(len(coefs))):
    #             res += coefs[n]*(x**n)
    #             exp += 1

    for n, c in enumerate(reversed(coefs)):
        res += c * (x ** n)

    print(float(res))

if __name__ == "__main__":
    main()