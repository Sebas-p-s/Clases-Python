#Documentacion o algo asi
#Se crea el menu para que el usuario no se pierda y sepa los comandos
menu = ("""
    ____________________________________   
   [                                    ]         
   [        Adopta tu mascota :3        ]    
   [____________________________________]   
   [                                    ]
   [ 1. Ingresa el animal               ]     
   [ 2. Adopta tu mascota               ]     
   [ 3. Ver los animales adoptados      ]     
   [ 4. Ver los animales no adoptados   ]
   [ 5. Salir                           ]     
   [____________________________________]          
    """)
#Creo el opt que me servira para usarlo con el while, asi para que muestre mi menu hasta que el usuario se salga del programa
opt_menu = True
#Se crea una lista de animales, junto al mensaje que mostrara cuando algun dato no cumpla. Ademas una lista animales adoptados para si se quiere ver
lista_animales = []
animales_adoptados =[]
mensaje_no_valido = "Dato no valido"
#Definimos una función crear mascota para ser llamada mas tarde en el menu
def crear_mascota():
    nombre = str(input("Ingrese el nombre que tiene el animal: ")).capitalize()
    while not nombre:
        print (mensaje_no_valido)
        nombre = str(input("Ingrese el nombre que tiene el animal: ")).capitalize()
    especie = str(input(f"Ingrese la especie de {nombre}: ")).capitalize()
    while not especie:
        print(mensaje_no_valido)
        especie = str(input(f"Ingrese la especie de {nombre}: ")).capitalize()
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    while edad < 1 :
        print(mensaje_no_valido)
        edad = int(input(f"Ingrese la edad de {nombre}: "))
    while edad > 100:
        print(mensaje_no_valido)
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        edad 
    energia = str(input(f"Ingrese la energia de {nombre}(alta,media,baja): ")).capitalize()
    while energia not in ("Alta" , "Media" , "Baja"):
            print(mensaje_no_valido)
            energia = str(input(f"Ingrese la energia de {nombre}(alta,media,baja): ")).capitalize()
    compatible_ninos = str(input(f"¿{nombre} es compatible con niños? (Si/No): ")).capitalize()    
    while compatible_ninos not in ("Si" , "No"):
        print(mensaje_no_valido)
        compatible_ninos = str(input(f"¿{nombre} es compatible con niños? (Si/No): ")).capitalize()
    lista_animales.append({'Nombre': nombre, 'Especie' : especie , 'Edad': edad , 'Energia' : energia , 'Compatible con niños' : compatible_ninos})
    print(f"{nombre} fue puesto en adopción.")

# Aca creamos una funcion para que el usuario ingrese sus preferencias
def preferencias():
    if lista_animales:
        usuario = str(input("Ingrese su nombre de usuario para adoptar: ")).capitalize()
        while not usuario:
            print(mensaje_no_valido)
            usuario = str(input("Ingrese su nombre de usuario para adoptar: "))
        especie_buscada = str(input("Ingrese la especie que busca: ")).capitalize()
        while not especie_buscada:
            print(mensaje_no_valido)
            especie_buscada = str(input("Ingrese la especie que busca: ")).capitalize()
        print("Recuerde, al filtar con la edad buscaremos animales que esten dentro de un rango de 3 años menor o mayor")
        edad_buscada = int(input("Ingrese la edad buscada: "))
        while not edad_buscada:
            print(mensaje_no_valido)
            edad_buscada = int(input("Ingrese la edad buscada: "))
        while edad_buscada < 1 :
            print(mensaje_no_valido)
            edad_buscada = int(input("Ingrese la edad buscada: "))
        energia_buscada = str(input("Ingrese la energia buscada (Baja, Media, Alta): ")).capitalize()
        while not energia_buscada:
            print(mensaje_no_valido)
            energia_buscada = str(input("Ingrese la energia buscada (Baja, Media, Alta): ")).capitalize()
        compatibilidad_buscada = str(input("Ingrese si busca que se compatible con niños (Si/No): ")).capitalize()
        while not compatibilidad_buscada:
            print(mensaje_no_valido)
            compatibilidad_buscada = str(input("Ingrese si busca que se compatible con niños (Si/No): ")).capitalize()
        filtro_de_busqueda(especie_buscada,edad_buscada,energia_buscada,compatibilidad_buscada,usuario)
    elif not lista_animales:
        print("Error, no se ha encontrado animales para adoptar")
        
    
