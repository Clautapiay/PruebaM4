#definir la clase que permita crear instancias de tipo Campaña.
from anuncio import Anuncio

class Campaña():
    def __init__(self,nombre: str, fecha_inicio, fecha_termino, anuncio):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.__anuncio = anuncio

    def __str__():
        pass
