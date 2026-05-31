"Xiaomi Redmi Note 13":109,
    "Motorola G54": 130
}

telefono_total = sum(inventario.values())

compras = {}

def mostrar_menu():
    print("")
    print("==========================")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos teléfonos tiene la tienda")
    print("2: Comprar un teléfono")
    print("3: Mostrar compras")
    print("4: Salir del programa")

def mostrar_inventario():
    print("***** INVENTARIO *****")
    for llave, valor in inventario.items():
        print(f"{llave}: {valor}")
    print("En total tenemos", telefono_total, "teléfonos")
