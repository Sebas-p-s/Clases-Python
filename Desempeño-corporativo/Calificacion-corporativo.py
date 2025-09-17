##Creo primero la funcion para que el usuario registre a los empleados, tendra un opt para el usuario registre los empleados que quiera y no solo uno y tenga que regresar con el menu.
##creare una tupla para que la lista de despeños este en uan sola linea
lista_de_los_desempenos = ("Calidad","Puntualidad","Colaboracion","Eficiencia")
empleados_desempenos = []
promedios = {}
lista_promedios = []
def registar_empleados():
    opt_registrar_empleados = True
    while opt_registrar_empleados:
        nombre_empleado = str(input("Ingrese el nombre del empleado: ")).capitalize()
        empleado = {'Nombre' : nombre_empleado}
        if not nombre_empleado:
            print("No ingreso valores vacios.")
        else:
            for i in lista_de_los_desempenos:
                respuesta = -1

                while respuesta <= 0 or respuesta > 10:
                    respuesta = (float(input(f"Ingrese el puntaje de {nombre_empleado} basado en su {i}: ")))
                    if respuesta <= 0 or respuesta > 10:
                        print("Dato no valido")  
                ##Esto lo que hara sera unir la respuesta a el diccionario empleado ejemplo: empleado['calidad']= 8.5
                empleado[i] = respuesta
            empleados_desempenos.append(empleado)
        salir = ""
        while salir not in ("Si", "No"):
            salir = str(input("¿Desea salir?(Si/No): ")).capitalize()
            if salir == "Si":
                opt_registrar_empleados = False
                print("Regresando al menu.")
            elif salir == "No":
                pass
            else:
                print("Respuesta no valida.")

def calcular_promedios():
    if empleados_desempenos:
        for empleado in empleados_desempenos:
            suma_promedios = 0
            promedio = 0
            for categoria in lista_de_los_desempenos:
                suma_promedios += empleado[categoria]
            promedio = suma_promedios / len(lista_de_los_desempenos)
            promedio = round(promedio, 1)
            promedios[empleado['Nombre']] = promedio
            lista_promedios.append(promedio)
        indi = 0
        for i in promedios:
            print(f"{i} : {lista_promedios[indi]}")
            indi += 1
                       
    else: 
        print("No hay ningun dato")

registar_empleados()
calcular_promedios()
        
        
                    
                


    