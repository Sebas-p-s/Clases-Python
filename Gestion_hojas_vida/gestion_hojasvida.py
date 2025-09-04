Menu = ('''
  _______________________________       
 (_______________________________) 
 |                               |
 |1. Registrar oferta laboral    |
 |2. Lista ofe laboral           |
 |3. Registrar candidatos        |
 |4. Lista candidatos            |
 |5. Agregarle perfil laboral    |
 |6. Lista perfiles laborales    |
 |7. Salir                       |
 |_______________________________|
 (_______________________________)       
        ''')

ofertas = []
candidatos = []
lista_final = []
opt_menu = True
def registrar_ofe_lab():
    opt_ofe_lab = True
    while opt_ofe_lab:
        opt_salir = True
        oferta_lab = input("Ingrese la oferta laboral: ")
        if oferta_lab in ("" , " "):
            print("No ingrese ofertas vacias")
        else:
            ofertas.append(oferta_lab)
        while opt_salir :
            salir = str(input("¿Desea salir?(Si/No): ")).capitalize()
            if salir == "Si":
                print("Saliendo del programa")
                opt_ofe_lab = False
                opt_salir = False
            elif salir == "No":
                opt_salir = False
            else:
                print("Respuesta no valida")
            
def registrar_can():
    opt_reg_ofe = True
    while opt_reg_ofe:
        opt_salir = True
        candidato = str(input("Ingrese el candidato: ")).capitalize()
        edad = int(input("Ingrese la edad: "))
        aprendizaje = str(input("Ingrese en que se especializa el candidato: ")).capitalize()
        candidato = (f"{candidato} tiene {edad} años y tiene conocimientos como {aprendizaje}")
        candidatos.append(candidato)
        print (candidatos)
        while opt_salir:
            salir = str(input("¿Desea salir?(Si/No): ")).capitalize()
            if salir == "Si":
                opt_reg_ofe = False
                opt_salir = False
            elif salir == "No":
                opt_salir = False
            else:
                print("Respuesta no valida")

def lista_ofe_lab():
    num = 1
    for oferta in ofertas:
         print (f"""{num}. {oferta}""")
         num += 1
        
def lista_candidatos():
    num = 1
    for candidato in candidatos:
        print (f"""*{num}. {candidato}""")
        num += 1



def perfil_lab():
    opt_per_lab = True
    while opt_per_lab:
        opt_salir = True
        if candidatos == []:
            print("No hay nada en candidatos")
        elif ofertas == []:
            print("No hay nada en ofertas laborales, retornando al menu")
        else:
            indice_of_lab = int(input("Escriba el numero de la lista de la oferta laboral: "))
            indice_of_lab -= 1
            indice_candidato = int(input("Escriba el numero de la lista de candidatos: "))
            indice_candidato -= 1
            if indice_of_lab < 0:
                print("Numero de oferta no valido")
            if indice_candidato < 0:
                print("Numero de candidato no valido")
            else:
                if indice_candidato >= 0 and indice_of_lab >= 0:
                    lista_final.append({"oferta": ofertas[indice_of_lab] , "candidato": candidatos.pop(indice_candidato)})
        while opt_salir:
            salir = str(input("¿Desea salir?(Si/No): ")).capitalize()
            if salir == "Si":
                opt_per_lab = False
                opt_salir = False
            elif salir == "No":
                opt_salir = False
            else:
                print("Respuesta no valida")

        
def lista_perfil():
    for i in lista_final:
        print(f" La oferta : {i['oferta']} y su candidato: {i['candidato']}")
        
        
while opt_menu:
    print(Menu)
    respuesta = int(input("Ingrese numero del programa: "))
    if respuesta == 1:
        registrar_ofe_lab()
    elif respuesta == 2:
        lista_ofe_lab()
    elif respuesta == 3:
        registrar_can()
    elif respuesta == 4:
        lista_candidatos()
    elif respuesta == 5:
        perfil_lab()
    elif respuesta == 6:
        lista_perfil()
    elif respuesta == 7:
        opt_menu = False
    else:
        print("Respuesta no valida")
    