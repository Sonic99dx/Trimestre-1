clientes=["Sofia","Andres","Camilo"]
productos=["Celular","Portatil","Tablet"]
print(clientes)
print(productos)
if "Camilo" in clientes:
    clientes.append("Valeria")
    print(clientes)
else:
    print("Camilo no esta")
if "Tablet" in productos:
    productos.append("Impresora")
    print(productos)
else:
    print("La tablet no se encuentra")
if "Andres" in clientes:
    clientes.remove("Andres")
    print(clientes)
else:
    print("Andres no esta")
if len(productos)>3:
    productos.remove(productos[0])
    print(productos)
else:
    print("No hay mas de tres productos, todo esta bien")
if "Celular" in productos:
    print("Celular todavia se encuentra")
else:
    productos.append("Smartwatch")
    print(productos)
if "Valeria" in clientes:
    nuevo_cliente=("Valeria","Impresora")
    print(nuevo_cliente)
else:
    print("Valeria no esta")
destacados=["Sofia","Camilo"]
inventario=["Impresora","Smartwatch"]
print(destacados)
print(inventario)
if "Smartwatch" in inventario:
    productos.append("Accesorios")
    print(productos)
if "Sofia" in destacados:
    ficha_clientes={"nombre":"Sofia","producto":"Portatil","activo":"True"}
    print(ficha_clientes)
    if "ficha_clientes" in locals:
         ficha_clientes["frecuencia"]="Mensual"
         print(ficha_clientes)        