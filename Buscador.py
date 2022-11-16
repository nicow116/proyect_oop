
from Computador_class import *
from Lista_comp import *

class Buscador:

    def __init__(self) -> None:
        self.computador = []
        self.componentes = []

    def buscarComputador (self,cat,criterio):
        #Acceder a Base de Datos y buscar
        archivo = open ("archivos/computadores.csv", "r")
        self.computador = []

        for lineas in archivo:
            #Inicio de la información del computador
                coincide = False 
                datos = lineas.split(";")

                id = datos[0]
                nombre = datos[1]
                marca = datos[2]
                precio = datos[3]

                #Almacenar componentes
                componentes = []
                for comp in datos[4].split("%"):
                    datos_comp = comp.split(" ")

                    tipo = datos_comp[0]
                    nombre_comp = datos_comp[1]
                    marca_comp = datos_comp[2]
                    precio_comp = datos_comp[3]
                    car_comp = datos_comp[4]

                    match tipo:
                        # aqui los instancia como una clase en espesifico segun su tipo 
                        case "RAM":
                            componentes.append(RAM (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                        case "Procesador":
                            componentes.append(Procesador (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                        case "Disco":
                             componentes.append(Disco (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                        case "GPU":
                            componentes.append(GPU (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                    
                        case "PSU":
                            componentes.append(PSU (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                        

                    
                    #Buscar coincidencias
                    match (cat):
                        case "marca":
                            if (marca == criterio):
                                coincide = True
                        case "nombre":
                            if (nombre == criterio):
                                coincide = True
                        case "precio":
                            if (precio <= int(criterio)):
                                coincide = True
                        case "":
                            coincide = True

                    
                    #Agrega coincidencias a la lista
                    if (coincide):
                        self.computador.append(Computador(id = id, nombre = nombre, marca = marca, precio = precio, componentes = componentes))

        archivo.close()


def buscarComponente (self, cat, criterio):
        #Acceder a Base de Datos y buscar
        archivo = open ("archivos/componentes.csv", "r")
        self.computador = []

        for lineas in archivo:
            coincide = False
            col = lineas.split(";")
            

            #Leer marca, nombre y precio
            marca_comp = col[1]
            nombre_comp = col[2]
            precio_comp = int(col[3])
            car_comp = col[4]
            comp = col[0]

            match (cat):
                case "marca":
                    if (marca_comp == criterio):
                        coincide = True
                case "nombre":
                    if (nombre_comp == criterio):
                        coincide = True
                case "precio":
                    if (precio_comp <= int(criterio)):
                        coincide = True
                case "tipo":
                    if (comp == criterio):
                        coincide = True
                case "":
                    coincide = True


            #Leer el tipo de componente
            if (coincide):
                match comp:
                    # aqui los instancia como una clase en espesifico segun su tipo 
                    case "RAM":
                        
                        self.componentes.append(RAM (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                    case "Procesador":
                    
                        self.componentes.append(Procesador (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                    case "Disco":
                        self.componentes.append(Disco (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                    case "GPU":
                        self.componentes.append(GPU (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                
                    case "PSU":
                        self.componentes.append(PSU (nombre = nombre_comp, marca = marca_comp, precio = precio_comp, car = car_comp))
                   

    


