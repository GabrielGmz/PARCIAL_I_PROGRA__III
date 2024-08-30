from datetime import datetime

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = []

    def registrar_asistencia(self, estado, fecha, razon=None):
        self.asistencias.append({"estado": estado, "fecha": fecha, "razon": razon})

class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_estudiantes = {}

    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes[estudiante.nombre] = estudiante

    def registrar_asistencia_estudiante(self, nombre_estudiante, estado, fecha, razon=None):
        if nombre_estudiante in self.lista_estudiantes:
            self.lista_estudiantes[nombre_estudiante].registrar_asistencia(estado, fecha, razon)
            print(f"Asistencia registrada para {nombre_estudiante}.")
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado en la lista.")

    def mostrar_asistencia(self):
        print(f"Asistencia registrada por {self.nombre}:")
        for estudiante in self.lista_estudiantes.values():
            print(f"Estudiante: {estudiante.nombre}")
            for asistencia in estudiante.asistencias:
                estado = asistencia["estado"]
                fecha = asistencia["fecha"].strftime("%Y-%m-%d")
                razon = asistencia.get("razon", "N/A")
                print(f"  Fecha: {fecha}, Estado: {estado}, Razón: {razon}")

class Director:
    def __init__(self, nombre):
        self.nombre = nombre

    def revisar_asistencia(self, docente):
        print(f"Asistencia revisada por el director {self.nombre}:")
        docente.mostrar_asistencia()


docente = Docente("Prof. Gòmez")
director = Director("Director Garcìa")

while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Registrar asistencia")
    print("3. Mostrar asistencia registrada")
    print("4. Revisar asistencia (Director)")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar estudiante
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        estudiante = Estudiante(nombre_estudiante)
        docente.agregar_estudiante(estudiante)
        print(f"Estudiante {nombre_estudiante} agregado.")

    elif opcion == "2":
        # Registrar asistencia
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        estado = input("Ingrese el estado (Asistencia/Permiso/Inasistencia): ")
        fecha = datetime.now()
        razon = None
        if estado.lower() == "permiso":
            razon = input("Ingrese la razón del permiso: ")

        docente.registrar_asistencia_estudiante(nombre_estudiante, estado, fecha, razon)

    elif opcion == "3":
        # Ver asistencia registrada
        docente.mostrar_asistencia()

    elif opcion == "4":
        # Revisar asistencia (Director)
        director.revisar_asistencia(docente)

    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")

