
#crear diccionario
objetos={'auto': 'tuingo','moto':'yamaha', 'casa':'departamento', 'billete':100}
print(objetos)

#clear  elimina todo el contenido del diccionario.
objetos.clear()
print(objetos)

#get() nos permite consultar el value para un key determinado.
print(objetos.get('auto'))


#items() devuelve una lista con los keys y values del diccionario.
d=objetos.items()
print(list(d))

#keys()devuelve una lista con todas las keys del diccionario.
d=objetos.keys()
print(d)

#values()devuelve una lista con todos los values o valores del diccionario.
d=objetos.values()
print(d)

#pop busca y elimina la key que se pasa como parámetro y devuelve su valor asociado.
objetos.pop('casa')
print(objetos)

#popitem() elimina de manera aleatoria un elemento del diccionario.

objetos.popitem()
print(objetos)