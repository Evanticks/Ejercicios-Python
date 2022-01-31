def LeerFecha():
    dia=int(input("Dime el día: "))
    mes=int(input("Dime el mes: "))
    ano=int(input("Dime el año: "))
    while not Validar_Fecha(dia,mes,ano):
        dia=int(input("Dime el día: "))
        mes=int(input("Dime el mes: "))
        ano=int(input("Dime el año: "))
        return dia,mes,ano

def EsBisiesto(dato_ano):
    return dato_ano%4 == 0


def Dias_Del_Mes(mes,ano):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    if EsBisiesto(ano):
        dias[1]=29
        return dias[mes-1]

def Calcular_Dia_Juliano(dia,mes,ano):
    diaj=0
    for i in range(1,mes):
        diaj=diaj+dia(mes,ano)
        diaj=diaj+dia
    return diaj

def Resta_Dias(dia,mes):
    dia1=input("Dime un día: ")
    mes1=input("Dime un mes: ")
    dia2=input("Dime otro día: ")
    mes2=input("Dime otro mes: ")
    Calcular_Dia_Juliano(dia1,mes1,dia2,mes2)

def Validar_Fecha(dia,mes,ano):
    if mes not in range (1,13):
        return False
    if dia in range (1,Dias_Del_Mes):
        return True


