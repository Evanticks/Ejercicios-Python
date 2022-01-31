from audioop import avg
import statistics
listacal=[]
listanombre=[]
alum=int(input("Dime cuántos alumnos tiene la clase: "))
for i in range (alum):
    nombre=input("Dime el nombre del alumno: ")
    nota=int(input("dime cuantas notas tiene ese alumno: "))
    listanombre.append(nombre)
    for n in range(nota):
        calificacion=int(input("Ingesa la nota: "))
        listacal.append(calificacion)
        listacal[nota:]
print(listacal)
 #print(sum(listacal)/nota)
    



