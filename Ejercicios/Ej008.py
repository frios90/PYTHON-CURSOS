print("Ejercicio 8 Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.")


while True:

    print("ingrese una palabra:")
    
    palabra = input("p: ")

    if palabra in ["salir", "q", "exit"]:
        break

    palabraReverse = palabra[::-1]
##La expresión [::-1] se utiliza para obtener una "rebanada" de la cadena que va desde
##el último carácter hasta el primero, lo que da como resultado la cadena invertida.
    
    if palabra == palabraReverse :
        print(palabra +  " es un palíndromo"  )
    else:
        print("nada")

    print("## para terminar use la palabra 'salir' ##")


##word = input("Introduce una palabra: ")
##reversed_word = word
##word = list(word)
##reversed_word = list(reversed_word)
##reversed_word.reverse()
##if word == reversed_word:
##    print("Es un palíndromo")
##else:
##    print("No es un palíndromo")
