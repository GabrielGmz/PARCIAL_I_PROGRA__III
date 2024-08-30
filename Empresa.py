class Empleado:
    def __init__(self, nombre, anios_laborados):
        self.nombre = nombre
        self.anios_laborados = anios_laborados
        self.bono_adicional = 0
    
    def calcular_bono(self):
        if self.anios_laborados > 5:
            self.bono_adicional = 1000  # Bono fijo para simplificar, puede ser otro valor o porcentaje
        return self.bono_adicional

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, anios_laborados, salario_base, comisiones):
        super().__init__(nombre, anios_laborados)
        self.salario_base = salario_base
        self.comisiones = comisiones
    
    def calcular_salario(self):
        bono = self.calcular_bono()
        salario_total = self.salario_base + self.comisiones + bono
        return salario_total

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anios_laborados, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, anios_laborados)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        bono = self.calcular_bono()
        salario_total = (self.tarifa_por_hora * self.horas_trabajadas) + bono
        return salario_total

def ingresar_empleado_fijo():
    nombre = input("Ingrese el nombre del empleado fijo: ")
    anios_laborados = int(input("Ingrese los años laborados: "))
    salario_base = float(input("Ingrese el salario base: "))
    comisiones = float(input("Ingrese las comisiones: "))
    return EmpleadoFijo(nombre, anios_laborados, salario_base, comisiones)

def ingresar_empleado_por_horas():
    nombre = input("Ingrese el nombre del empleado por horas: ")
    anios_laborados = int(input("Ingrese los años laborados: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    return EmpleadoPorHoras(nombre, anios_laborados, tarifa_por_hora, horas_trabajadas)

# Ingreso de empleados
empleados = []
numero_empleados = int(input("Ingrese el número de empleados a registrar: "))

for _ in range(numero_empleados):
    tipo_empleado = input("Ingrese el tipo de empleado (fijo/por horas): ").strip().lower()
    if tipo_empleado == "fijo":
        empleado = ingresar_empleado_fijo()
    elif tipo_empleado == "por horas":
        empleado = ingresar_empleado_por_horas()
    else:
        print("Tipo de empleado no válido. Intente nuevamente.")
        continue
    empleados.append(empleado)

# Calcular y mostrar salarios
for empleado in empleados:
    salario_total = empleado.calcular_salario()
    print(f"\nEmpleado: {empleado.nombre}")
    print(f"Salario Total: ${salario_total:.2f}")
    print("-----")
