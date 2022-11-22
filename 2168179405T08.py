import signal
import sys,os
import time

productos= [
        {
            "nombre":"Tortilla",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Coca-cola",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Pepsi",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Huevo",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Rancheritos",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Sabritas",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Fanta",
            "unidades":0,
            "c_compra":8,
            "vendido":int(),
        },
        {
            "nombre":"Ciel",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Carlos V",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Snicker",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Bubalo",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Fritos",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Doritos",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Chips",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Frijoles",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Panditas",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Tostitos",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Chetos",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Barritas",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        },
        {
            "nombre":"Gansito",
            "unidades":0,
            "c_compra":0,
            "vendido":int(),
        }
    ]

def agregar_articulo(productos):
    
    #funcion para agregar articulo
    nuevo_producto = input("introduce el nombre de tu articulo\n")
    unidades = input ("introduce las unidades\n") 
    costo = input ("introduce el costo de compra\n")
    productos.append({
            "nombre":nuevo_producto,
            "unidades":unidades,
            "c_compra":costo,
            "vendido":int(),
        })
    print("Se han realizado los cambios, este es el nuevo inventario.")
    i=0
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    input("presiona enter para volver")

def editar_articulo(productos):
    
    #funcion para editar articulo
    p=str()
    i=0
    print("Inventario actual.")
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto a editar:\n> ")
        if not p.isdecimal() or int(p) not in range(1, len(productos)+1):
            print('Introduce un numero valido.')
            continue
        else:
            p = int(p) - 1
            break
    nuevo_producto = input("introduce el nombre de tu articulo\n")
    unidades = int(input ("introduce las unidades\n")) 
    costo = int(input ("introduce el costo de compra\n"))
    productos[p]["nombre"]=nuevo_producto
    productos[p]["unidades"]=unidades
    productos[p]["c_compra"]=costo
    print("Se han realizado los cambios, este es el nuevo inventario.")
    i=0
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    input("presiona enter para volver")

def eliminar_articulo(productos):
    #funcion para eliminar articulos
    p=str()
    i=0
    print("Inventario actual.")
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto a eliminar:\n> ")
        if not p.isdecimal() or int(p) not in range(1, len(productos)+1):
            print('Introduce un numero valido.')
            continue
        else:
            p = int(p) - 1
            break
    del productos[p]
    print("Se han realizado los cambios, este es el nuevo inventario.")
    i=0
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    input("presiona enter para volver")

def mostrar_inventario(productos):
    #funcion para mostrar inventario
    i=0 
    valor_venta=0
    print("Inventario actual.")
    for producto in productos:
        valor_venta = productos[i]['c_compra']+(productos[i]['c_compra']*.15)
        i +=1
        print("{}) {}./ unidades = {}./ costo de compra = {}./ valor de venta {} . ".format(i, producto["nombre"], producto["unidades"], producto["c_compra"] , valor_venta))
    input("presiona enter para volver")

def eliminar_agregar(productos):
    while True:
        os.system("cls")
        print("Que deseas hacer? \n1)Eliminar articulo \n2)Editar articulo \n3)Agregar articulo \n4)Volver al menu")
        opcion= input("\n :\n> ")
        # Validando opcion deseada
        if opcion == "1":
            #eliminar articulo
            eliminar_articulo(productos)
        elif opcion == "2":
            #Editar articulo
            editar_articulo(productos)
        elif opcion == "3":
            #agregar articulo
            agregar_articulo(productos)
        elif opcion == "4":
            menu()
        else:
            input("Opcion no valida intenta de nuevo")
            os.system("cls")

def vender_articulo(productos):
    
        #Funcion para vender articulo

    v=0
    p=str()
    i=0
    unidad=0
    print("Inventario actual.")
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto a vender:\n> ")
        if not p.isdecimal() or int(p) not in range(1, len(productos)+1):
            print('Introduce un numero valido.')
            continue
        else:
            p = int(p) - 1
            break
    while True:
        unidad= input("Cuantos {} quieres vender, actualmente hay: {}\n>".format(productos[p]['nombre'], productos[p]['unidades']))
        if not unidad.isdecimal() or int(unidad) > productos[p]['unidades']:
            print('Introduce un numero entero.(no se pueden vender mas productos de los que hay en existencia)\n>')
            continue
        else:
            unidad= int(unidad)
            break
    productos[p]['unidades'] -= unidad
    productos[p]['vendido']  += unidad
    valor_venta= (productos[p]['c_compra']+productos[p]['c_compra']*.15)*unidad
    input("Se han realizado los cambios, este es el inventario actual, {}: {} y se han vendido {}, tu ganancia fue de {}\
        \nPresiona enter para volver al menu".format(productos[p]['nombre'], productos[p]['unidades'], productos[p]['vendido'], valor_venta))

def salir(signal=None,frame=None):
    #funcion para salir
    print("programa terminado")
    sys.exit(0)

def agregar_inventario(productos):

    #funcion para llenar inventario

    p=str()
    i=0
    unidad=0
    print("Inventario actual.")
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto a agregar:\n> ")
        if not p.isdecimal() or int(p) not in range(1, 21):
            print('Introduce un numero del 1 al 20.')
            continue
        else:
            p = int(p) - 1
            break
    while True:
        unidad= input("Cuantas {} quieres agregar, actualmente hay: {}\n>".format(productos[p]['nombre'], productos[p]['unidades']))
        if not unidad.isdecimal():
            print('Introduce un numero entero.\n>')
            continue
        else:
            unidad= int(unidad)
            break
    productos[p]['unidades'] += unidad
    input("Se han realizado los cambios, este es el inventario actual, {}: {}.\n Presiona enter para volver al menu".format(productos[p]['nombre'], productos[p]['unidades']))

def agregar_costo(productos):
    
        #Funcion para llenar los costos

    p=str()
    i=0
    unidad=0
    print("Inventario actual.")
    for producto in productos:
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto al cual agregaras costo:\n> ")
        if not p.isdecimal() or int(p) not in range(1, len(productos)+1):
            print('Introduce un numero del 1 al 20.')
            continue
        else:
            p = int(p) - 1
            break
    while True:
        unidad= input("Que costo quieres agregar a {}, actualmente su costo es: {}\n>".format(productos[p]['nombre'], productos[p]['c_compra']))
        if unidad.isalpha() or unidad in ['','\n']:
            print('Introduce un numero.\n>')
            continue
        else:
            unidad= float(unidad)
            break
    productos[p]['c_compra'] = unidad
    input("Se han realizado los cambios, este es el inventario actual, {} Costo: {},\nPresiona Enter para volver al menu.".format(productos[p]['nombre'], productos[p]['c_compra']))

def calcular_ventas(productos):
     
        #Función para calcular ventas

    p=str()
    i=0
    h=0
    unidad=0
    print("Inventario actual.")
    for producto in productos:
        h += productos[i]['vendido']*(productos[i]['c_compra']+productos[i]['c_compra']*.15)
        i +=1
        print("{}) {}".format(i, producto["nombre"]))
    while True:
        p= input("\nSelecciona el producto del que quieres calcular ventas:\n> ")
        if not p.isdecimal() or int(p) not in range(1, len(productos)+1):
            print('Introduce un numero del 1 al 20.')
            continue
        else:
            p = int(p) - 1
            break
    precio_unitario= productos[p]['c_compra']+productos[p]['c_compra']*.15
    ganancia_total= precio_unitario*productos[p]['vendido']
    productos[p]['unidades'] += unidad
    input("Se han vendido {} de {} a un precio de {} y tu ganancia total de este producto ha sido de {}, las ganancias en general son de {} \n Presiona enter para volver al menu".format(productos[p]['vendido'], productos[p]['nombre'],precio_unitario, ganancia_total,h))

def menu():
    
    
       # Menu para venta de articulos
    
    signal.signal(signal.SIGINT, salir)
    opcion=str()
    while True:
        os.system("cls")
        print("""1) Agregar Unidades\n2) Aregar Costo de Compra\n3) Calcular ventas\n4) Vender articulo\n5) Salir\n6) Mostrar inventario\n7) Agregar, editar o eliminar aritculo""")
        opcion= input("\n \n> ")

        # Validando opcion deseada
        if opcion == "1":
            # Agregar producto
            agregar_inventario(productos)
        elif opcion == "2":
            #Agregar costo de compra.
            agregar_costo(productos)
        elif opcion == "3":
            #calcular ventas
            calcular_ventas(productos)
        elif opcion == "4":
            #vender articulo
            vender_articulo(productos)
        elif opcion == "5":
            #salir del programa al menu principal.
            salir()
        elif opcion == "6":
            #mostrar inventario
            mostrar_inventario(productos)
        elif opcion == "7":
            eliminar_agregar(productos)
            #agregar o eliminar a
        else:
            input("Opcion no valida intenta de nuevo")
            os.system("cls")
    
    
menu()