print("Calcular si un estudiante aprueba o reprueba una materia")

nota_1=float(input("Digita la primera nota: "))
nota_2=float(input("Digita la segunda nota: "))
nota_3=float(input("Digita la tercera nota: "))
nota_4=float(input("Digita la cuarta nota: "))
nota_5=float(input("Digita la quinta nota: "))

suma=(nota_1*0.15)+(nota_2*0.2)+(nota_3*0.15)+(nota_4*0.3)+(nota_5*0.2)
print(suma)

if suma<2 and suma>=1:
	print("Estas reprobado y no puedes recuperar")
elif suma>=4.5 and suma<=5:
	print("Felicidades por tu nota tan alta")
elif suma>=3 and suma<4.5:
	print("Estas aprobado")
elif suma>=2 and suma<3:
	print("Estas reprobado pero puedes recuperar")	
else:
	print("Nota invalida")

# numero 32



