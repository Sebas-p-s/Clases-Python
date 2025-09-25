## Creo mi lista de diccionarios con los datos suministrados.

datos_suministrados = [ {"Fecha": 2018, "Bogota" :7830, "Antioquia": 6420, "Valle del cauca": 4840},
                        {"Fecha": 2019, "Bogota" :7900, "Antioquia": 6480, "Valle del cauca": 4960},
                        {"Fecha": 2020, "Bogota" :7970, "Antioquia": 6535, "Valle del cauca": 4955},
                        {"Fecha": 2021, "Bogota" :8050, "Antioquia": 6590, "Valle del cauca": 5020},
                        {"Fecha": 2022, "Bogota" :8120, "Antioquia": 6645, "Valle del cauca": 5090} ]

## Aqui creo mi lista de ubicacion la cual servira para usarla despues en un for para no tener que usar introducir la ubicacion por consola.
ubicacion = ("Bogota","Antioquia","Valle del cauca")


## Esta era la formula que el profre uso pero no funciono asi que tuve que investigarla en otro lado.
## Tasa_de_Crecimiento=(PfinalPinicial)1n−1Tasa_de_Crecimiento=\left(\frac{P_{final}}{P_{inicial}}\right)^{\frac{1}{n}}-1Tasa_de_Crecimiento=(PinicialPfinal)n1−1
## r = (P_final / P_inicial)^(1/t) - 1. Esta es la nueva formula, r= respuesta t = tiempo, la formula saque buscando tasa de crecimiento compuesto poblacional en internet.

## Creo la funcion para que no se tenga que repetir codigo mas adelante.
def calcular_tasa(ubicacion):
    p_inicial = datos_suministrados[0][ubicacion]
    p_final = datos_suministrados[4][ubicacion]
    t = len(datos_suministrados) - 1 ## Estos son los años que han transcurridos
    tasa = (p_final/p_inicial)**(1/t) - 1
    return tasa

## Aqui creo un diccionario donde tendre los diferentes porcentajes calculados con la ecuacion.
dicci_tasas_calculadas = {}

## Aqui creo la funcion donde guardara los resultados ya redondeados de la formula de la tasa acumulado a el diccionario que comente atras.
def tasas_calculadas():
    for ciudad in ubicacion:
        calcular_tasa(ciudad)
        tasa = calcular_tasa(ciudad)
        dicci_tasas_calculadas[ciudad] = round(tasa, 4)

## En esta lista se creara el diccionario con las proyecciones.
datos_calculados = []

## Esta funcion hara la proyeccion.
def calcular_proyeccion():
    tasas_calculadas()
    ## Aqui le digo que me traiga el ultimo dato o diccionario de la lista que nos brindo el ejercicio, osea el ultimo año.
    ultimo = datos_suministrados[-1]
    for i in range(5):
        ## Aqui hacemos el calculo para que se sume uno a la fecha ya que es la proyeccion del año siguiente.
        nuevo = {"Fecha": ultimo["Fecha"] + 1}
        for ciudad in ubicacion:
            tasa = dicci_tasas_calculadas[ciudad]
            dato_inicial = ultimo[ciudad]
            ## Aqui lo que hago es que calculo la poblacion mas la poblacion que va a crecer.
            ## Ejemplo 100 * 1 = 100, si crecen 10 personas osea el 10% seria 110 personas, entonces 100 * 1.10 = 110 = poblacion mas la que crecio.
            poblacion = dato_inicial * (1 + tasa)
            ## Aqui guardo en el diccionario nuevo las tasas de cada ciudad, los redondeo porque las tasas tienen decimales.
            nuevo[ciudad] = round(poblacion)
        ## Aqui los guardo en forma de lista.
        datos_calculados.append(nuevo)
        ## Hago use la ultima fecha mas arriba para que vuelva a calcular la nueva.
        ultimo = nuevo
    ## Aqui retorna los datos :P
    return datos_calculados

proyecciones = calcular_proyeccion()
for fila in proyecciones:
    print(fila)

def graficar():
    import matplotlib.pyplot as plt
    fechas = [int(fecha["Fecha"]) for fecha in datos_calculados]
    bogota = [dato["Bogota"] for dato in datos_calculados]
    antioquia = [dato["Antioquia"] for dato in datos_calculados]
    valle_d_ca = [dato["Valle del cauca"] for dato in datos_calculados]

    plt.plot(fechas, bogota,marker="s", label="Bogota")
    plt.plot(fechas, antioquia,marker="s", label="Antioquia")
    plt.plot(fechas, valle_d_ca,marker="s", label="Valle del cauca")

    plt.title("Proyeccion")
    plt.xlabel("Año")
    plt.ylabel("Poblacion")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.xticks(fechas)
graficar()