print("##------------------------------------------------------------------------------**")
print("##---------------Programa para calcular promedios----------------**")
print("##------------------------------------------------------------------------------**")


print("-Ingrese nombre del alumno:")
nombre = input(": ")


while True:      
    print("-Ingrese nota de matemáticas:")
    nota_matematicas = float(input(": "))
    if nota_matematicas >= 1 and nota_matematicas <= 7:
        break
    else:
        print("ERROR")

while True:      
    print("-Ingrese nota de castellano:")
    nota_castellano = float(input(": "))
    if nota_castellano >= 1 and nota_castellano <= 7:
        break
    else:
        print("ERROR")


while True:      
    print("-Ingrese nota de historia:")
    nota_historia = float(input(": "))
    if nota_historia >= 1 and nota_historia <= 7:
        break
    else:
        print("ERROR")

while True:      
    print("-Ingrese nota de naturaleza:")
    nota_naturaleza = float(input(": "))
    if nota_naturaleza >= 1 and nota_naturaleza <= 7:
        break
    else:
        print("ERROR") 

promedio  = (nota_matematicas + nota_castellano + nota_historia + nota_naturaleza) / 4

if promedio > 5.5:
    print( nombre + " Aprobaste! : " + str(promedio) )
else:
    print( nombre + " Reprobaste! : " + str(promedio) )
