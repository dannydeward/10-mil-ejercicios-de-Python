tareas = []

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes")
    else:
        print("Tareas pendientes:")
        for index, tarea in enumerate(tareas, start=1):
            print(f"{index}. {tarea}")

def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        tarea_eliminar = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= tarea_eliminar <= len(tareas):
            tarea_eliminada = tareas.pop(tarea_eliminar - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada correctamente")
        else:
            print("Número de tarea inválido")

while True:
    print("\nLista de Tareas")
    print("1. Agregar Tarea")
    print("2. Mostrar Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1/2/3/4): "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        mostrar_tareas()
    elif opcion == 3:
        eliminar_tarea()
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")
