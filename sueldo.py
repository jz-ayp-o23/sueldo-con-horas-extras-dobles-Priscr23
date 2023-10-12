"""
Diseña un programa para calcular el sueldo semanal de un empleado, dadas las horas trabajadas y la tarifa horaria (cuánto se le paga por cada hora trabajada). Considerar que si trabajó más de 48 horas, las horas excedentes se pagan al doble. Desglosar la cantidad y el importe correspondientes a las horas extras.
750722
"""

#Entradas
horas_semanal = float(input("Ingrese horas trabajadas: "))
tarifa_horaria = float(input("Ingrese la tarifa horaria: "))

#Procesos
horas_normales = 48
horas_extras = horas_semanal - 48
horas_extras_pago = tarifa_horaria * 2
compensacion = horas_extras * horas_extras_pago


sueldo_normal = horas_normales * tarifa_horaria
pago_extra = compensacion + sueldo_normal


#Salidas
if horas_semanal <= 48:
    print("Su sueldo es de: ", sueldo_normal)
  

elif horas_semanal > 48:
    print("Su sueldo es: ", pago_extra)


