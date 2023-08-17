def sumas(suma, alturas_estudiantes):
   media = (suma/altura_estudiantes)
   if (media - math.floor(media) > .6):
       return math.ceil(media)
   else:
       return math.floor(media)
   
 

import math
alturas = []
altura_estudiantes = int(input("Cuantos estudiantes habra: "))
suma = 0

for i in range(altura_estudiantes):
    a= float(input(f"Ingrese la altura de el estudiante {i+1} : "))
    alturas.append(a)
    suma += a

media = sumas(suma, altura_estudiantes)
print(f"La suma de la altura de los estudiantes es de : {suma}")
print(f"lA MEDIA DE LOS ESTUDIANTES FUE DE: {media}")

