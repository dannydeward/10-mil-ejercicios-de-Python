 #cajero Automatico
import time

cuentas={}

def saludar():
    print('Bienvendo al cajero Automatico')
    time.sleep(1) # RETRAMOS UN SEGUNDO EL SALUDO

def verifcar_cuenta():
    while True:
        tienes_cuenta=input('¿Tienes una cuenta? (Si/No):  ')
        if tienes_cuenta== "si":
            return True
        elif tienes_cuenta=='no':
            return False
        else:
            print('por favor, responde si o no')
            
def crear_cuenta():
    nombre=input('introduce tu nombre:')
    clave= int(input('ingresa un numero de 4 dijitos:' ))
    saldo= 0
    cuentas[nombre]={'clave':clave, 'saldo': saldo }
    print("Cuenta ha sido creada exitosamente")
            
def iniciar_sesion():
    nombre=input('ingrese su nombre: ')
    clave=int(input('ingrese su clave: '))
    
    if nombre in cuentas and cuentas[nombre]['clave']==clave:
        print(f'Bienvenido,{nombre}!')
        return True
    else:
        crear_cuenta_opcional=input('Nombre de usuario incorrecto, ¿Quieres abrir una cuenta?, Si o No')
        if crear_cuenta_opcional== 'si':
            crear_cuenta()
        else:
            print('Operacion Finalizada, Hasta Luego')
            return False
        
def operaciones():
    nombre=input('ingrese su nombre: ')
    while True: 
        print("\nOperaciones Disponibles")
        print('1.-Consultar Saldo')
        print('2.-Hacer Deposito')
        print('3.-Hacer retiro')
        print('4.-salir')
        
        opcion=input('selecione una operacion, ingrese un numero del 1 al 4: ')
       

        if opcion== '1':
            print(f"Tu saldo actual es ${cuentas[nombre]['saldo']}")
        elif opcion =='2':
            deposito=float(input('Ingrese el monto a depositar: '))
            cuentas[nombre]['saldo']+=deposito
        elif opcion=='3':
            retiro=float(input('Ingrese el monto a retirar: '))
            if retiro > cuentas[nombre]['saldo']:
                print('fondos insuficientes, retire otor monto')
            else:
                cuentas[nombre]['saldo']-=retiro
                print(f"retiro existoso, tu nuevo saldo es ${cuentas[nombre]['saldo']}")
        elif opcion=='4':
            print('Sesion finalizada, Que tenga buen dia')
            break
        
        else:
            print('opcion no valida, elige una opocion del 1 al 4 ')    
     
saludar()

if verifcar_cuenta():
    if not iniciar_sesion():
        print('operacion cancelada, hasta luego')
    else:
        operaciones()
else:
    crear_cuenta()
    iniciar_sesion()
    operaciones()
       
    
