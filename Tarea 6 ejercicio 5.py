from crypt import crypt
f=open ("contras.txt")
lineas=f.readlines()
f.close()
lista=[]
for linea in lineas:
    lista.append(linea.split(":"))

nombre=input ("Nombre: ")
encontrado=False
for usuario in lista:
    if nombre==usuario[0]:
        encontrado=True
        sal=usuario[1][:30] #Esto es un slice o rebanada
        passwd=input("Contraseña: ")
        encriptado=crypt(passwd,sal)
        if usuario [1] == encriptado:
            print("La contraseña es correcta.")
        else: print("La contraseña no es correcta.")
if not encontrado:
    print("Usuario no existe")

#El usuario es prueba y la contraseña es HALLOWEEN