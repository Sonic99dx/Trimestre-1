# x,y,z=1,2,3
# print(x,y,z)
# print(x)
# print(y)
# print(x,y)
# x=10
# z=x+5
# print(z)
# p1,p2,p3="goku","vegeta","saitama"
# print(p1,"vs",p2)
# print(p3,"wins")
# dx="hey que onda"
# dx+=", como estas"
# dx+=", que has echo"
# print(dx)
# mensaje= "goku le gana a moreno"
# buscar=mensaje.find("moreno")
# print(buscar)
# extraccion=mensaje[0:12]
# print(extraccion)
# mensaje="el conocimiento es poder"
# encount1=mensaje.find("conocimiento")
# encount2=mensaje.find("poder")
# print(encount1)
# print(encount2)

# #ejercicio 2 
# mensaje2="la practica hace al maestro"
# encount3=mensaje2.find("practica")
# encount4=mensaje2.find("maestro")
# print(encount3)
# print(encount4)

# #ejercicio 3
# ask=input("escribe una frase")
# ask2=input("dime que buscar en el texto")
# print(ask.find(ask2))

#ejercicio 3-1
# text=("El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire.")
# print(text.find("oeste"))
# print(text.find("cactus"))
# print(text.find("admirar"))
# print(text[50:600])

#notas
nombre=input("escribe el nombre del estudiante")
nota=float(input("coloca una nota de 1.0 a 5.0"))
nota1=float(input("coloca una nota de 1.0 a 5.0"))
nota2=float(input("coloca una nota de 1.0 a 5.0"))
mul1=nota*20
mul2=nota1*30
mul3=nota2*50
div=mul1+mul2+mul3//100
print("la nota del",nombre," es",div)