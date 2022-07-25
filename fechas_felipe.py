def bisiesto(anio: int):

    if anio % 100 != 0 and anio % 4 == 0:
        return True
    elif anio % 400 == 0:
        return True
    else:
        return False

def valid_fec(dia: int, mes: int, bisiesto:bool):

    if mes == 2:
        if bisiesto and 1 <= dia <= 29:
            return True
        elif 1 <= dia <= 28:
            return True
        else:
            return False
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            return True
        return False
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            return True
        return False
    else:
        return False
        
def main():
    n = int(input())
    
    for _ in range (n):
        d, m, a = list(map(int, input().split()))
        
        if valid_fec(d, m,bisiesto(a)):
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
        
        
if __name__ == "__main__":
    main()       
