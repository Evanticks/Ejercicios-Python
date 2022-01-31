from crypt import crypt
f=open ("wpa_pass.txt")
lineas=f.readlines()
f.close()
f=open ("contras.txt")
contra=f.readlines()
f.close()
lista=[]

for lineas in lista:
encontrado=False
for i in lista:
    if i in lista[0]:
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