#Aqui cree una funcion para no hacer tan extensa la funcion "Preferencias", ya que seria mucho texto.
#Esta se encarga de filtrar con un contador las coincidencias para mostrarle al usuario si algun animal le puede gustar
def filtro_de_busqueda(especie_buscada,edad_buscada,energia_buscada,compatibilidad_buscada,usuario):
    if lista_animales:
        encontrado = False
        for i in lista_animales:
            respuesta = ""
            contador = 0
            if especie_buscada == i['Especie']:
                contador += 1
            if (edad_buscada - 3) <= i['Edad'] <= (edad_buscada + 3):
                contador += 1
            if energia_buscada == i['Energia']:
                contador += 1
            if compatibilidad_buscada == i['Compatible con niños']:
                contador += 1
            if contador  == 3:
                print(f"{i['Nombre']} cumple casi todos los requisitos pero puede ser de tu agrado.")
                print(f"""Tus requisitos fueron Especie: {especie_buscada} , Edad cercana buscada {edad_buscada} , energia {energia_buscada}
                      y si era compatible con niños: {compatibilidad_buscada}.
                      
                      {i['Nombre']} tiene los siguientes atributos: Especie: {i['Especie']} , Edad: {i['Edad']} , Energia: {i['Energia']} y Compatibilida con niños: {i['Compatible con niños']}
                      
                      Como puedes ver solo no cumple una de tus condiciones.
                      
                      """)
                while respuesta not in ("Si", "No"):
                    respuesta = str(input("¿Aun asi lo deseas adoptar?(Si/No): ")).capitalize()
                    if respuesta == "Si":
                        adoptado = i
                        print(f"Adoptaste a {i['Nombre']}, Felicidades por tu nueva compañia.")
                        lista_animales.remove(i)
                        animales_adoptados.append({'Usuario' : usuario , **adoptado})
                        encontrado = True
                        break
                    if respuesta == "No":
                        print("Verificando si hay otro que cumpla tus caracteristicas")
            if contador == 4:
                print(f"{i['Nombre']} cumple todos los requisitos.")
                print(f"""Tus requisitos fueron Especie: {especie_buscada} , Edad cercana buscada {edad_buscada} , energia {energia_buscada}
                      y si era compatible con niños: {compatibilidad_buscada}.
                      
                      {i['Nombre']} tiene los siguientes atributos: Especie: {i['Especie']} , Edad: {i['Edad']} , Energia: {i['Energia']} y Compatibilida con niños: {i['Compatible con niños']}
                      """)
                while respuesta not in ("Si", "No"):
                        respuesta = str(input("¿Lo deseas adoptar?(Si/No): ")).capitalize()
                        if respuesta == "Si":
                            adoptado = i
                            print(f"Adoptaste a {i['Nombre']}, Felicidades por tu nueva compañia.")
                            lista_animales.remove(i)
                            animales_adoptados.append({'Usuario' : usuario , **adoptado})
                            encontrado = True
                            break
                        if respuesta == "No":
                            print("Le avisaremos si hay algun animal para adoptar.")
    if not encontrado:
        print("Ningun animal cumple la mayoria de lo que pediste.")
                            
#Aqui creamos un lista de animales adoptados para que verifique tus animales                           
def lista_de_adoptados():
    if animales_adoptados:
        print("Aqui la lista de tus animales adoptados:")
        for i in animales_adoptados:
            print(f" Dueño: {i['Usuario']}, Nombre de la mascota: {i['Nombre']}, Especie: {i['Especie']} , Edad: {i['Edad']} , Energia: {i['Energia']} y Compatibilida con niños: {i['Compatible con niños']}.")
    if not animales_adoptados:
        print("No tienes ningun animal adoptado.")
#Creo una lista para ver si hay animales sin adoptar, para que no se tenga que buscar en lo escrito en consola.   
def lista_no_adoptados():
    if lista_animales:
        for i in lista_animales:
            print(f" Nombre: {i['Nombre']}, Especie: {i['Especie']} , Edad: {i['Edad']} , Energia: {i['Energia']} y Compatibilida con niños: {i['Compatible con niños']}.")
    elif not lista_animales:
        print("No hay animales en adopcion.")
    
        
while opt_menu:
    print(menu)
    respuesta_menu = int(input("Ingrese el numero de el programa que quiere ejecutar: "))
    if respuesta_menu == 1:
        crear_mascota()
    elif respuesta_menu == 2:
        preferencias()
    elif respuesta_menu == 3:
        lista_de_adoptados()
    elif respuesta_menu == 4:
        lista_no_adoptados()
    elif respuesta_menu == 5:
        opt_menu = False
        print("Hasta pronto.")
    else:
        print(mensaje_no_valido)
        
        
        