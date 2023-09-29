print("Ejercicio 9 Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.")



while True:
    print("Ingrese una palabra:")
    palabra = input("P: ")
    if palabra in ["salir", "exit"]:
        break

    a = 0
    e = 0
    i  = 0
    o = 0
    u = 0

    for vocal in palabra:
        if  vocal in ["a", "A"]:
            a += 1
        if  vocal in ["e", "E"]:
            e += 1
        if  vocal in ["i", "I"]:
            i += 1
        if  vocal in ["o", "O"]:
            o += 1
        if  vocal in ["u", "U"]:
            u += 1

    print("total a: " + str(a))
    print("total e: " + str(e))
    print("total i: "  + str(i))
    print("total o: " + str(o))
    print("total u: " + str(u))

