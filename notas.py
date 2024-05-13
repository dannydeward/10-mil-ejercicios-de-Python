
suma_notas=0
Promedio=0
Nota_alta=0
Nota_baja=10
aprobados=0
for nota  in range (30):
    nota=int(input('ingrese la nota '))
    suma_notas=suma_notas+nota
    if nota > Nota_alta:
        Nota_alta=nota
    if nota<Nota_baja:
        Nota_baja=nota
    if nota >= 4:
        aprobados= aprobados +1


print('La nota mas alta es: ', Nota_alta)

print('La nota mas baja es: ', Nota_baja)

print ('la suma total de notas es:' , suma_notas)

Promedio= suma_notas/30
print('el promedio de notas es: ', Promedio)

print('el total de aprobados es: ', aprobados)