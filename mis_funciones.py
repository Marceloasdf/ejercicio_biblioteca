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





def opcion3(libros):
    print("buscar libro por nombre")
    titulo_libro=input("que libro quiere buscar?: ")
    for x in libros:
        if x.get("titulo")==titulo_libro:   
            print("libro encontrado")
            print(x)
        else:
            print("libro no encontrado, lo sentimos")
    

def opcion4(ibros):
    libro_actualizar=input("que libro quiere actualizar?: ")

def opcion5():
    pass
def opcion6():
    print("Adios!")
    exit()