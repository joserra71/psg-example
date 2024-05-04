# Conversion de 288325 en dias, horas y segundos
tiempo_total = 288325
dias = tiempo_total // (60 * 60 * 24)
tiempo_total = tiempo_total % (60 * 60 * 24)
horas = tiempo_total // (60 * 60)
tiempo_total = tiempo_total % (60 * 60)
minutos = tiempo_total // 60
segundos = tiempo_total % 60

print("Conversion de 288325 segundos en:")
print("dias")
print (dias)
print("*****")
print("horas")
print (horas)
print("*****")
print("minutos")
print(minutos)
print("******")
print("segundos")
print(segundos)