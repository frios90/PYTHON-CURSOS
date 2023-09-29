##EJERCICIOS DE TUPLAS Y LISTAS

#ejecicio 001

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

print("Ejercio 001");
print("Escribir un programa que almacene las asignaturas de un curso (por ejemplo MatemáticasFísica, Química, Historia y Lengua) en una lista y la muestre por pantalla.")
print("");
    
finish = False
signatures = []
while finish == False:
    print("Seleccione una opción")
    print("1.- Ingresar asignatura")
    print("2.- Finalizar y mostrar")
    print("")

    while True:
        option = input("opción :")
        if option == "1" or option == "2":
            break
        
    if option == "1":
        print("--ingrese asignatura:")
        signature = input("::")
        signatures.append(signature)
    else:
        print("Las asignaturas ingrasadas son")
        for val in signatures:
            print("- " + val)
        finish = True
            
