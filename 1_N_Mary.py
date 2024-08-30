class Producto:
    def __init__(self, nombre, cantidad, precio_sugerido):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_sugerido = precio_sugerido

class Tienda:
    def __init__(self):
        self.inventario = {}
        self.libreta_compras = []

    def agregar_producto(self, nombre, cantidad, precio_sugerido):
        if nombre in self.inventario:
            self.inventario[nombre].cantidad += cantidad
        else:
            self.inventario[nombre] = Producto(nombre, cantidad, precio_sugerido)
        print(f"Producto {nombre} agregado al inventario.")

    def calcular_total(self, productos_comprados):
        total = sum(self.inventario[producto].precio_sugerido * cantidad for producto, cantidad in productos_comprados.items())
        return total

    def registrar_compra(self, productos_comprados, efectivo):
        total = self.calcular_total(productos_comprados)
        if efectivo < total:
            print("Efectivo insuficiente.")
            return None

        for producto, cantidad in productos_comprados.items():
            if self.inventario[producto].cantidad >= cantidad:
                self.inventario[producto].cantidad -= cantidad
                self.libreta_compras.append((producto, cantidad, self.inventario[producto].precio_sugerido * cantidad))
            else:
                print(f"No hay suficiente {producto} en inventario.")
                return None

        vuelto = efectivo - total
        print(f"Compra registrada. Total: ${total:.2f}. Vuelto: ${vuelto:.2f}.")
        return vuelto

    def mostrar_inventario(self):
        print("Inventario actual:")
        for producto in self.inventario.values():
            print(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio Sugerido: ${producto.precio_sugerido:.2f}")

    def ver_libreta(self):
        if not self.libreta_compras:
            print("La libreta está vacía.")
            return

        print("Libreta de compras:")
        for compra in self.libreta_compras:
            producto, cantidad, total = compra
            print(f"Producto: {producto}, Cantidad: {cantidad}, Total: ${total:.2f}")

tienda = Tienda()

while True:
    print("\nOpciones:")
    print("1. Agregar producto (proveedor)")
    print("2. Realizar compra (cliente)")
    print("3. Ver libreta de compras")
    print("4. Ver inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar productos (proveedor)
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
        precio_sugerido = float(input(f"Ingrese el precio sugerido para {nombre}: "))
        tienda.agregar_producto(nombre, cantidad, precio_sugerido)

    elif opcion == "2":
        # Registrar compra (cliente)
        productos_comprados = {}
        while True:
            nombre = input("Ingrese el nombre del producto a comprar (o 'terminar' para finalizar): ")
            if nombre.lower() == 'terminar':
                break
            if nombre in tienda.inventario:
                cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea comprar: "))
                productos_comprados[nombre] = cantidad
            else:
                print(f"Producto {nombre} no encontrado en el inventario.")

        # Mostrar el total antes de pedir el efectivo
        total = tienda.calcular_total(productos_comprados)
        print(f"El total de la compra es: ${total:.2f}")

        # Solicitar el monto de efectivo del cliente
        efectivo = float(input("Ingrese el monto de efectivo del cliente: "))
        tienda.registrar_compra(productos_comprados, efectivo)

    elif opcion == "3":
        # Ver libreta de compras
        tienda.ver_libreta()

    elif opcion == "4":
        # Ver inventario
        tienda.mostrar_inventario()

    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")



