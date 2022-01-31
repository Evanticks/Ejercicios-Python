pagar=float(input("Cantidad que se ha de pagar: "))
entregado=float(input("Cantidad que se ha entregado: "))
cambio=entregado-pagar
while cambio !=0:
    if cambio >=50:
        cambio=cambio-50
        print("billete de 50 euros")
    elif cambio >=20 and cambio<50:
        cambio=cambio-20
        print("Billete de 50 euros")
    elif cambio >=10 and cambio <20:
        cambio=cambio-10
        print("Billete de 10 euros")
    elif cambio >=5 and cambio <10:
        cambio=cambio-5
        print("Billete de 10 euros")
    elif cambio >=2 and cambio <5:
        cambio=cambio-2
        print("Moneda de 2 euros")
    elif cambio >=1 and cambio <2:
        cambio=cambio-1
        print("Moneda de 1 euro")
    elif cambio >=0.50 and cambio <1:
        cambio=cambio-0.50
        print("Moneda de 50 cents")
    elif cambio >=0.20 and cambio <0.50:
        cambio=cambio-0.20
        print("Moneda de 20 cents")
    elif cambio >=0.10 and cambio <0.20:
        cambio=cambio-0.10
        print("Moneda de 10 cents")
    elif cambio >=0.05 and cambio <0.10:
        cambio=cambio-0.05
        print("Moneda de 5 cents")
    elif cambio >=0.02 and cambio <0.05:
        cambio=cambio-0.02
        print("Moneda de 2 cents")
    elif cambio >0 and cambio < 0.02:
        cambio=0
        print("Moneda de 1 cent")
print("fin del programa")