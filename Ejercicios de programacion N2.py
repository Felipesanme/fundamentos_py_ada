#!/usr/bin/env python
# coding: utf-8

# Descripción
# 
# Los años bisiestos tienen 366 dias y son aquellos que son multiplos de 4 y no terminan con dos ceros o aquellos que despues de quitar los dos ceros del final son divisibles por 4 (divisibles por 400). Por ejemplo 1800, y 1900 no son años bisiestos, sin embargo el año 2000 si lo fue.
# 
# Entrada
# 
# La entrada consiste de numeros naturales en el rango de 1800 y 9999.
# 
# Salida
# 
# En la salida escriba una palabra que diga "si" si fue biciesto y "no" si no fue bisiesto, sin comillas.

# In[18]:


anho = int(input("Escoja un año entre 1800 y 9999 "))

while anho < 1800 or anho > 9999:
    print ("Error!")
    anho = int(input("Por favor escoja un año entre 1800 y 9999 "))

if anho % 100 == 0 and anho // 100 % 4 == 0:
    print ("El año escogido es bisiesto")
    
elif anho % 100 != 0 and anho % 4 == 0:
    print ("El año escogido es bisiesto")

else:
    print ("El año escogido no es bisiesto")
    
    
    
    


# Descripción
# 
# Escriba un programa que lee tres numeros enteros separados por un espacio y los imprima en una linea separados por un espacio en forma ordenada de menor a mayor.
# 
# Entrada
# 
# La entrada consiste de tres números enteros separados por un espacio.
# 
# Salida
# 
# La salida consiste de los números impresos de menor a mayor.
# 
# Ejemplo Entrada
# 
# 3 1 2
# 
# Ejemplo Salida
# 
# 1 2 3

# In[11]:


print ("Ingrese tres números enteros separados por un espacio")
num = input("ingrese el número ")

print ("los números ingresados son ",num)

primero = int(num[0])
segundo = int(num[2])
tercero = int(num[4])

mayor = max(primero,segundo,tercero)
menor = min(primero,segundo,tercero)   

if primero < segundo < tercero or tercero < segundo < primero:
    inter = segundo  
elif primero < tercero < segundo or segundo < tercero < primero:
    inter  = tercero
else:
    inter = primero
    
print("ahora se mostrarán los 3 números organizados de mayor a menor ",mayor,inter,menor)

# print("ahora se mostrarán los 3 números organizados de mayor a menor")


# In[ ]:


x = "1 3 5"
print(int(x[0]))


# In[ ]:




