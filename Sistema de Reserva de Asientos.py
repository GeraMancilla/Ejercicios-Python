asientos = ['Disponible'] * 25
precio_boleto = 115.75

while True:
    print("Asientos disponibles:")
    for i, estado in enumerate(asientos):
        numero_asiento = i + 1
        if estado == 'Disponible':
            print(f"Asiento {numero_asiento}: {estado}")

    asiento = int(input("¿Qué asiento deseas ocupar? (Ingresa el número del asiento) "))
    if asiento < 1 or asiento > 25:
        print("Asiento inválido. Por favor, elige un número de asiento válido.")
        continue

    if asientos[asiento - 1] == 'Ocupado':
        print("El asiento seleccionado ya está ocupado. Por favor, elige otro asiento.")
        continue

    pago = float(input("¿Cuánto pagarás por el boleto? "))
    if pago < precio_boleto:
        print("El pago es insuficiente. No se puede vender el boleto.")
        continue

    cambio = pago - precio_boleto
    print(f"Gracias por tu compra. Tu cambio es de ${cambio:.2f}.")

    asientos[asiento - 1] = 'Ocupado'

    seguir_comprando = input("¿Deseas comprar más boletos? (si/no) ")
    if seguir_comprando.lower() != 'si':
        break

print("Gracias por viajar con nosotros. ¡Buen viaje!")
