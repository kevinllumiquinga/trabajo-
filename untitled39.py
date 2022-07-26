# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 23:07:50 2022

@author: USER
"""

import math
def seno(un):
    import math 
    x=math.radians(un) 
    x2=math.sin(x)
    return x2
def coseno(co):
    k=math.radians(co) 
    k2=math.cos(k)
    return k2
    
    
    
while True:
    inicio=int(input("Desea inicial ingrese 0 o 1, si desea terminar ingrese numeros mayores a 1: "))
    if inicio>1:
       break
    print("ESCOJA LA OPCCION QUE REQUIERE REALIZAR ")
    print("")
    print("1.descomposicion de fuerzas, dado el angulo y la fuerza.")
    print("2.descomposicion de fuerzas, dado el cateto opuesto, cateto adyasente y la fuerza.")
    print("3.descomposicion de fuerzas, dado el cateto opuesto y el cateto adyasente sin fuerza.")
    print("4.descomposicion de fuerzas, dado el angulo sin fuerza.")
    print("")
    f1=int(input("ingrese el literal que desea obtener: "))
    print()
    if f1==1:
        a=float(input("ingrese el angulo: "))
        a1=float(input("ingrese la fuerza: "))
        sin2=seno(a)*a1
        sen2=coseno(a)*a1
        print("")
        print("descomposicion en el eje x: ",sen2)
        print("descomposicion en el eje y: ",sin2)
    if f1==2:
        b=float(input("ingrese el cateto opuesto: "))
        b1=float(input("ingrese el cateto adyasente: "))
        b3=float(input("ingrese la fuerza: "))
        div=b1/b
        sin3=seno(div)*b3
        sen3=coseno(div)*b3
        print("")
        print("descomposicion en el eje x: ",sen3)
        print("descomposicion en el eje y: ",sin3)
    if f1==3:
        c=float(input("ingrese el cateto opuesto: "))
        c1=float(input("ingrese el cateto adyasente: "))
        div2=c1/c
        sin4=seno(div2)
        sen4=coseno(div2)
        print("")
        print("descomposicion en el eje x: ",sen4)
        print("descomposicion en el eje y: ",sin4)
    if f1==4:
        d=float(input("ingrese el angulo: "))
        sin5=seno(d)
        sen5=coseno(d)
        print("")
        print("descomposicion en el eje x: ",sen5)
        print("descomposicion en el eje y: ",sin5)
    else:
        print("fin del programa, datos fuera de rango.")
        
        
        
        