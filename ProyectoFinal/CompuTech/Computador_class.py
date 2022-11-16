from Lista_comp import *

class Computador:
    def __init__ (self, id, nombre, marca, componentes, precio):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.componentes = componentes
        self.precio = precio

    def __repr__(self) -> str:
        return self.nombre + "\t" + self.marca + "\n" + self.obtenerEsp()

    def obtenerEsp (self):
        esp = "Componentes:     \n"

        for comp in self.componentes:
            esp = esp + "   " +  comp.obtenerTipo() + "\n   " + comp.nombre + "   " + comp.marca + " \n   " + comp.obtenerEsp() + "\n\n"

        return esp