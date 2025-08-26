lista_productos = []
retornar = False
def registrar_producto():
    opt_registrar = True
    while opt_registrar:
        producto = str(input("Ingrese el producto a registrar: "))
        cantidad = int(input(f"Ingrese la cantidad de {producto}, cantidad: "))
        precio_u = float(input(f"Ingrese el valor unitario de {producto}, valor: "))
        lista_productos.append({"producto": producto , "cantidad": cantidad , "precio_u": precio_u})
        continuar = ""
        while continuar not in ("si" , "no"):
            continuar = str(input("¿Desea agregar otro producto?(si o no): "))
            if continuar == "si":
                pass
            elif continuar == "no":
                opt_registrar = False
            else:
                print("Respuesta no valida")
def listar():
    for i in lista_productos:
        print(f''' 
            - Hay {i['producto']} la cantidad es {i['cantidad']} y el precio unitario es {i['precio_u']}$
              ''')
def valor_total():
    print("Bienvenido, en este programa podra el valor total del inventario de un producto")
    opt_valortotal = True
    while opt_valortotal:
        buscar_producto = str(input("Escriba el producto al cual quiera calcularle su valor total: "))
        print (buscar_producto)
        for producto in lista_productos:
            if buscar_producto == producto['producto']:
                valor_cal_total = (f"{producto['cantidad']} * {producto['precio_u']}$")
                print(f" {buscar_producto} vale en total {valor_cal_total}$")
        while retornar not in ("si" , "no"):
            retornar = ("¿Desea buscar otro valor total?(si o no): ").lower()
            if retornar == "si":
                retornar = "si"
            elif retornar == "no":
                retornar = "no"
                print("Saliendo del programa")
                opt_valortotal = False
registrar_producto()
valor_total()