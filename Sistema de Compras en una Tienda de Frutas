estante = 0 
precioEstante = []
frutas = []
repetir = True

while repetir:

    def pagar (indice, indice2,contador1, contador2):
        precio1 = precioEstante[indice]*contador1
        precio2 = precioEstante[indice2]*contador2

        sumaTotal = precio1 + precio2
        return sumaTotal
    
    print("Cauntoas estantes deseas coloca ?")

    for i in range(estante):
        ingreso_de_frutas = input(
            f"Ingresa el nombre de fruta para el estante {i+1} :")
        while True:
            try:
                ingreso_de_precio = int(
                    input(f"Ingresa el precio para el estante {i+1} :"))
                break
            except ValueError:
                print("Error. Ingresa un numero valido ")
        print("\n")
        frutas.append(ingreso_de_frutas)
        precioEstante.append(ingreso_de_precio)

    for i in range(estante):
        print(
            f"Estante numero {i+1} se encuntra lleno de {frutas[i]} a un precio de {precioEstante[i]}\n")

    pedidoCliente = input( "Que es lo que compraras elije la fruta que deseas comprar : ")

    if pedidoCliente in frutas:
        indice = frutas.index(pedidoCliente)
        nombreFruta = frutas[indice]
        contador1 = 0
        contador2 = 0

        print(f"Exelente eleccion {nombreFruta} se encuntra en el estante {indice+1} y tine un costo de {precioEstante[indice]}")
        a = int(input(f"Cuantas piesas de {nombreFruta} compraras : "))
        contador1 += a
        while True:
            b = input("Deseas agregar otra fruta diferente a esta : ")
            if b.lower() == "si" or b.lower() == "no":
                break
            else:
               print("Respuesta inválida. Por favor, responde 'si' o 'no'.")


        if b == "Si":
            while True:
               pedidoCliente2 = input("Cual es la nueva fruta que compraras :")
               if pedidoCliente2 in frutas:
                 indice2 = frutas.index(pedidoCliente2)
                 nombreFruta2 = frutas[indice2]
                 b = int(input(f"Cuantas piesas de {nombreFruta2} compraras : "))
                 contador2 += b
                 print(
                    f"Pagaras un total de ${pagar(indice,contador1,contador2)}")
               else:
                    s = input("Fruta no existente.Preciona 1 para terminar")
                    if s == 1:
                        break
            continue

        else:
            print(f"Pagaras un total de : {pagar(indice,contador1,contador2)}")

    else:
        print("Error")
