def revisar_fecha(d, m, a):
    # d, m, a = list(map(int, input().split()))

    if (a % 4 == 0 and a % 100 != 0) or (a % 4 == 0 and a % 100 == 0 and a % 400 == 0):
        leap = 1
    else:
        leap = 0
    # 30 11 1971
    # 29 2 2001

    if leap == 0 and m == 2 and (d >= 29):
        print('Fecha incorrecta')
    elif (m in [4, 6, 9, 11]) and (d > 30):
        print('Fecha incorrecta')
    elif (m not in [2, 4, 6, 9, 11]) and (d > 31):
        print('Fecha incorrecta')
    elif d < 1 or m > 12 or m < 1:
        print('Fecha incorrecta')
    else:
        print('Fecha correcta')


def main():
    n = int(input())

    for _ in range(n):
        d, m, a = list(map(int, input().split()))
        revisar_fecha(d, m, a)


if __name__ == "__main__":
    main()
