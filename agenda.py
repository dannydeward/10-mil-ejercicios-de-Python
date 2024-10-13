contactos = {}

def cargar_contacto(nombre,telefono):
    contactos[nombre] = telefono

def borrar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]

def buscar_contacto(nombre):
    return contactos.get(nombre, "Contacto no existe")

cargar_contacto("Alice", "123-4567")
print(contactos)
cargar_contacto("Bob", "987-6543")
print(contactos)
print(buscar_contacto("Alice"))
borrar_contacto("Alice")
print(buscar_contacto("Alice"))
print(contactos)
