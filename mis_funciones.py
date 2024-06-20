import json 
libros = []

def opcion1():
    print("Agregar libro")
    titulo=input("ingrese el titulo del libro: ")
    autor=input("ingrese el nombre del autor: ")
    año_publi=int(input("ingrese el año de publicacion: "))
    genero=input("ingrese el genero del libro: ")
    libro={"titulo":titulo, "autor":autor, "año.de.publicacion":año_publi,"genero":genero}
    libros.append(libro)
    print("libro agregado exitosamente")
