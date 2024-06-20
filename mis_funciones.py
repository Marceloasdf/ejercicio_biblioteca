import json 
libros = []

def opcion1():
    print("Agregar libro")
    titulo=input("ingrese el titulo del libro: ")
    autor=input("ingrese el nombre del autor: ")
    fecha_publi=int(input("ingrese el año de publicacion: "))
    genero=input("ingrese el genero del libro: ")
    libro={"titulo":titulo, "autor":autor, "fecha.de.publicacion":fecha_publi,"genero":genero}
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
            print(f"fecha de publicacion:{l['fecha.de.publicacion']}")
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
    

def opcion4(libros):
    print("actualizar libro")
    libro_actualizar=input("que libro quiere actualizar?: ")
    for x in libros:
        if x.get("titulo")==libro_actualizar:
            print("libro encontrado")
            pass
        else:
            print("libro no encontrado, lo sentimos")

def opcion5():
    print("guardar libros en archivo.json")
    nombre_archivo=input("ingrese nombre de archivo: ")
    with open(nombre_archivo+".json","w",newline="") as archivo:
        json.dump(libros,archivo)
def opcion6():
    print("Adios!")
    exit()