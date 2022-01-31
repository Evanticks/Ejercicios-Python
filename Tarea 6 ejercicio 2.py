articulos=[]
conteo=int(input("Dime cuántos artículos vas a introducir: "))
for i in range(conteo):
    articulo=input("Dime el nombre del artículo: ")
    precio=float(input("Dime el precio del artículo: "))
    articulos.append([articulo,precio])

for i in articulos:
    (sum(i[1]))
    print ("la media del precio total es", i)
