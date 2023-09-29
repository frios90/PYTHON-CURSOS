##Ejercicio 003

##Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

print("Ejercicio 003")
print("Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.")

signatures = [
        {
            "sign" : "Castellano",
            "note" : 0
        },
        {
            "sign" : "Matematcas",
            "note" : 0
        },
        {
            "sign" : "Historia",
            "note" : 0
        },
        {
            "sign" : "Naturaleza",
            "note" : 0
        }       

    ]

for key, val in enumerate(signatures):
    print("ingrese la nota de :" + val["sign"])
    signatures[key]["note"] = input("nota: ")

print(signatures)

print("BONUS: *args en prametros de funciones funciones")


def sumar (*args):
    suma = 0
    for a in args:
        suma = suma + a
    return suma


suma = sumar(1,2,8,9,15,48,79)
print(suma)
