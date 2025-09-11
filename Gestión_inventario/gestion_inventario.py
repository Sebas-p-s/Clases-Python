Menu_empresarial =('''
===== MENÚ DE INVENTARIO EMPRESARIAL ====
    
    1. Registrar producto
    2. Mostrar inventario
    3. Calcular valor total del inventario
    4. Buscar producto
    5. Registrar venta
    6. Salir                   
                                    
''')
opt_menu = True
lista_productos = []
valor_cal_total = ""
def registrar_producto():
    opt_registrar = True
    while opt_registrar:
        retornar = ""
        producto = str(input("Ingrese el producto a registrar: ")).capitalize()
        producto not in lista_productos
        cantidad = int(input(f"Ingrese la cantidad de {producto}, cantidad: "))
        precio_u = int(input(f"Ingrese el valor unitario de {producto}, valor: "))
        lista_productos.append({"producto": producto , "cantidad": cantidad , "precio_u": precio_u})
        while retornar not in ("Si" , "No"):
            retornar = str(input("¿Desea agregar otro producto?(si o no): ")).capitalize()
            if retornar == "Si":
                pass
            elif retornar == "No":
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
        buscar_producto = str(input("Escriba el producto al cual quiera calcularle su valor total: ")).capitalize()
        for producto in lista_productos:
            if buscar_producto == producto['producto']:
                valor_cal_total = (producto['cantidad'] * producto['precio_u'])
                print(f" {buscar_producto} vale en total {valor_cal_total},00$")
                retornar = ""
            elif buscar_producto != producto['producto']:
                print("Producto no encontrado")
        while retornar not in ("Si" , "No"):
            retornar = input(("¿Desea buscar otro valor total?(si o no): ")).capitalize()
            if retornar == "Si":
                retornar = "Si"
            elif retornar == "No":
                retornar = "No"
                print("Saliendo del programa")
                opt_valortotal = False
            else:
                print("Opción no reconocida")

def buscar_producto_fun():             
    opt_buscar_producto =True
    while opt_buscar_producto:
        producto_buscado = str(input("Ingrese el producto que desea buscar: ")).capitalize()
        for producto in lista_productos:
            if producto_buscado == producto['producto']:
                valor_cal_total = producto['precio_u'] * producto['cantidad']
                print(f'''
                    Producto: {producto['producto']}
                    Precio Unitario: {producto['precio_u']}
                    Cantidad: {producto['cantidad']}
                    Valor Total: {valor_cal_total}$
                    ''')
            else:
                print("Producto no encontrado")
        retornar = str(input("¿Quiere buscar otro producto?(si o no): ")).capitalize()
        if retornar in ("Si", "No"):
            if retornar == "Si":
                pass
            elif retornar == "No":
                opt_buscar_producto = False
                print ("Regresando al menu empresarial")
            else:
                print("Opción no reconocida")

def registrar_venta():
    opt_registrar_venta = True
    producto_buscado = input("Ingrese el producto el cual va a vender: ").capitalize()
    for producto in lista_productos:
        if producto_buscado == producto['producto']:
            cant_vender = int(input("Ingrese la cantidad a vender: "))
            if producto['cantidad'] >= cant_vender:
                producto['cantidad'] = (producto['cantidad'] - cant_vender)
                resultado_total = (producto['cantidad'] * producto['precio_u'])
                print(f"Vendiste {producto['producto']} en {cant_vender * producto['precio_u']}$")
                print(f"{producto['producto']} quedaron {producto['cantidad']} y el valor total de que queda es {resultado_total}$.")
            elif producto['cantidad'] < cant_vender:
                print(f"No se pueden restar {producto['cantidad']}" f" - {cant_vender}, no existen productos negativos")
                

        
while opt_menu:
    print(Menu_empresarial)
    selector_menu = input("Seleccione alguna opción :")
    if selector_menu == "1":
        registrar_producto()
    elif selector_menu == "2":
        listar()
    elif selector_menu == "3":
        valor_total()
    elif selector_menu == "4":
        buscar_producto_fun()
    elif selector_menu == "5":
        registrar_venta()
    elif selector_menu == "6":
        opt_menu = False
        print("Hasta Pronto")
