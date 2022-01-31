#Agenda(lista) de contactos (diccionario) donde vamos a guardar nombre y número de teléfono.
agenda=[]
confirmar=input("Quieres añadir datos?, s/n: ")
while confirmar !="n":
    contacto={}
    contacto["nombre"]=input("Nombre: ")
    contacto["telefono"]=input("telefono: ")
    agenda.append(contacto)
    confirmar=input("Quieres añadir nuevos datos?, s/n: ")
#for contacto in agenda:
#    print (contacto)
for amigo in agenda:
    print("Nombre del amigo:", amigo.get("nombre"))
    print("Teléfono del amigo:", amigo.get("telefono"))
#mostrar todos los nombres y sus teléfonos
#pedir un nombre y si existe muesta un teléfono, si no existe contacto hay que indicarlo
encontrado=False
nombre_a_buscar=input("Escribe el nombre que quieres encontrar: ")
for amigo in agenda:
    if nombre_a_buscar==amigo.get("nombre"):
        print(amigo.get("telefono"))
        encontrado=True
if encontrado == False:
    print("no se ha encontrado el contacto")