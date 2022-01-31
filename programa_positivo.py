#comprobar si es positivo y que te muestre un mensaje en
#pantalla diciendo si es positivo o negativo.
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from positivo_funcion import comprobar_num
number=int(input("Escribe un número: "))
if comprobar_num (number) is True:
    print("Numero positivo")
elif comprobar_num (number) is False:
    print("Numero negativo")
