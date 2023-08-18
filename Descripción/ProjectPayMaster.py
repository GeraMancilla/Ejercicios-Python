class Proyecto:
    def __init__(self, empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores):
        self.empresa = empresa
        self.nombre_proyecto = nombre_proyecto
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.num_desarrolladores = num_desarrolladores
    
    def calcular_pago(self):
        pass


class ProyectoAutomatizacion(Proyecto):
    def __init__(self, empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores, costo_base, costo_material):
        super().__init__(empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores)
        self.costo_base = costo_base
        self.costo_material = costo_material
    
    def calcular_pago(self):
        costo_total = self.costo_base + self.costo_material
        pago_por_desarrollador = costo_total / self.num_desarrolladores
        return pago_por_desarrollador


class ProyectoWeb(Proyecto):
    def __init__(self, empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores, costo_base_por_modulo, costo_hospedaje, porcentaje_impuesto):
        super().__init__(empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores)
        self.costo_base_por_modulo = costo_base_por_modulo
        self.costo_hospedaje = costo_hospedaje
        self.porcentaje_impuesto = porcentaje_impuesto
    
    def calcular_pago(self):
        costo_total_base = self.costo_base_por_modulo * self.num_desarrolladores
        total_pago = costo_total_base + self.costo_hospedaje
        impuesto = total_pago * (self.porcentaje_impuesto / 100)
        pago_final = total_pago - impuesto
        pago_por_desarrollador = pago_final / self.num_desarrolladores
        return pago_por_desarrollador


def main():
    tipo_proyecto = input("Ingrese el tipo de proyecto (Automatización o Web): ")
    empresa = input("Ingrese el nombre de la empresa: ")
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    fecha_inicio = input("Ingrese la fecha de inicio: ")
    fecha_termino = input("Ingrese la fecha de término: ")
    num_desarrolladores = int(input("Ingrese el número de desarrolladores: "))
    
    if tipo_proyecto.lower() == "automatización":
        costo_base = float(input("Ingrese el costo base: "))
        costo_material = float(input("Ingrese el costo por material: "))
        proyecto = ProyectoAutomatizacion(empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores, costo_base, costo_material)
    elif tipo_proyecto.lower() == "web":
        costo_base_por_modulo = float(input("Ingrese el costo base por módulo: "))
        costo_hospedaje = float(input("Ingrese el costo de hospedaje: "))
        porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))
        proyecto = ProyectoWeb(empresa, nombre_proyecto, fecha_inicio, fecha_termino, num_desarrolladores, costo_base_por_modulo, costo_hospedaje, porcentaje_impuesto)
    else:
        print("Tipo de proyecto inválido.")
        return
    
    pago_por_desarrollador = proyecto.calcular_pago()
    print(f"Pago por desarrollador: ${pago_por_desarrollador:.2f}")


if __name__ == "__main__":
    main()
