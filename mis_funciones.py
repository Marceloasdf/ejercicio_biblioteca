import json 
libros = []

def opcion1():
    print("Agregar libro")
    titulo=input("ingrese el titulo del libro: ")
    autor=input("ingrese el nombre del autor: ")
    fecha_publi=validar_fechapubli()
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
            print(f"Titulo:",l["titulo"])
            print(f"autor:",l["autor"])
            print(f"fecha de publicacion:",l["fecha.de.publicacion"])
            print(f"genero:",l["genero"]) 





def opcion3(libros):
    if len(libros)==0:
        print("no hay libros guardados, primero guarde libros en opcion 1")
    else:
        print("buscar libro por nombre")
        titulo_buscar=input("que libro quiere buscar?: ")
        for li in libros:
            if titulo_buscar.lower()==li["titulo"].lower():
                print(f"Titulo:",li["titulo"])
                print(f"autor:",li["autor"])
                print(f"fecha de publicacion:",li["fecha.de.publicacion"])
                print(f"genero:",li["genero"])
                return
        print("no encontramos el libro, lo sentimos")


def opcion4(libros):
    if len(libros)==0:
        print("no hay libros guardados, primero guarde libros en opcion 1")
    else:
        print("actualizar libro")
        libro_actualizar=input("que libro quiere actualizar?: ")
        for li in libros:
            if libro_actualizar.lower()==li["titulo"].lower():
                li["autor"]=input("ingrese nuevo autor: ")
                li["fecha.de.publicacion"]=int(input("ingrese nueva fecha de publicacion: "))
                li["genero"]=input("ingrese nuevo genero: ")
                print("Libro modificado con exito")
                return
        print("no encontramos el libro, lo sentimos")



def opcion5():
    if len(libros)==0:
        print("no hay libros guardados, primero guarde libros en opcion 1")
    else:
        print("guardar libros en archivo.json")
        nombre_archivo=validar_nombrearchivo()
        with open(nombre_archivo+".json","w") as archivo:
            json.dump(libros,archivo, indent=4) #para que no quede tan junto el texto, con enters 
            print("archivo creado exitosamente")
def opcion6():
    print("Adios!")
    exit()

################### funciones de validacion
def validar_opcion(lista_opciones):
    while True:
        try:
            opc=int(input("ingrese opcion: "))
            if opc in lista_opciones:
                return opc
        except:
            print("opcion incorrecta")
        else:
            print("solo se pueden numeros enteros")

def validar_nombrearchivo():
    while True:
        nombre_archivo=input("ingrese nombre de archivo: ")
        if len(nombre_archivo.strip())>=3:
            return nombre_archivo
        else:
            print("minimo 3 letras para el nombre del archivo")

def validar_fechapubli():
    while True:
        try:
            fecha_publi=int(input("ingrese el año de publicacion: "))
            if len(str(fecha_publi))==4:
                return fecha_publi
        except:
            print("Error, solo numeros enteros")
        else:
            print("Error, la fecha debe ser 4 digitos")
            