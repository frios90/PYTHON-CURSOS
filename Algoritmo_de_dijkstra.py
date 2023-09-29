import json
#func para la lectura de un json con estructura de puntos y pesos
#por: Francisco Rios Castillo (Fejhu)

caso_001 = 'casos_de_uso_dijkstra/caso-001.json' # OK
caso_002 = 'casos_de_uso_dijkstra/caso-002.json' # OK
caso_003 = 'casos_de_uso_dijkstra/caso-003.json' # OK
caso_004 = 'casos_de_uso_dijkstra/caso-004.json' # OK 
caso_005 = 'casos_de_uso_dijkstra/caso-005.json' # OK 

def leer_json_con_matriz_de_puntos():
    with open(caso_004, 'r') as archivo: ##Cambiar entre uno de los 5 casos probados.
        contenido = archivo.read()
        datos     = json.loads(contenido)
    return datos
#func para crear un array con los puntos que existen en las coordenadas entregadas
def crear_pre_template_array (datos):
    pre_template_array = []
    for punto in datos:
        if not punto["origen"] in pre_template_array:
            pre_template_array.append(punto["origen"])
        if not punto["destino"] in pre_template_array:
            pre_template_array.append(punto["destino"])
    return pre_template_array
#Func para crear el template auxiliar
def crear_template (pre_template_array):
    template = []
    for punto in pre_template_array:
        template.append({
            "valor" : punto,
            "paso"  : False
        })
    return template
#func para crear la base para la matriz
def crear_base_matriz_dijkstra(pre_template_array):
    matriz_de_Dijkstra = []
    for vector in pre_template_array:
        matriz_de_Dijkstra.append(crear_template(pre_template_array))
    return matriz_de_Dijkstra

#func para encontrar las intersecciones de un punto definitivo
def interseccionesDelPunto (punto_valor):
    inter_origen = filter(lambda p: p["origen"] == punto_valor, datos)
    return inter_origen

#func para encontrar el undice de un punto segun su nombre de destino
def buscar_index_destino (destino) :
    temp_template = template
    for index, punto in enumerate(temp_template):
        if destino == punto["valor"]:
            return index

#func para encontrar el undice de un punto segun su nombre de origen
def buscar_index_origen (origen, template) :
    temp_template = template
    for index, val in enumerate(temp_template):
        if origen == val["valor"]:
            return index

def  buscar_definitivo_ciclo_anterior (ciclo):
    definitivo_anterior = False
    for paso in matriz_de_Dijkstra[ciclo-1]:
        if paso["paso"] and paso["paso"]["definitivo"] == True:
            definitivo_anterior = paso["paso"]
    return definitivo_anterior

def validar_enlace_final (origen, destino):
    for ind, enlace in enumerate(datos):
        if enlace["origen"] == origen  and enlace["destino"] == destino and enlace["extremo"] == "fin":
            if enlace["extremo"] == "fin":
                return True

def obtener_peso_enlace (enlace_consulta):
    for ind, enlace in enumerate(datos):
        if enlace["origen"] == enlace_consulta["origen"]  and enlace["destino"] == enlace_consulta["destino"]:
            return enlace["peso"]

def verFormatoRutaFinal ():
    for index, punto in enumerate(ruta_tomada):
        print("Paso " + str(index+1) + " [ de "+ punto["origen"] +" a "+ punto["destino"] +" = "+str(punto["peso"])+ "] "+ punto["label"])

def verMatrizDeDijkstra():
    formato_final_matriz = []

    for index_formato, formato in enumerate(template):
        formato_final_matriz.append({
            "punto" : formato["valor"],
            "avance" : []
        })
        for paso in matriz_de_Dijkstra:
            for detalle in paso:
                if detalle["valor"] == formato["valor"]:
                    if detalle["paso"]:
                        formato_final_matriz[index_formato]["avance"].append(detalle["paso"]["label"])
                    else:
                        formato_final_matriz[index_formato]["avance"].append("( ∞ )")

    mostrar_matriz(formato_final_matriz)

