inventario = {}

def cargar_inventario():
    while True:
        producto = input("Ingrese el nombre del producto (o 'q' para volver al menú): ")
        if producto == 'q':
            break
        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio_venta = float(input("Ingrese el precio de venta del producto: "))
        costo = float(input("Ingrese el costo del producto: "))
        inventario[producto] = {'cantidad': cantidad, 'precio_venta': precio_venta, 'costo': costo}
        
        continuar = input("¿Desea cargar más inventario? (s/n): ")
        if continuar.lower() != 's':
            break
        
def recibir_pedido():
    pedido = {}
    while True:
        producto = input("Ingrese el nombre del producto en el pedido (o 'q' para terminar el pedido): ")
        if producto == 'q':
            break
        cantidad = int(input("Ingrese la cantidad deseada: "))
        pedido[producto] = cantidad
    return pedido

def confirmar_stock(pedido):
    for producto, cantidad in pedido.items():
        if producto not in inventario or inventario[producto]['cantidad'] < cantidad:
            return False
    return True

def registrar_venta(pedido):
    for producto, cantidad in pedido.items():
        inventario[producto]['cantidad'] -= cantidad
    print("Venta registrada exitosamente.")

def imprimir_resumen():
    while True:
        opcion = input("\nSeleccione una opción:\n1. Resumen de inventario\n2. Resumen de ventas\n3. Resumen de costos\n4. Diferencia entre costo y venta\n5. Salir\nOpción: ")
        
        if opcion == '1':
            print("\n--- Resumen del inventario ---")
            for producto, info in inventario.items():
                print(f"Producto: {producto}, Cantidad: {info['cantidad']}, Precio de venta: {info['precio_venta']}, Costo: {info['costo']}")
        elif opcion == '2':
            print("\n--- Resumen de ventas ---")
            # Calcula el total de ventas
            total_ventas = sum(info['precio_venta'] * info['cantidad'] for info in inventario.values())
            print(f"Total de ventas: {total_ventas}")
        elif opcion == '3':
            print("\n--- Resumen de costos ---")
            # Calcula el total de costos
            total_costos = sum(info['costo'] * info['cantidad'] for info in inventario.values())
            print(f"Total de costos: {total_costos}")
        elif opcion == '4':
            print("\n--- Diferencia entre costo y venta ---")
            # Calcula la diferencia entre costo y venta
            diferencia = sum((info['precio_venta'] - info['costo']) * info['cantidad'] for info in inventario.values())
            print(f"Diferencia entre costo y venta: {diferencia}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar Inventario")
        print("2. Registrar Ventas")
        print("3. Ver Resúmenes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cargar_inventario()
        elif opcion == '2':
            pedido = recibir_pedido()
            if confirmar_stock(pedido):
                registrar_venta(pedido)
            else:
                print("No hay suficiente stock para completar el pedido.")
        elif opcion == '3':
            imprimir_resumen()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

# Iniciar el sistema
menu()
