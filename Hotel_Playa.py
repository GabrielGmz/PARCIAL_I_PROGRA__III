class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche

class Cliente:
    def __init__(self, nombre, dni, noches, habitacion, servicios_extra):
        self.nombre = nombre
        self.dni = dni
        self.noches = noches
        self.habitacion = habitacion
        self.servicios_extra = servicios_extra

    def calcular_total(self):
        total_habitacion = self.habitacion.precio_por_noche * self.noches
        total_servicios = sum(self.servicios_extra.values())
        total = total_habitacion + total_servicios
        return total

    def generar_factura(self):
        print("\n--- Factura del Hotel ---")
        print(f"Cliente: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Habitación: {self.habitacion.tipo}")
        print(f"Noches: {self.noches}")
        print(f"Precio por noche: ${self.habitacion.precio_por_noche:.2f}")
        print(f"Total habitación: ${self.habitacion.precio_por_noche * self.noches:.2f}")
        if self.servicios_extra:
            print("\nServicios Extra:")
            for servicio, precio in self.servicios_extra.items():
                print(f"  {servicio}: ${precio:.2f}")
            print(f"Total servicios extra: ${sum(self.servicios_extra.values()):.2f}")
        print(f"\nTotal a pagar: ${self.calcular_total():.2f}")
        print("-------------------------\n")

class Hotel:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Sencilla", 100),
            Habitacion("Doble", 150),
            Habitacion("Suite", 250)
        ]
        self.servicios = {
            "Piscina": 20,
            "Cancha de Golf": 50,
            "Spa": 70
        }

    def mostrar_habitaciones(self):
        print("\nHabitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones, start=1):
            print(f"{i}. {habitacion.tipo} - ${habitacion.precio_por_noche:.2f} por noche")

    def mostrar_servicios(self):
        print("\nServicios adicionales disponibles:")
        for servicio, precio in self.servicios.items():
            print(f"{servicio}: ${precio:.2f}")

    def elegir_habitacion(self, opcion):
        return self.habitaciones[opcion - 1]

    def elegir_servicios(self):
        servicios_seleccionados = {}
        while True:
            self.mostrar_servicios()
            servicio = input("Ingrese el nombre del servicio que desea (o 'terminar' para finalizar): ")
            if servicio.lower() == 'terminar':
                break
            if servicio in self.servicios:
                servicios_seleccionados[servicio] = self.servicios[servicio]
            else:
                print("Servicio no disponible.")
        return servicios_seleccionados

# Simulación de uso interactivo

hotel = Hotel()

while True:
    print("\nOpciones:")
    print("1. Ver habitaciones disponibles")
    print("2. Registrar cliente y generar factura")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Mostrar habitaciones disponibles
        hotel.mostrar_habitaciones()

    elif opcion == "2":
        # Registrar cliente y generar factura
        hotel.mostrar_habitaciones()
        eleccion = int(input("Seleccione el número de la habitación deseada: "))
        habitacion_seleccionada = hotel.elegir_habitacion(eleccion)

        nombre_cliente = input("Ingrese el nombre del cliente: ")
        dni_cliente = input("Ingrese el DNI del cliente: ")
        noches = int(input("Ingrese el número de noches que permanecerá: "))

        print("\n¿Desea agregar servicios adicionales?")
        servicios_extra = hotel.elegir_servicios()

        cliente = Cliente(nombre_cliente, dni_cliente, noches, habitacion_seleccionada, servicios_extra)
        cliente.generar_factura()

    elif opcion == "3":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")
