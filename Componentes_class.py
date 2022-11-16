


class Componentes:
    
    def __init__ (self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def __repr__(self) -> str:
        return self.marca + "   " + self.nombre + "\n" + self.obtenerEsp()

    def obtenerEsp (self) -> str:
        return ""

    def obtenerTipo(self) -> str:
        return "Componente"
