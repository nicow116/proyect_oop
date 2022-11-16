from Buscador import *
buscador = Buscador()
print (" bienvenido quieres buscar un computador armado o componentes presiona 1 para computador o 2 para componentes ")
obcion  = input()

if ( obcion == "1"):
    parametro = input (" por cual parametro quieres buscar el computador  1 para marca 2 para nombre 3 para precio 0 para todos")
    if ( parametro == "1"):
        marca = input (" ingrese la marca del computador ")
        buscador.buscarComputador("marca", marca)


    if ( parametro == "2"):
        nombre = input (" ingrese el nombre del computador ")
        buscador.buscarComputador("nombre", nombre)

    if ( parametro == "3"):
        precio = input (" ingrese el precio del computador ")
        buscador.buscarComputador("precio", precio)

    if ( parametro == "0"):
        buscador.buscarComputador("", "1000")

    for comp in buscador.computador:
        print(comp)

if (obcion == "2"):
    obcion2 = input ( " selecciona el componente que quieres RAM , DISCO , GPU ,CPU ,PSU ")
    

    buscador.buscarComponente("tipo", obcion2)
    print ( " ingresa el parametro por el cual deseas filtrar el componente 1 para marcar 2 para nombre 3 para precio")
    parametro = input ()
     
    if ( parametro == "1"):
        marca = input (" ingrese la marca del componente  ")
        buscador.buscarComponente("marca", marca)


    if ( parametro == "2"):
        nombre = input (" ingrese el nombre del componente  ")
        buscador.buscarComponente("nombre", nombre)

    if ( parametro == "3"):
        precio = input (" ingrese el precio del componente  ")
        buscador.buscarComponente("precio", precio)


for comp in buscador.componentes:
        print(comp)

        """
        aqui nos encargamos de imprimir el computador o el componente dependiendo la cateogoria , su marca , su precio ,su nombre
        """

    

      
