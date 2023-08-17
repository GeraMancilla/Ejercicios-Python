# TITULO
print("AEROPUERTO DIDA")

# Consturctor para retener los datos de los objetos


class Examen:
    def __init__(self, costo, titulo, existencias):
        self.costo = costo
        self.titulo = titulo
        self.existencias = existencias
    # Funcion paa calcular el cambiou

    def total(self, total_objetos):
        return self.cost2o * total_objetos

    def cambio(self, efectivo, total_objetos):
        total = self.total(total_objetos)
        return efectivo - total


# Registro los datos de los objetos
print("AREA DE REGISTROS\n\n")
print("REGISTRO PERIODICOS\n")
costo_periodico = int(input("Ingresa el costo : "))
titulo_periodico = input("Ingresa el titulo : ").strip().title()
existencias_periodico = int(input("Numero de existencia de el elemento  :"))
periodico = Examen(costo_periodico, titulo_periodico, existencias_periodico)
print("")
print("REGISTRO REVISTAS\n")
costo_revista = int(input("Ingresa el costo : "))
titulo_revista = input("Ingresa el titulo : ").strip().title()
existencias_revista = int(input("Numero de existencia de el elemento  :"))
revista = Examen(costo_revista, titulo_revista, existencias_revista)
print("")
print("REGISTRO LIBROS\n")
costo_libro = int(input("Ingresa el costo : "))
titulo_libro = input("Ingresa el titulo : ").strip().title()
existencias_libro = int(input("Numero de existencia de el elemento  :"))
libro = Examen(costo_libro, titulo_libro, existencias_libro)
print("")
# Ciclo wile para tener la oportunidad de regresar al menu principal
while True:
    # Mostramos el Menu
    print("DISPENSADOR\n",
          "ELIGE LA OPCION QUE DESEAS REALIZAR \"Tecleando el numero correspondiente\"\n")
    print("1. EXTRAER PERIODICO\n", "2. EXTAER REVISTA\n", "3. EXTRAER LIBRO\n")
    res = int(input("Ingresa tu respuesta aqui : "))
    if (res == 1):

        # Muestro los datos de el objeto periodico
        print("Costo de la Periodico : ", periodico.costo)
        print("Titulo de la Periodico", periodico.titulo)
        print("Existencias : ", periodico.existencias)

        # While True para tner la oportunidad de volver si agrega un monto menor al costo de el objeto
        while True:
            efectivo = int(input(
                "Para continuar con tu compra deberas ingresar el efectivo con el que cuentas: $"))
            if (efectivo > periodico.costo):
                cambio = periodico.cambio(efectivo)
                print("Gracias por su compra.Su cambio es:", cambio)
                periodico.existencias -= 1
                break
            else:
                print("Agrega un monto valido")
                break

        # Pregunto al usuario si desea regresar  al menu principal
        decicion = int(
            input("Deseas regresar(Preciona 4 para regresar y 5 para terminar)"))
        if (decicion == 4):
            continue
        else:
            break
    elif (res == 2):
        # Muestro los datos de el objeto revista
        print("Costo de Revista: ", revista.costo)
        print("Titulo de Revista: ", revista.titulo)
        print("Existencias : ", revista.existencias)

        # While True para tner la oportunidad de volver si agrega un monto menor al costo de el objeto
        while True:
            total_objetos = int(input("Cuantas unidades deseas comprar: "))
            efectivo = int(input(
                "Para continuar con tu compra deberas ingresar el efectivo con el que cuentas: $"))
            if (efectivo > revista.total(total_objetos)):
                cambio = revista.cambio(efectivo, total_objetos)
                print("Gracias por su compra.Su cambio es:", cambio)
                revista.existencias -= total_objetos
                break
            else:
                print("Agrega un monto valido")

        # Pregunto al usuario si desea regresar
        decicion = int(
            input("Deseas regresar(Preciona 4 para regresar y 5 para terminar)"))
        if (decicion == 4):
            continue
        else:
            break

    elif (res == 3):
        # Muestro los datos de el objeto libro
        print("Costo de Libro: ", libro.costo)
        print("Titulo de Libro: ", libro.titulo)
        print("Existencias : ", libro.existencias, "\n")
        # While True para tner la oportunidad de volver si agrega un monto menor al costo de el objeto
        while True:
            efectivo = int(input(
                "Para continuar con tu compra deberas ingresar el efectivo con el que cuentas: $"))
            if (efectivo > libro.costo):
                cambio = libro.cambio(efectivo)
                print("Gracias por su compra.Su cambio es:", cambio)
                libro.existencias -= 1
                break
            else:
                print("Agrega un monto valido")
        # Pregunto al usuario si desea regresar al menu principal
        decicion = int(
            input("Deseas regresar(Preciona 4 para regresar y 5 para terminar)"))
        if (decicion == 4):
            continue
        else:
            break
