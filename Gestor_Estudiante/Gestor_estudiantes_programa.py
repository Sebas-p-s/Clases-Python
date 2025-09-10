menu =('''
_______________________________
|                             |          
|   Menu gestor estudiantes   |
|_____________________________|                           
|                             |   
| 1. Registrar estudiante     |
| 2. Listar estudiantes       |
| 3. Buscar estudiantes       |
| 4. Calcular promedio        |  
| 5. Salir                    |
|_____________________________|     
''')

estudiantes_lista = []
opt_menu = True
def registrar_estudiante():
    continuar = True
    continuar
    while continuar:
        estudiante = str(input("Ingrese nombre del estudiante: ")).capitalize()
        print(" ")
        asignatura = str(input("Ingrese la asignatura a la que esta inscrito: ")).capitalize()
        print(" ")
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        print(" ")
        estudiante_datos = (estudiante, asignatura, nota)
        estudiante_lista_lo = list(estudiante_datos)
        estudiantes_lista.append({"Nombre": estudiante, "Asignatura": asignatura, "Nota": nota})
        while continuar:
            respuesta = str(input("¿Quiere continuar?(Si/No) ")).capitalize()
            if respuesta == "Si":
                break
            elif respuesta == "No":
                continuar = False
            else:
                print("Respuesta no valida.")
        
def listar_estudiantes():
    if estudiantes_lista:
        indice = 1
        for i in estudiantes_lista:
            print(f"{indice}. {i['Nombre']} , {i['Asignatura']} cuya nota es {i['Nota']}")
            indice += 1
    else:
        print("No hay ningun dato.")

def busqueda_estudiante():
    if estudiantes_lista:
        buscar = str(input("Ingrese el nombre del estudiante: ")).capitalize()
        encontrado = False
        for i in estudiantes_lista:
            if i['Nombre'] == buscar:
                print(f"{i['Nombre']} , {i['Asignatura']} cuya nota es {i['Nota']}, fue encontrado")
                encontrado = True
                break
        if not encontrado:
            print(f"El estudiante {buscar} no esta listado.")
    else: 
        print("No hay ningun dato.")
        
def calcular_prom():
    if estudiantes_lista:
        suma = 0
        indice = 0
        for i in estudiantes_lista:
            suma += i['Nota']
            indice += 1
        respuesta = (suma/indice)
        print(f"El promedio es de {respuesta:.3f}") 
    else:
        print("No hay ningun dato.")
        

while opt_menu:
    print(menu)
    opcion = int(input("Ingrese la opción que desea elegir: "))
    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        listar_estudiantes()
    elif opcion == 3:
        busqueda_estudiante()
    elif opcion == 4:
        calcular_prom()
    elif opcion == 5:
        opt_menu = False
        print("Hasta luego.")
    else:
        print("Respuesta no valida.")

            
            

        
