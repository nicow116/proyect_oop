from Componentes_class import Componentes

class RAM (Componentes):
    
    def _init_(self, nombre, marca, precio, car) -> None:
        super()._init_(nombre, marca, precio)
        self.car = car

    def obtenerEsp (self) -> str:
        return "Memoria: " + self.car

    def obtenerTipo(self) -> str:
        return "RAM"


class Procesador (Componentes):
    
    def _init_(self, nombre, marca, precio, car) -> None:
        super()._init_(nombre, marca, precio)
        self.car = car

    def obtenerEsp (self) -> str:
        return "Potencia: " + self.car

    def obtenerTipo(self) -> str:
        return "Procesador"

class GPU (Componentes):
    
    def _init_(self, nombre, marca, precio, car) -> None:
        super()._init_(nombre, marca, precio)
        self.car = car

    def obtenerEsp (self) -> str:
        return "Graficos: " + self.car

    def obtenerTipo(self) -> str:
        return "GPU"
    
class Disco (Componentes):
    
    def __init__(self, nombre, marca, precio, car) -> None:
        super().__init__(nombre, marca, precio)
        self.car = car

    def obtenerEsp (self) -> str:
        return "Capacidad: " + self.car

    def obtenerTipo(self) -> str:
        return "Disco"



class PSU (Componentes):
    
    def __init__(self, nombre, marca, precio, car) -> None:
        super().__init__(nombre, marca, precio)
        self.car = car

    def obtenerEsp (self) -> str:
        return "Voltaje: " + self.car

    def obtenerTipo(self) -> str:
        return "PSU"


