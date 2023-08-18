class CuentaBancaria:
    def __init__(self, nombre_socio, saldo_inicial):
        self.nombre_socio = nombre_socio
        self.saldo = saldo_inicial
        self.puntos_promocionales = 0
    
    def depositar(self, monto):
        self.saldo += monto
        if isinstance(self, CuentaPlatino):
            self.saldo *= 1.01
        elif isinstance(self, CuentaOro):
            self.saldo *= 1.02
            self.puntos_promocionales += 100
    
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
        else:
            print("Saldo insuficiente para retirar el monto especificado.")
    
    def consultar_saldo(self):
        return self.saldo


class CuentaOro(CuentaBancaria):
    pass


class CuentaPlatino(CuentaBancaria):
    pass


def main():
    cuentas = []
    
    while True:
        print("\nOpciones:")
        print("1. Abrir cuenta Oro")
        print("2. Abrir cuenta Platino")
        print("3. Realizar depósito")
        print("4. Realizar retiro")
        print("5. Consultar saldo")
        print("6. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            nombre_socio = input("Ingrese el nombre del socio: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuenta_oro = CuentaOro(nombre_socio, saldo_inicial)
            cuentas.append(cuenta_oro)
            print(f"Cuenta Oro para {nombre_socio} creada con éxito.")
        
        elif opcion == 2:
            nombre_socio = input("Ingrese el nombre del socio: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuenta_platino = CuentaPlatino(nombre_socio, saldo_inicial)
            cuentas.append(cuenta_platino)
            print(f"Cuenta Platino para {nombre_socio} creada con éxito.")
        
        elif opcion == 3:
            cuenta_idx = int(input("Ingrese el número de cuenta: ")) - 1
            if 0 <= cuenta_idx < len(cuentas):
                monto = float(input("Ingrese el monto a depositar: "))
                cuentas[cuenta_idx].depositar(monto)
                print("Depósito realizado con éxito.")
            else:
                print("Número de cuenta inválido.")
        
        elif opcion == 4:
            cuenta_idx = int(input("Ingrese el número de cuenta: ")) - 1
            if 0 <= cuenta_idx < len(cuentas):
                monto = float(input("Ingrese el monto a retirar: "))
                cuentas[cuenta_idx].retirar(monto)
                print("Retiro realizado con éxito.")
            else:
                print("Número de cuenta inválido.")
        
        elif opcion == 5:
            cuenta_idx = int(input("Ingrese el número de cuenta: ")) - 1
            if 0 <= cuenta_idx < len(cuentas):
                saldo = cuentas[cuenta_idx].consultar_saldo()
                print(f"Saldo de la cuenta de {cuentas[cuenta_idx].nombre_socio}: {saldo}")
            else:
                print("Número de cuenta inválido.")
        
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()
