
         #parámentros
def suma(number1, number2):

    sum = number1 + number2
    print(sum)

#argumentos
#suma(2, 2)#4

# 3 Funciones que hagan la resta, división y multiplicación.


import random


dinero = False

def verder_alcohol(edad):
    print(edad)

        #True           True
    if edad >= 18 and dinero:# Si esta condición no se cumple, se va directo al else
        print("Vender alcohol.")

    elif edad >=18:
        print("Te vendo alcohol, pero es fiado.")

    else:# Si la condición no se cumple, entra aquí mero.
        print("No vender alcohol, porque es menor de 18 años.")


value = 1
while value < 2:
    value = value + 1
    edad = random.randint(5, 20)
    verder_alcohol(edad)

