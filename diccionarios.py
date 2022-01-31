alum1={}
alum1["nombre"]="Pepe"
alum1["edad"]=23
#los diccionarios son mutables, por tanto se puede alterar
#cada campo del diccionario, ya que son listas.
alum2={"nombre":"María","edad":25}
aula=[]
aula.append(alum1)
aula.append(alum2)
#print (aula[1]["nombre"])
#for alum in aula:
#    print(alum["nombre"])
domicilio1={"calle":"Botica","numero":10}
alum3={"nombre":"Rafa","edad":30,"domicilio":{"calle":"Botica","numero":10}, "asignaturas":["FH", "LM", "BD"]}
#print(len(alum3))
#del(alum3["edad"])
#alum4=alum3.copy()
#print(alum3.get("nombre")) es una función de diccionario, no sirve para listas.
