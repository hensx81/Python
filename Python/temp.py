#***************************************************
#Nombre: Hennry
#Fecha: 15-04-2016 
# Programa para convertir una temperatura desde 
# Grados Fahrenheit a grados Celsius
#*************************************************
ent = raw_input ('Introduzca la Temperatura Fahrenheit : ')
try:
	pass
	fahr = float(ent)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print 'Temperatura en Grados Celsius : ', cel
except
	print 'Por favor, Introduzca un número'
