print("Ejercicio 6 .- Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una      lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.")



asignaturas = [
    "Castillano",
    "Ingles",
    "Matematicas",
    "Historia"
]

keys_aprobadas = []

for key,val in enumerate(asignaturas):
    while True:
        nota = float(input("Ingrese la nota de " + val + " : "))
        if nota >=1 and nota <= 7:
            break
        else:
            print("Reingrese una nota del 1 al 7")

    if nota > 4:
        keys_aprobadas.append(val)


for i in keys_aprobadas:
    asignaturas.remove(i)

print("las asignaturas reprobadas son:")
print(asignaturas)
        
        
    
