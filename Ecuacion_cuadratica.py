import math

print("Algoritmo que imprima una funcion cuadratica")

a=int(input('Ingrese el valor de a: '))

if a==0:
    print('El valor de "a" no puede ser cero ')
    print('reingrese el valor de "a" ')

    a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de b: '))
c=int(input('Ingrese el valor de c: '))

x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)

print("Las raices son: ")
print(x1)
print(x2)
print("Final del programa")    
