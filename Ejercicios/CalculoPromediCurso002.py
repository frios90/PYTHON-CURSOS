##Funcion main
def main() :
    print("##------------------------------------------------------------------------------**")
    print("##---Programa para calcular notas de un curso------------------**")
    print("##------------------------------------------------------------------------------**")

   
    administracion = managementeAlumns()

    print("##------------------------------------------------------------------------------**")
    print("##---Resultados de la gestion de alumnos-------------------------**")
    print("##------------------------------------------------------------------------------**")
    for alumno in administracion:
        print("##---"+alumno["nombre"]+"-------------------------**")
        print("Ramo 001 : " + str(alumno["ramo_1"]))
        print("Ramo 002 : " + str(alumno["ramo_2"]))
        print("Ramo 003 : " + str(alumno["ramo_3"]))
        print("Ramo 004 : " + str(alumno["ramo_4"]))
        print("Promedio : " + str(alumno["promedio"]))
        print("Asistencia : " + str(alumno["asistencia"]))

        if  alumno["promedio"] < 4 and alumno["asistencia"] < 75:
            print("X-REPRUEBA")
        else:
            print("O-APRUEBA")     
        
##Función para la administración de alumnos
def  managementeAlumns ():
    alumnos = []

    while True:
        
        print("-Seleccione una opción:")
        print("1) Registrar datos de alumno")
        print("2) Finalizar")
       

        while True:
            option = input(": ")
            if option == "1" or option == "2":
                break
            else:
                print("ingrese una opción valida")


        if option == "1":
            print("ingrese nombre del alumno")
            nombre = input(": ")
            print("ingrese porcentaje de asistencia del alumno")
            while True:
                asistencia = int(input(": "))
                if asistencia >= 1 and asistencia <= 100:               
                    break
                else:
                    print("ingrese una opción valida")  
            print("ingrese notas del ramo 1")
            ramo_1 = ingresoNumero()
            print("ingrese notas del ramo 2")
            ramo_2 = ingresoNumero()
            print("ingrese notas del ramo 3")
            ramo_3 = ingresoNumero()
            print("ingrese notas del ramo 4")
            ramo_4 = ingresoNumero()
                
            
            promedio = (ramo_1 + ramo_2 + ramo_3 +  ramo_4) / 4

            alumnos.append({
                "nombre" : nombre,
                "ramo_1" : ramo_1,
                "ramo_2" : ramo_2,
                "ramo_3" : ramo_3,
                "ramo_4" : ramo_4,
                "asistencia" : asistencia,
                "promedio" : promedio
            })
         
        else:
            print("finalizaste el proceso")
            return alumnos
            break

##funcion para ingreso de una nota
def ingresoNumero ():
    while True:
            nota = int(input(": "))
            if nota >= 1 and nota <= 7:
                return nota
                break
            else:
                print("ingrese una opción valida")

##Iniciando MAIN()
main()