def mostrar_matriz (formato_final_matriz):
    for mostrar in formato_final_matriz:
        print(mostrar["punto"], end=" |    ")
        for index_avance, avance in enumerate(mostrar["avance"]):
            relleno = " " * (9 - len(avance))
            ajuste = avance + relleno
            print(ajuste, end="|    ")
        print()
#usar func leer_json_con_matriz_de_puntos
datos = leer_json_con_matriz_de_puntos()
#usar func crear_pre_template_array
pre_template_array = crear_pre_template_array(datos)
#ordenar array de puntos
pre_template_array.sort()
#usar func crear_template
template = crear_template(pre_template_array)
#usar func crear_base_matriz_dijkstra
matriz_de_Dijkstra = crear_base_matriz_dijkstra(pre_template_array)

definitivo                 = False #guarda el paso definitivo del ciclo
index_definitivo           = 0 #index del paso definitivo del ciclo
siguiente_definitivo       = False #guarda el paso definitivo del próximo ciclo
index_siguiente_definitivo = 0 #index del paso definitivo del próximo ciclo
buscando_camino            = "en_ruta" #definir final del recorrido > en_ruta, llego, termino
ruta_tomada                = [] #resultado resumido de la ruta tomada

for index, paso in enumerate(matriz_de_Dijkstra):
    peso_siguiente_definitivo = 99999
   
    if index == 0 :
        inter_origen = interseccionesDelPunto(paso[0]["valor"])
        menor_peso   = 0
        for index_inter, inter in enumerate(inter_origen):
            if inter["extremo"] == "inicio":
                menor_peso             = inter["peso"]
                definitivo             = inter
                index_inter_definitivo = index_inter
        detalle_paso = {
            "destino"       : definitivo["destino"],
            "origen"        : definitivo["origen"],
            "peso"          : definitivo["peso"],
            "peso_arrastre" : definitivo["peso"],
            "peso_enlace"   : obtener_peso_enlace(definitivo),
            "definitivo"    : True,
            "label"         : "#("+str(definitivo["peso"])+","+definitivo["origen"]+")#"
        }
        definitivo = detalle_paso
        ruta_tomada.append(definitivo)

        matriz_de_Dijkstra[index][index_inter_definitivo]["paso"] = detalle_paso

        inter_origen = interseccionesDelPunto(paso[0]["valor"])
        for index_inter_2, inter_2 in enumerate(inter_origen):
            if inter_2["destino"] != definitivo["origen"]:
                detalle_paso = {
                    "destino"       : inter_2["destino"],
                    "origen"        : definitivo["origen"],
                    "peso"          : inter_2["peso"],
                    "peso_arrastre" : inter_2["peso"],
                    "peso_enlace"   : obtener_peso_enlace(inter_2),
                    "definitivo"    : False,
                    "label"         : "("+str(inter_2["peso"])+","+definitivo["origen"]+")"
                }

                matriz_de_Dijkstra[index][index_inter_2]["paso"] = detalle_paso

                if inter_2["peso"] < peso_siguiente_definitivo:
                    peso_siguiente_definitivo  = inter_2["peso"]
                    siguiente_definitivo       = detalle_paso
                    index_siguiente_definitivo = index_inter_2

    else:
        if not buscando_camino == "termino":
            if buscando_camino == "llego":
                buscando_camino = "termino"
            ##lleno definitivo anterior como *
            detalle_paso = {
                "destino"       : definitivo["destino"],
                "origen"        : definitivo["origen"],
                "peso"          : definitivo["peso"],
                "peso_arrastre" : definitivo["peso_arrastre"],
                "peso_enlace"   : obtener_peso_enlace(definitivo),
                "definitivo"    : False,
                "label"         : "( * )"
            }
            matriz_de_Dijkstra[index][index_definitivo]["paso"] = detalle_paso

            ##seteo en definitivo actual proveniente del ciclo anterior
            definitivo_anterior = buscar_definitivo_ciclo_anterior(index)
            if definitivo_anterior["destino"] == siguiente_definitivo["origen"]:
                if not validar_enlace_final(siguiente_definitivo["origen"], siguiente_definitivo["destino"]):
                    peso_nuevo_definitivo = siguiente_definitivo["peso_enlace"] + definitivo["peso_arrastre"] ## ???? por aqui va la cosa
                else:
                    peso_nuevo_definitivo = siguiente_definitivo["peso"]
            else:
                peso_nuevo_definitivo = siguiente_definitivo["peso"]

            detalle_paso = {
                "destino"       : siguiente_definitivo["destino"],
                "origen"        : siguiente_definitivo["origen"],
                "peso"          : peso_nuevo_definitivo,
                "peso_arrastre" : siguiente_definitivo["peso"],
                "peso_enlace"   : obtener_peso_enlace(siguiente_definitivo),
                "definitivo"    : True,
                "label"         : "#("  +str(peso_nuevo_definitivo) + "," + siguiente_definitivo["origen"]+")#"
            }
            ruta_tomada.append(detalle_paso)
            index_siguiente_definitivo = buscar_index_destino(siguiente_definitivo["destino"])
            matriz_de_Dijkstra[index][index_siguiente_definitivo]["paso"] = detalle_paso

            definitivo       = detalle_paso ##IMPORTANTO PORQUE ESTO PASA A LA SIGUIENTE COMO *
            index_definitivo = index_siguiente_definitivo
            inter_origen     = interseccionesDelPunto(definitivo["destino"])
            menor_peso       = 0

            for index_inter, inter in enumerate(inter_origen):
                index_llenar = buscar_index_destino(inter["destino"])

                # if (matriz_de_Dijkstra[index][index_llenar]["paso"] and matriz_de_Dijkstra[index][index_llenar]["paso"]["label"] == "( * )"):
                #     ##aqui no hago nada porque lo envie desde la vuelta anterior como una definitivo
                #     pass
                # el
                if not matriz_de_Dijkstra[index][index_llenar]["paso"]:
                    ## 2) si no hay paso (osea, no hay intersección), preguntare por la intersección anterior, pasando un algo o un * segun correspontda o nada --
                    nuevo_peso_interseccion = inter["peso"] + definitivo["peso"]

                    cliclo_enlace_anterior = matriz_de_Dijkstra[index-1][index_llenar]["paso"]
                    if cliclo_enlace_anterior and cliclo_enlace_anterior["peso"] < nuevo_peso_interseccion:
                        detalle_paso = cliclo_enlace_anterior
                    else:
                        detalle_paso = {
                            "destino"       : inter["destino"],
                            "origen"        : inter["origen"],
                            "peso"          : nuevo_peso_interseccion,
                            "peso_arrastre" : siguiente_definitivo["peso"],
                            "peso_enlace"   : obtener_peso_enlace(inter),
                            "definitivo"    : False,
                            "label"         : "(" + str(nuevo_peso_interseccion) + "," + inter["origen"] + ")"
                        }
                    index_destino = buscar_index_destino(inter["destino"])

                    matriz_de_Dijkstra[index][index_destino]["paso"] = detalle_paso

            #Validar puntos vacios actuales en relación a su respectivo del ciclo anterior
            for index_no_inter, no_inter in enumerate(matriz_de_Dijkstra[index]):
                if not no_inter["paso"]:
                    index__previo      = buscar_index_origen(no_inter["valor"], template)
                    paso_matriz_previa = matriz_de_Dijkstra[index-1][index__previo]["paso"]

                    if paso_matriz_previa:
                        index__previo_destino = buscar_index_destino(paso_matriz_previa["destino"])
                        matriz_de_Dijkstra[index][index__previo_destino]["paso"] = paso_matriz_previa

    for index, val in enumerate(matriz_de_Dijkstra[index]):
        if val["paso"] and val["paso"]["peso"] < peso_siguiente_definitivo and not val["paso"]["definitivo"] and not val["paso"]["label"] == '( * )':
            peso_siguiente_definitivo  = val["paso"]["peso"]
            siguiente_definitivo       = val["paso"]
            index_siguiente_definitivo = index

print("############################################")
print("Matriz de Dijkstra")
print("############################################")
verMatrizDeDijkstra()


print("############################################")
print("Resumen de ruta mas corta")
print("############################################")
verFormatoRutaFinal()

