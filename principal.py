import time, os
from mis_funciones import *
while True:
    print("menu biblioteca")
    print("1) agregar un libro")
    print("2) mostrar libros almacenados")
    print("3) buscar libro por titulo")
    print("4) actualizar informacion de un libro")
    print("5) guardar libros en archivo .json ")
    print("6) Salir")
    
    opc=int(input("Ingrese opcion:"))
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
