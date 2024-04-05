
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError

class Campaña():
    def __init__(self,nombre: str, fecha_inicio, fecha_termino, anuncios:list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncio = anuncios

    def __str__(self):
        cant_video = 0
        cant_display = 0
        cant_social = 0
        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cant_video +=1
            if isinstance(elemento, Display):
                cant_display +=1
            elif isinstance(elemento, Social):
                cant_social +=1
        
        return f""" 
        Nombre de la Campaña: {self.__nombre}
        Anuncios: {cant_video} Video, {cant_display} display, {cant_social} Social"""

    def modificar_nombre_campaña(self, nuevo_nombre):
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoError(f"'Largo de {nuevo_nombre} supera los 250 caracteres")
        else:
            self.__nombre = nuevo_nombre


    #getter y setter de los demas atributos privados
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    #setter y getter de fecha_inicio y fecha_termino segun descripcion
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    @property
    def url_archivo(self):
        return self.correo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo:str):
        self.__url_archivo = url_archivo

    #Solo getter de anuncio segun descripcion
    @property
    def anuncio(self):
        return self.__anuncio
    