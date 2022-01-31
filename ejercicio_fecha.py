from funciones_fecha import LeerFecha,EsBisiesto

a,m,d=LeerFecha()

if EsBisiesto(miano):
    print("año no bisiesto.")
else:
print("año no bisiesto.")


#Programa 2
d1,m1,a1=LeerFecha()
d2,m2,a2=LeerFecha()


dj1=CalcularDiaJuliano(d1,m1,a1)
dj2=CalcularDiaJuliano(d2,m2,a2)

print(abs(dj1-dj2))
