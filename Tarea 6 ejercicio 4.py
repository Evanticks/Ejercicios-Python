equipos=[]
resultados=[]
#[["Betis","Sevilla"],["Madrid","Barcelona"],["Rayo","Osasuna"],["Atlético","Cádiz"],["Levante","Getafe"],["PSG","Lille"],["Juventus","Lazio"],["Man U.","Man City"],["Bayern","Dortmund"],["Liverpool","Tottenham"],["Alavés","Valladolid"],["Kawasaki Frontale","Vissel Kobe"],["River","Boca"],["Torino","Roma"],["Chelsea","Arsenal"]]
for i in range(0,15):
    equipo1=input("indica el nombre del equipo local: ")
    equipo2=input("Indica el nombre del equipo visitante: ")
    resultado1=int(input("Indica el resultado del equipo local: "))
    resultado2=int(input("Indica el resultado del equipo visitante: "))
    equipos.append([equipo1,equipo2])
    resultados.append([resultado1,resultado2])
for i in zip(equipos,resultados):
    print (i)
