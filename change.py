def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto=float(input("Ingresar gasto:"))
    recibido=int(input("Dinero recibido"))
    vuelto=(recibido-gasto)
    pesos=int(vuelto)
    centavos=int((vuelto-pesos)*100)


    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
