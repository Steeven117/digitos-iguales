# DOS ULTIMOS DIGITOS IGUALES

print("-------------------------------------------------------------")
print("----------LOS ULIMOS DIGITOS CUMPLEN O NO LA FUNCION---------")
print("-------------------------------------------------------------")

#INPUT

X = int(input("Ingrese el valor de X: "))

#PROCESSING

A = X%100
C = A%10
B = A//10

if C==B :
    Rta = "Los dos ultimos digitos son iguales"

else : 
    Rta = "Los dos ultimos digitos no son iguales"

#OUTPUT

print(str(Rta))
