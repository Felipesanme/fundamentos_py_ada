#!/usr/bin/env python
# coding: utf-8

# Problema # 1
# 
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# 
# 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# 
# 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5bs y si es mayor de 18 años, 10bs.
# 

# In[2]:


edad = int(input("Por favor ingrese la edad del cliente"))

if edad < 4:
    print ("La entrada es gratis!")
elif 4 <= edad <= 18:
    print ("La entrada le cuesta 5 bs")
else:
    print("La entrada le cuesta 10 bs")


# Problema # 2
# 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura que sea el número introducido.

# In[11]:


altura = int(input("Ingrese la base del triángulo rectángulo "))

for i in range (0,altura+1):
    print ("*"*i)
    if i == 20:
        break





