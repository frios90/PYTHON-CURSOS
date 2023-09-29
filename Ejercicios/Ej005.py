print("Ejercicio 5.-Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.")

numeros = []
for i in range(10):
    numeros.append(str(i+1))

numeros.reverse()
mi_string = ','.join(numeros)

print(mi_string) # Resultado: elemento1,elemento2,elemento3
