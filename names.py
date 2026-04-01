def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    nombre=input("Ingrese su nombre")
    apellido=input("Ingrese su apellido")
    nya=nombre+" "+apellido
    print(nya.lower())
    print(nya.title())
    print(nya.upper())
    #print("\t",nya.lower())
    print(f"\t{nya.lower()}")
