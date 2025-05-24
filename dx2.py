print("multiplicacion o division")
num1=int(input("inserta un numero"))
num2=int(input("inserta la potencia"))
dom=input("escoge d para division y m para multiplicacion")
num3=int(input("inserta otro numero"))
num4=int(input("inserta la potencia"))
d=num1**num2/num3**num4
m=num1**num2*num3**num4
if dom == "d":
     print("el resultado es",d)
else:
    print("el resultado es",m)
print(input("si sirvio o no sirvio"))
print("toma un premio")

import webbrowser

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("https://www.tailsarchive.com/p/blog-page_11.html?m=0")
