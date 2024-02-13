import time
import json

# Intentamos cargar el diccionario desde un archivo
try:
    with open('cuentas.json', 'r') as archivo:
        cuentas = json.load(archivo)
except FileNotFoundError:
    cuentas = {}

nombre = input('Ingrese su nombre: ')

def guardar_cuentas():
    with open('cuentas.json', 'w') as archivo:
        json.dump(cuentas, archivo)

def saludar():
    print('Bienvenido al cajero automático')
    time.sleep(1)

def crear_cuenta():
    clave = int(input('Ingrese un número de 4 dígitos: '))
    saldo = 0
    cuentas[nombre] = {'clave': clave, 'saldo': saldo}
    print("Cuenta ha sido creada exitosamente")

def iniciar_sesion():
    clave = int(input('Ingrese su clave: '))

    if nombre in cuentas and cuentas[nombre]['clave'] == clave:
        print(f'Bienvenido, {nombre}!')
        return True
    else:
        crear_cuenta_opcional = input('Nombre de usuario incorrecto, ¿Quieres abrir una cuenta?, Si o No: ')
        if crear_cuenta_opcional.lower() == 'si':
            crear_cuenta()
        else:
            print('Operación Finalizada, Hasta Luego')
            return False

def operaciones():
    while True:
        print("\nOperaciones Disponibles")
        print('1.- Consultar Saldo')
        print('2.- Hacer Depósito')
        print('3.- Hacer Retiro')
        print('4.- Salir')

        opcion = input('Seleccione una operación, ingrese un número del 1 al 4: ')

        if opcion == '1':
            print(f"Tu saldo actual es ${cuentas[nombre]['saldo']}")
        elif opcion == '2':
            deposito = float(input('Ingrese el monto a depositar: '))
            cuentas[nombre]['saldo'] += deposito
        elif opcion == '3':
            retiro = float(input('Ingrese el monto a retirar: '))
            if retiro > cuentas[nombre]['saldo']:
                print('Fondos insuficientes, retire otro monto')
            else:
                cuentas[nombre]['saldo'] -= retiro
                print(f"Retiro exitoso, tu nuevo saldo es ${cuentas[nombre]['saldo']}")
        elif opcion == '4':
            guardar_cuentas()  # Guardamos el diccionario antes de salir
            print('Sesión finalizada, Que tenga buen día')
            break
        else:
            print('Opción no válida, elige una opción del 1 al 4 ')

saludar()

if nombre in cuentas:
    if not iniciar_sesion():
        print('Operación cancelada, hasta luego')
    else:
        operaciones()
else:
    crear_cuenta()
    iniciar_sesion()
    operaciones()
