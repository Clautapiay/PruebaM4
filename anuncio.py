from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str, formato):
        self.__ancho = ancho 
        self.__alto = alto 
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        self.formatos_subtipos = {"Formato1": ["Subtipo1", "Subtipo2"], "Formato2": ["Subtipo3", "Subtipo4"]}
    
    def modificar_alto(self, nuevo_alto):
        self.alto = nuevo_alto if nuevo_alto > 0 else 1
    
    def modificar_ancho(self,nuevo_ancho):
        self.ancho = nuevo_ancho if nuevo_ancho > 0 else 1

    def modificar_sub_tipo(self, nuevo_subtipo):
        if nuevo_subtipo not in self.__sub_tipo:
            raise SubTipoInvalidoError(f'Subtipo {nuevo_subtipo} no válido para el tipo {self.tipo}')
        else:
            self._sub_tipo = nuevo_subtipo

@abstractmethod
def comprimir_anuncios(self):
    pass
@abstractmethod
def redimensionar_anuncio(self):
    pass

    #gettes y setter de atributos privados
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho < 0 else 1
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto <0 else 1

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @ancho.setter
    def sub_tipo(self, sub_tipo):
        self.__sub_tipo = sub_tipo

    #getter y setter de url_clic y url_archivo  segun description
    @property
    def url_archivo(self):
        return self.url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo:str):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic:str):
        self.__url_clic = url_clic

    
    #mostrar_formatos debe tener staticmethod
    @staticmethod
    def mostrar_formatos(self, mostrar_formatos):
        for formato, subtipos in Anuncio.formatos_subtipos.items():
            print(f"{formato}:")
            for subtipo in subtipos:
                print(f"- {subtipo}")



    def comprimir_anuncio(self, comprimir_anuncio):
        self.comprimir_anuncio = comprimir_anuncio

    def redimensionar_anuncio(self, redimensionar_anuncio):
        self.redimensionar_anuncio = redimensionar_anuncio


class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")
    def __init__(self, duracion:int, ancho =1, alto=1, formato="Video", sub_tipos=("instream","outstream")):
        super().__init__(1, 1, str, str, str)
        self.__duracion = duracion if duracion >0 else 5
    
    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self):
        pass

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self):
        pass

    #Mensaje en comprimir_anuncio
    def comprimir_anuncio(self,comprimir_anuncio):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self, redimensionar_anuncio):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def modificar_duracion(self,nueva_duracion):
        self.duracion = nueva_duracion if nueva_duracion > 0 else 5

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo)

    def comprimir_anuncio(self,comprimir_anuncio):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self, redimensionar_anuncio):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo)
    
    def comprimir_anuncio(self,comprimir_anuncio):
        self.comprimir_anuncio = comprimir_anuncio
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self, redimensionar_anuncio):
        self.redimensionar_anuncio = redimensionar_anuncio
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
        
