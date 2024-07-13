import math # Control + click para ver la libreria


numTest1 = 20
numTest2 = 10
sumaTest = numTest1+numTest2
# print(numTest1 + numTest2)
print(sumaTest)

print("\n----------------------\n")

num1 = float(input("Ingrese el valor del número 1: "))
num2 = float(input("Ingrese el valor del número 2: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
potencia = num1 ** num2 # Es lo mismo math.pow
potencia_2 = math.pow(num1, num2) # Es lo mismo **
raizCuadrada = math.sqrt(num1) # Solo potencia de 2
RaizCubica = num1 ** (1/3)

# print("\tLa suma es:", suma)
# print(f'\tLa suma es: {suma}')

print("\tLa suma es: "+str(suma)) # convierte la variable a string
print("\tLa resta es: "+str(resta))
print("\tLa multiplicacion: "+str(multiplicacion))
print("\tLa division: "+str(division))
print("\tEl modulo: "+str(modulo))
print("\tLa potencia: "+str(potencia)+" o "+str(potencia_2))
print("\tLa raiz cuadrada: "+str(raizCuadrada))
print("\tLa raiz cubica: "+str(RaizCubica))


print("\n----------------------\n")

   