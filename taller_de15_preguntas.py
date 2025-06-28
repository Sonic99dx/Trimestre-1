# print("Ejercicio 1")
# suma=0
# num1=int(input("ingresa un numero"))
# while num1 != 0:
#     suma += num1
#     num1=int(input("Ingresa otro numero o 0 para directamente terminar"))
# print("La suma es",suma)
# print("Ejercicio 2")
# contraseña=""
# while contraseña != "python123":
#     contraseña=input("Ingresa una contraseña: ")
# print("ontraseña correcta")
# print("Ejercicio 3")
# lista=[]
# producto=input("Ingresa un producto: ")
# while producto.lower() != "fin":
#     lista.append(producto)
#     producto=input("Ingresa un producto: ")
# print("LIsta de compras lista",lista)
# print("Ejercicio 4")
# contador=0
# pares=0
# inpares=0
# while contador<10:
#     num=int(input(f"Ingrese el numero{contador+1}: "))
#     if num % 2== 0:
#         pares+=1
#     else:
#         inpares+=1
#     contador+=1
# print("Pares",pares,"Impares",inpares)
# print("Ejercicio 5")
# notas=[]
# entrada=input("Ingresa una nota de 0 a 5")
# while entrada.lower() != "salir":
#     nota=float(entrada)
#     if 0 <= nota <= 5:
#         notas.append(nota)
#     entrada=input("ingresa otra nota o salir: ")
# if notas:
#     print("promedio:",sum(notas)/len(notas))
# else:
#     print("No se ingresaron notas validas")
# print("Ejercicio 6")
# num=int(input("Ingresa un numero: "))
# i=1
# while i <=10:
#     print(f"{num} x {i} = {num+i}")
#     i += 1
# print("Ejercicio 7")
# num_secreto = 17
# adivina = int(input("Adivina el número secreto jejejeje: "))
# while adivina != num_secreto:
#     if adivina < num_secreto:
#         print("ufff casi pero muy bajo.")
#     else:
#         print("requete cerca pero muy alto.")
#     adivina = int(input("Intenta de nuevo :( "))
# print("¡Siiiiiiiiii es Correcto!")
# print("Ejercicio 8")
# frutas = ("manzana", "pera", "uva", "banana", "kiwi","sandia")
# fruta = input("Adivina la fruta: ")
# while fruta.lower() not in frutas:
#     fruta = input("Incorrecto, intenta otra fruta: ")
# print("¡Acertaste!")
# print("Ejercicio 9")
# diccionario = {"gato": "cat","perro": "dog","casa": "house","libro": "book","sol": "sun"}
# palabra = input("Ingresa una palabra sencilla en español: ")
# while palabra != "salir":
#     if palabra in diccionario:
#         print("Traducción:", diccionario[palabra])
#     else:
#         print("Palabra no encontrada.")
#     palabra = input("Ingresa otra palabra o 'salir': ")
# print("Ejercicio 10")
# while True:
#     print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
#     opcion = input("Elige una opción: ")
#     if opcion == "5":
#         break
#     a = float(input("Ingresa el primer número: "))
#     b = float(input("Ingresa el segundo número: "))
#     if opcion == "1":
#         print("Resultado:", a + b)
#     elif opcion == "2":
#         print("Resultado:", a - b)
#     elif opcion == "3":
#         print("Resultado:", a * b)
#     elif opcion == "4":
#         if b != 0:
#             print("Resultado:", a / b)
#         else:
#             print("No se puede dividir por cero.")
# print("Ejercicio 11")
# personas = {}
# nombre = input("Ingresa un nombre o salir: ")
# while nombre.lower() != "salir":
#     edad = int(input(f"Ingrese la edad de {nombre}: "))
#     personas[nombre] = edad
#     nombre = input("Ingresa otro nombre o salir: ")
# print("Registro de edades:", personas)
# print("Ejercicio 12")
# colores = ["rojo", "azul", "verde", "amarillo", "negro"]
# color = input("Adivina un color son 5 encuentra 1: ")
# while color.lower() not in colores:
#     color = input("No está, intenta con otro: ")
# print("¡Color encontrado!")
# print("Ejercicio 13")
# num = int(input("Ingresa un número: "))
# i = 1
# while i <= 5:
#     print(f"{num}^{i} = {num**i}")
#     i += 1
# print("Ejercicio 14")
# cuadrados = []
# i = 0
# while i < 5:
#     num = int(input(f"Ingresa el número {i+1}: "))
#     cuadrados.append(num ** 2)
#     i += 1
# print("Cuadrados:", cuadrados)
print("Ejercicio 15")
estudiantes = {}
nombre = input("Ingresa nombre del estudiante (o 'fin'): ")
while nombre.lower() != "fin":
    nota = float(input(f"Ingrese la nota final de {nombre}: "))
    estudiantes[nombre] = nota
    nombre = input("Ingresa otro nombre (o 'fin'): ")
print("Estudiantes y sus notas:", estudiantes)
