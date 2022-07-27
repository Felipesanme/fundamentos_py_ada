
def promedio(n_est:int, verbales:list, numericas:list) -> int:
    est_deb_pro = 0
    i = 0
    j = 0
    suma = 0
    prom = 0
    for i in range(n_est):
        suma = suma + verbales[i]+ numericas[i]
        i =+ 1

    prom = suma/n_est
    # print(prom)

    for j in range(n_est):
        if (verbales[j]+ numericas[j]) < prom:
            est_deb_pro += 1
    print (est_deb_pro)

def main():

    n = int(input())  # casos de prueba

    for _ in range(n):

        n_est = int(input()) #número de estudiantes

        verbales = list(map(int, input().split())) #notas verbales
        numericas = list(map(int, input().split())) #notas verbales

        promedio (n_est,verbales,numericas)

if __name__ == "__main__":
    main()