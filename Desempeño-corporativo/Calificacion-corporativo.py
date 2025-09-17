##Creo primero la funcion para que el usuario registre a los empleados, tendra un opt para el usuario registre los empleados que quiera y no solo uno y tenga que regresar con el menu.
##creare una tupla para que la lista de despeños este en uan sola linea
lista_de_los_desempenos = ("Calidad","Puntualidad","Colaboracion","Eficiencia")
empleados_desempenos = []
promedios = {}
lista_promedios = []
lista_clasificacion = []

def registar_empleados():
    opt_registrar_empleados = True
    print("Solo podra salir cuando registre minimo 3 empleados")
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
        indice = 0
        for i in empleados_desempenos:
            indice += 1
            if 3 <= indice:
                while salir not in ("Si", "No"):
                    salir = str(input("¿Desea salir?(Si/No): ")).capitalize()
                    if salir == "Si":
                        opt_registrar_empleados = False
                        print("Regresando al menu.")
                    elif salir == "No":
                        pass
                    else:
                        print("Respuesta no valida.")
##Esta funcion sirve para que se calcule el promedio el cual usaremos despues.
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
    else: 
        print("No hay ningun dato")
## Ya con el promedio podremos clasificarlos y guardalos para usarlos despues.        
def clasificar_desempeno():
    if not empleados_desempenos:
        print("No hay ningun empleado registrado")
    else:
        calcular_promedios()
        for i in lista_promedios:
            if i < 5:
                clasificado = "Bajo"
                lista_clasificacion.append(clasificado)
            elif 5 <= i < 8.5:
                clasificado = "Aceptable"
                lista_clasificacion.append(clasificado)
            elif 8.5 <= i <= 10:
                clasificado = "Sobresaliente"
                lista_clasificacion.append(clasificado)
            print(lista_promedios)
            print(lista_clasificacion)
                
            
registar_empleados()
clasificar_desempeno()
        
        
                    
                


    