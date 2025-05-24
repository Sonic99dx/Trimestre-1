print("Ejercicio numero 1")
nombre=input("Ingrese el nombre del producto")
cost=float(input("Ingrese el costo del producto"))
cant=int(input("Ingresa la cantidad del producto"))
tupla=(nombre,cost)
print(f"EL producto es{tupla}")
lstp=[tupla,cant]
dc={"producto":lstp}
prt=cant*cost
print(f"El costo de todo es: {prt} y el diccionario es: {dc}")
print("Ejercicio numero 2")
