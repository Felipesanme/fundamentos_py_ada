def comprobacion_cadena(cadena_uno:str,cadena_dos:str) -> str:
  for i in range (0,9):
    if cadena_uno [i] == cadena_dos[i]:
      return ("con la misma letra")

comprobacion_cadena("perro","pera")

# cadena = "Perro"
# print (cadena(2))