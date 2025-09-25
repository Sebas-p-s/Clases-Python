## Creo mi lista de diccionarios con los datos suministrados
from numpy.ma.core import indices

datos_suministrados = [ {"Fecha": 2018, "Bogota" :7830, "Antioquia": 6420, "Valle del cauca": 4840},
                        {"Fecha": 2019, "Bogota" :7900, "Antioquia": 6480, "Valle del cauca": 4960},
                        {"Fecha": 2020, "Bogota" :7970, "Antioquia": 6535, "Valle del cauca": 4955},
                        {"Fecha": 2021, "Bogota" :8050, "Antioquia": 6590, "Valle del cauca": 5020},
                        {"Fecha": 2022, "Bogota" :8120, "Antioquia": 6645, "Valle del cauca": 5090} ]

## Aqui creo mi lista de ubicacion la cual servira para usarla despues en un for para no tener que usar introducir la ubicacion por consola
ubicacion = ("Bogota","Antioquia","Valle del cauca")


## Esta era la formula que el profre uso pero no funciono asi que tuve que investigarla en otro lado.
## Tasa_de_Crecimiento=(PfinalPinicial)1n−1Tasa_de_Crecimiento=\left(\frac{P_{final}}{P_{inicial}}\right)^{\frac{1}{n}}-1Tasa_de_Crecimiento=(PinicialPfinal)n1−1

## r = (P_final / P_inicial)^(1/t) - 1. Esta es la nueva formula, r= respuesta t = tiempo, la formula saque buscando tasa de crecimiento compuesto poblacional en internet
## Creo la funcion para que no se tenga que repetir codigo mas adelante
def calcular_tasa(ubicacion):
    p_inicial = datos_suministrados[0][ubicacion]
    p_final = datos_suministrados[4][ubicacion]
    respuesta = (p_final - p_inicial)**(1/5) - 1
    return respuesta
## Aqui creo un diccionario donde tendre los diferentes porcentajes calculados con la ecuacion
dicci_tasas_calculadas = {}

## Aqui creo la funcion donde guardara los resultados ya redondeados de la formula de la tasa acumulado a el diccionario que comente atras
def tasas_calculadas():
    for i in ubicacion:
        calcular_tasa(i)
        tasa = calcular_tasa(i)
        dicci_tasas_calculadas[i] = round(tasa, 2)

datos_calculados = []
def calcular_proyeccion():
    tasas_calculadas()
    datos_calculados_funcion = {}
    for ciudad in ubicacion:
        porcentaje = dicci_tasas_calculadas[ciudad]
        dato_inicial = datos_suministrados[4][ciudad]
        respuesta = dato_inicial * (porcentaje/100)
        respuesta = round(respuesta)
        respuesta_final = respuesta + dato_inicial
        datos_calculados_funcion[ciudad] = respuesta_final


    contador = 0
    if contador == 0 :
        fecha = datos_suministrados[0]["Fecha"]
        fecha += 1
        datos_calculados.append({'Fecha': fecha, **datos_calculados_funcion})
    fecha = datos_calculados[contador]["Fecha"]
    datos_calculados_funcion[contador] = fecha
    while contador < 4:
        if contador == 0 :
            for ciudad in ubicacion:
                porcentaje = dicci_tasas_calculadas[ciudad]
                dato_inicial = datos_calculados[0][ciudad]
                respuesta = dato_inicial * (porcentaje / 100)
                respuesta = round(respuesta)
                respuesta_final = respuesta + dato_inicial
                datos_calculados_funcion[ciudad] = respuesta_final
        elif contador > 0:
            for ciudad in ubicacion:
                porcentaje = dicci_tasas_calculadas[ciudad]
                dato_inicial = datos_calculados[ -1][ciudad]
                respuesta = dato_inicial * (porcentaje / 100)
                respuesta = round(respuesta)
                respuesta_final = respuesta + dato_inicial
                datos_calculados_funcion[ciudad] = respuesta_final
        contador += 1
    print(datos_calculados_funcion)




calcular_proyeccion()