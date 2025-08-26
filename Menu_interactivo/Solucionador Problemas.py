# Declarar variable
afirmacion = True
mensaje = '''
___________________________________________
|                                         |
|    Primer menu de opciones              |   
|         en python                       |
|_________________________________________|
|                                         |
|      1.Programa de suma                 |
|      2.Programa de notas                |
|      3.Promgrama de retiro de cajero    |
|      4.Gestor de tareas                 |
|      5.Salir                            |
|_________________________________________|
'''
men_sum =(''' 
Escriba dos numeros para hacer su suma, Ejemplo:
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|             A       +        B            |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|      
''')
men_intentar = "¿Quiere seguir en el programa?(si o no), si sale se le regresara al menu"
men_caje = '''
___________________________
|__________________________|
|                          |
| Bienvenido al Cajero     |
|   Automatico             |
|                          |
|                          |
|__________________________|
||      | 1 | 2 | 3 |      |
||      | 4 | 5 | 6 |      |
||      | 7 | 8 | 9 |      |
||_________________________|
||      -------------      |
||                   _____ |
||_________________________|
'''

men_gestor = ('''
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■                           ■    
■     Bienvenido a su       ■    
■     Gestor de Tareas      ■
■                           ■
■                           ■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
              
              
''')
men_gestor2 =('''
__________________________________
|Menu                            |
|--------------------------------|
|                                |
|  1.Crear tarea                 |
|  2.Ver lista de tareas         |
|  3.Eliminar tarea              |
|  4.Cambiar estado de la tarea  |
|  5.Salir                       |
|                                |
|________________________________|         
              
              
              
''')
def suma(num1 , num2):
    resultado = num1 + num2
    print(f"la suma de {num1} + {num2} = {resultado}")

calificacion = 0
def notas():
    clases = ["Español" , "Ingles", "Informatica","Biologia","Educacion fisica","Electronica","Danzas",
         "Artes","Musica","Contabilidad"]
    divisor = 0
    calificacion = 0
    for i in clases:
        nota = float(input(f"Ingrese la nota de {i} "))    
        divisor = divisor + 1
        calificacion = calificacion + nota
    prome = calificacion / divisor
    print(f"El promedio de sus notas son: {prome}")  

def cajero():
    esta_cajero = True
    tarjeta = ""
    contrasena = ""
    contrasena_intro = ""
    respuesta_cajero = ""
    while esta_cajero:
        print(men_caje)
        contrasena = int(input("Defina su contraseña numerica: "))
        while tarjeta != "tarjeta":
            tarjeta = (str(input("Ingrese su tarjeta debito o credito(Escriba -tarjeta-): ")))
            if tarjeta != "tarjeta":
                respuesta_cajero = str((input("No ha ingresado tarjeta, ¿Desea salir del programa?(si o no): " )))
                if respuesta_cajero != ("si" , "no"):
                    while respuesta_cajero not in ("si" , "no"):
                        respuesta_cajero = str((input("No ha ingresado tarjeta, ¿Desea salir del programa?(si o no): " )))
                if respuesta_cajero == "no":
                    pass
                if respuesta_cajero == "si":
                    esta_cajero = False
                    break
        if tarjeta == "tarjeta":
            while contrasena_intro != contrasena:
                contrasena_intro = int(input("Introduzca su contraseña: "))
                if contrasena_intro != contrasena:
                    print("Contraseña no coincide")
                    respuesta_cajero = str((input("¿Desea salir del programa?(si o no): " )))
                    while respuesta_cajero not in ("si" , "no"):
                        respuesta_cajero = str((input("¿Desea salir del programa?(si o no): " )))
                        if respuesta_cajero == "no":
                            pass
                        if respuesta_cajero == "si":
                            esta_cajero = False
                            break
            if contrasena_intro == contrasena:
                dinero = int(input("Introduzca el dinero que desea retirar: "))
                print(f"Usted ha retirado {dinero}$.")
                respuesta_cajero = str((input("¿Desea salir del programa?(si o no): " )))
                while respuesta_cajero not in ("si" , "no"):
                        respuesta_cajero = str((input("¿Desea salir del programa?(si o no): " )))
                        if respuesta_cajero == "no":
                            pass
                        if respuesta_cajero == "si":
                            esta_cajero = False
                            break

def gestor_tareas():
    gestor_afirmacion = True
    lista_tareas = []
    while gestor_afirmacion:
        print(men_gestor2)
        respuesta_gestor = int(input("Escoja una opción: "))
        if respuesta_gestor == 1:
            while respuesta_gestor == 1:
                tareas = input("Ingrese tareas a completar: ")
                tareas_estado = str(input("Ingrese el estado de la tarea: "))
                lista_tareas.append({"tareas":tareas, "tareas_estado":tareas_estado})
                preg_gestor = str(input("¿Desea regresar al menu?(si o no): "))
                if preg_gestor == "si":
                    respuesta_gestor = 0
                if preg_gestor == "no":
                    pass
        if respuesta_gestor == 2:
            nu = 1
            for i in lista_tareas:
                    print(f'''{nu}. |{i['tareas']}| su estado es |{i['tareas_estado']}| 
                        ''')
                    nu = nu + 1
        if respuesta_gestor == 3:
            eliminar= int(input("Ingrese el numero de la tarea a eliminar: "))
            lista_tareas.pop(eliminar - 1)
        if respuesta_gestor == 4:
            indice = int(input("Ingrese numero de la tarea para cambiar estado: "))
            indice = indice - 1
            nuevo_estado = str(input("Ingrese el estado de su tarea: "))
            lista_tareas[indice]['tareas_estado'] = nuevo_estado
            print(f"El estado de {lista_tareas[indice]['tareas']} ha cambiado a {lista_tareas[indice]['tareas_estado']}.")
        if respuesta_gestor == 5:
            gestor_afirmacion = False
                
                
                
while afirmacion:
    print(mensaje)
    
    opt = int(input("Seleccione una opción: "))
    
    if opt == 1:
        while opt == 1:
            print("Programa de suma")
            print(men_sum)
            num1 = int(input("Ingrese valor A: "))
            num2 = int(input("Ingrese valor B: "))
            suma(num1 ,  num2)
            print(men_intentar)
            respuesta = str(input())
            if respuesta == "si":
                opt = 1
            elif respuesta == "no":
                opt = 2
    elif opt == 2:
        while opt == 2:
            print("Programa de notas")
            notas()
            print(men_intentar)
            respuesta = str(input())
            if respuesta == "si":
                opt = 2
            else:
                opt = 3
    elif opt == 3:
        print("Programa de retiro cajero")
        cajero()
    elif opt == 4:
        print("Gestor de tareas")
        gestor_tareas()
    elif opt == 5:
        print('''
              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
              ⏹︎¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⏹︎
              ⏹︎ Gracias por usar mi programa       ⏹︎
              ⏹︎  "Solucionador Problemas".         ⏹︎
              ⏹︎ Hecho por: Sebastian Pachon        ⏹
              ⏹︎                                    ⏹
              ⏹︎¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤⏹︎
              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
              
              ''')
        afirmacion = False
    else:
        print("Opción no valida, eliga una opción del 1 al 5.")