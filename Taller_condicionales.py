# print("Positivo o negativo")
# nump=int(input("Ingrese un numero: "))
# if nump>=0:
#     print("Positivooo")
# else:
#     print("Negativooo")
# print("Mayor de dos numeros")
# num1=int(input("Ingresa un numero"))
# num2=int(input("Ingresa otro numero"))
# if num1<num2:
#     print("El primer numero es menor")
# elif num1>num2:
#     print("El segundo numero es menor")
# else:
#     print("Los numeros son iguales")
# print("Par o inpar")
# numi=int(input("Ingrese un numero"))
# if numi % 2:
#     print("El numero es inpar")
# else:
#     print("El numero es par")
# print("Numero en 10 a 20")
# num10_20=int(input("Ingresa un numero de 10 a 20"))
# if num10_20<=10:
#     print("Es menor que 10 o es 10")
# elif num10_20>=20:
#     print("El numero esta por encima de 20 o es 20")
# else:
#     print("Esta entre 10 y 20")
# print("Tres numeros cual es el mayor?")
# num1=int(input("Ingresa el numero 3"))
# num2=int(input("Ingresa el numero 5 "))
# num3=int(input("Ingresa el numero 2 "))
# if num1>num2:
#     print("Es menor")
# elif num3>num2:
#     print("Es menor")
# print("EL mayor es",num2)
# print("10% de descuento!!!!")
# producto=float(input("Ingresa el precio del producto de 1.00 a 200.00 dolares"))
# producto2=float(input("Ingresa el precio del producto de 1.00 a 200.00 dolares"))
# op=producto+producto2
# if op<100:
#     print("NO recibes el 10% mal ahi master precio total",op)
# else:
#     prt=op-0.10/op
#     print("Recibes tu descuento",prt)
# # print("Votaciones")
# edad=int(input("Ingresa tu edad"))
# if edad>=18:
#     print("Puede votar")
# else:
#     print("No puede votar")
# print("VIP Broooooooooo")
# precio=int(input("Ingresa la cantidad a pagar"))
# if precio>=1000:
#     prc=0.20/precio
#     print("Optienes vip precio total: ",prc)
# else:
#     print("NO optienes vip")
# vip=input("Eres vip o normal")
# if vip=="vip":
#     print("Puedes pasar a la sala vip")
# else:
#     print("No puedes pasar a la sala vip")
# print("Multiplo de 5 y 3")
# num53=int(input("Ingresa el numero: "))
# op2= (5*(num53//5))-(3*(num53//3))
# if op2==0:
#     print("Es multiplo de 3 y 5")
# else:
#     print("No es multiplo")
# print("Division de 2")
# num53=int(input("Ingresa el numero: "))
# numver1=int(input("Ingresa el numero que se dividira para verificar: "))
# numver2=int(input("Ingresa el numero que se dividira para verificar por segunda vez: "))
# opdx= (numver1*(num53//numver1))-(numver2*(num53//numver2))
# if opdx==0:
#     print(f"Es multiplo de {numver1} y {numver2}")
# else:
#     print("No es multiplo")
# print("Lista que bendicion")
# lista=[]
# lista=(int(input("Ingresa un numero")),int(input("Ingresa un numero")),int(input("Ingresa un numero")),int(input("Ingresa un numero")),int(input("Ingresa un numero")))
# print(lista)
# if lista[2]<=10:
#     print("Es menor o igual a 10")
# else:
#     print("Es meyor o igual a 10")
# print("Numero 7 donde estara")
# lista2=[3, 5, 7, 9]
# if lista2[2]==7:
#     print(f"El numero es {lista2[2]}")
# else:
#     print("el numero no es 7")
# print("Lista sumada")
# lista3=[4, 6, 2, 8]
# suma=lista3[0]+lista3[1]
# if suma<=10:
#     print("suma baja")
# else:
#     print("suma alta")
# print("Lista de la death note (Ejercicio 14)")
# lista4=["Ana","Luis","Pedro","Marta"]
# print(lista4)
# if lista4[3]=="Marta":
#     print("El nombre es marta")
# else:
#     print("EL nombre no es marta")
print("Ejercicio num15")
print("Ejercicio num15")
lista5 = []
for i in range(3):
    color = input("Ingresa un color: ")
    lista5.append(color)

print("Colores ingresados:", lista5)
if "azul" in lista5:
    lista5.remove("azul")  # Elimina la primera ocurrencia de "azul"
    nuevo_color = input("Ingresa un nuevo color para reemplazar 'azul': ")    #algo
    lista5.append(nuevo_color)
else:
    print("Todo está bien")

print("Lista final:", lista5)
