articulos=[]
precios=[]
conteo=int(input("Dime cuántos artículos vas a introducir: "))
if conteo >=1:
    for i in range(conteo):
        articulo=input("Dime el nombre del artículo: ")
        precio=float(input("Dime el precio del artículo: "))
        articulos.append(articulo)
        precios.append(precio)
print (sum(precios)/conteo, "Es la media de los precios.")
for i,a in zip(precios,articulos):
    if i > 100:
        print(a, "Vale más de 100")
nombre=input("Dime el nombre del artículo: ")
for i,a in zip(precios,articulos):
    if nombre in a:
        print(i, "Es su precio.")

