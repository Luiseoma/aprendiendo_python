#ingreso_mensual = 50000
#
#if ingreso_mensual > 10000:
#    print("Eres casi millonario")
#
#elif ingreso_mensual > 1000:
#    print("Estás bien")
#    
#else:
#    print("Buscate un trabajo")
    
    
#if anidados

ingreso_anual = 80000
gasto_anual = 80001

print(ingreso_anual - gasto_anual)
if ingreso_anual  > 10000:
    if ingreso_anual - gasto_anual < 0:
        print("Te falta plata")
    elif ingreso_anual - gasto_anual > 70000:
        print("Como viviste con tan poca plata un año")
    elif ingreso_anual - gasto_anual > 50000:
        print("Gastaste algo")
    elif ingreso_anual - gasto_anual > 20000:
        print("Uy casi casi")
    else:
        print("Poco ahorro")

        
    