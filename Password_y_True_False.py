f=open(contras.txt)
lineas=f.readlines()
f.close()
print (lineas)
lista=[]
for linea in lineas:
    lista.append(linea.split(":"))

print(lista)

nombre=input ("Nombre")
encontrado=False
for usuario in lista:
    if nombre==usuario[0]:
        Encontrado=True
        sal=usuario[1][:30] #Esto es un slice o rebanada
        passwd=input("Contraseña: ")
        print(usuario[1])
        print(sal)
if not encontrado:
    print("Usuario no existe")