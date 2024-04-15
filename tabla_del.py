def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Llamar a la función para imprimir la tabla de multiplicar
tabla_de_multiplicar(numero)
