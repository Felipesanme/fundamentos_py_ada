texto = "variable tipo string"
entero = 6
decimal = 3.14
booleano = True

## Punto 1
concatenado = texto + " " + str(entero) + " " + str(decimal) + " " + str(booleano)

## Punto 2
## El limite de enteros según la documentación consultada es de 2^63-1 que sería un número de 64 bit equivalente a 9223372036854775807.

## Para los números punto flotante (float) se tiene que hay una diferencia en los décimales debido a qué python utiliza la base 2 (binaria) para la representación de los números, entonces apartir del decimal 17, encontramos diferencia en la mayoría de los números con decimales y su representación en python.

##Punto 3

suma_n_pares = entero*(entero+1)

##Punto 4

print(suma_n_pares)
print(concatenado)