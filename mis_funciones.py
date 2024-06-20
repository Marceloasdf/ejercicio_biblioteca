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


def opcion2():
    print("mostrar libros guardados")
    if len(libros)==0:
        print("no hay libros guardados, primero guarde libros en opcion 1")
    else:
        for l in libros:
            print(f"Titulo:{l['titulo']}")
            print(f"autor:{l['autor']}")
            print(f"año de publicacion:{l['año.de.publicacion']}")
            print(f"genero:{l['genero']}\n") 





def opcion3():
    pass
def opcion4():
    pass
def opcion5():
    pass
def opcion6():
    print("Adios!")
    exit()