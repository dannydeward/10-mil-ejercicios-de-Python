"""cuenta=float(input("ingrese el valor total de la cuenta:"  ))
propina=float(input("ingrese el porcentaje de la propina:" ))

prop=cuenta*(propina/100)

total_pagar= cuenta+prop


#print("Total de la cuenta:", cuenta)
#print("total de la propina", prop)
print("total de la cuenta a pagar es :", cuenta, "+", prop, "es igual", total_pagar,"$")"""

def calcular_propina():
    cuenta=float(input("ingrese el valor total de la cuenta:"  ))
    propina=float(input("ingrese el porcentaje de la propina:" ))
    
    prop=cuenta*(propina/100)
    total_pagar= cuenta+prop
    
    print("total cuenta:", cuenta)
    print("total propina:", prop)
    print("Total a pagar", total_pagar)
    

calcular_propina()
    
