

calificaciones = []
estudiantes = []


bucle = True
while bucle:
    print("Bienvenido")
    res1 = input(str("Deseas agregar un Estudiante S/N? :  ")).capitalize()
    if (res1 == "S"):
        while True:
             nombre_estudiante = input("Ingresa el nombre del estudiante que deseas agregar : ")
             estudiantes.append(nombre_estudiante)
             
             while True:

                 r = input("Deseas agregar otro Estudiante ? S/N : ").capitalize()
                 if (r == "S"):
                   break
                 elif (r == "N"):
                   break
                 else:
                      print("Ingresa una opcion valida")
             if(r == "N"):
                 break
             else:
                 continue
    if(r == "N"):
        break                
             
        

res2 = input("Desas buscar un alumno S/N: ").capitalize()
if(res2 == "S"):
    r = input("Ingresa el nombre de el alumno : ")
    for nombre_estudiante in estudiantes:
        if(r == nombre_estudiante):
            print(nombre_estudiante)
    

    

       


    

