print("Ejercicio 4.-Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.")

numeros = []

print("Ingrese los numeros de su apuesta")

cont = 1

while cont <= 6:

    while True:        
        numero = int(input("numero " + str(cont) + " : "))
        
        if numero >= 1 and numero <= 25 and not numero in numeros:
            numeros.append(numero)
            
            break
        else:
            print("reingrese")
        
    cont += 1

print(numeros)

##Solucion web

##for i in range(6):
##    awarded.append(int(input("Introduce un número ganador: ")))
##awarded.sort()
##print("Los números ganadores son " + str(awarded))
