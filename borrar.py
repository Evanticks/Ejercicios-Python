articulos=[]
precios=[]
conteo=int(input("Dime cuántos artículos vas a introducir: "))
if conteo >=1:
    for i in range(conteo):
        articulo=input("Dime el nombre del artículo: ")
        precio=float(input("Dime el precio del artículo: "))
        articulos.append(articulo)
        precios.append(precio)
print (sum(precios)/conteo)