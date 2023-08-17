def datos(aparadores,precio,cantidad,c):
    indice = aparadores.index(c)
    mostrarNombres = aparadores[indice]
    precioPrenda = precio[indice]
    cantidadPrenda = cantidad[indice]
    return mostrarNombres,precioPrenda,cantidadPrenda

def cambio(efectivo):
    a = efectivo - cuentaTotal
    return a


#Codigo Principal
numAparadores = 2
aparadores = []
precio = []
cantidad = []
cuentaTotal = 0


for i in range (numAparadores):
    

    while True:
        try:
            a = input(f"\nIngresa el nombre de la prenda para el apareador {i+1}: ")
            c = int(input(f"Cuantas prendas tendra el aparador {i+1}: "))
            b = float(input(f"Precios para las prendas del aparador {i+1}: "))

            aparadores.append(a)
            precio.append(b)
            cantidad.append(c)
            break
        except ValueError:
            print("Dato no permitido")
            continue

while True:   
    
    print("\nCATALOGO DE PRENDAS\n")
    for i in range(numAparadores):
        print(f"Aparador: {i+1}\nPrenda : {aparadores[i]}\nPrecio: {precio[i]}\nCantidad : {cantidad[i]}\n")
        

    c = input("\nQue prenda deseas comprar : ")
        


    if c in aparadores : 
        mostrarNombres, precioPrenda, cantidadPrenda = datos(aparadores, precio, cantidad, c)
        if cantidadPrenda > 0:
            cantidad[aparadores.index(c)] -= 1
            cuentaTotal += precioPrenda
            respuestaCliente = input("Deseas comprar otra prenda ? : ").lower()
            if respuestaCliente == "si":
                continue
            elif respuestaCliente == "no":
                break
            else:
                print("Respuesta inválida. Ingresa 'si' o 'no'.")
            
            
        else:
            print("No hay prendas disponibles")
            continue
    else:
        print("Prenda no escontrada :")
  


print(f"Total a pagar : {cuentaTotal}")
    #Sistema de cambio al ususario 

    
while True:
    try:
        efectivo = float(input("Ingresa el monto con el que culminara la compra :"))
        if efectivo < 0 or efectivo < cuentaTotal:
            print("Monto insuficiente")
            continue
        else:
            print(f"Monto: {efectivo}\nCambio:{cambio(efectivo)}")
            print("Gracias por tu compra ")
            break
    except(ValueError,TypeError):
        print("Dato no soportado")

    
        







