print("2 letras")
letra1=input("Ingresa una letra").lower()
letra2=input("Ingresa otra letra").lower()
#Igualdad
if letra1 == letra2:
    print("Hay igualdad en las letras")
else:
    print("No hay igualdad")
#Orden alfabetico
if letra1<letra2:
    print(f"Estan en orden alfabetico{letra1} y {letra2}")
elif letra1>letra2:
    print(f"No estan en orden {letra1} y {letra2}")
else:
    print("Error")
#Vocales
vocales=("a","e","i","o","u")
if letra1 in vocales:
    print("La primera letra si califica como vocal")
elif letra2 in vocales:
    print("La segunda letra si califica como vocal")
elif letra1 and letra2 in vocales:
    print("Ambas letras califican como vocales")
else:
    print("Ninguna califica como vocal")