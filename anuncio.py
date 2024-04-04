# definir la clase Anuncio y las clases que permitan
#crear instancias de tipo Video, Display y Social, cada una de ellas con sus
#atributos de clase y valores correspondientes respectivos.

class Anuncio():
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str):
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    def mostrar_formatos(self, mostrar_formatos):
        self.mostrar_formatos = mostrar_formatos

    def comprimir_anuncio(self, comprimir_anuncio):
        self.comprimir_anuncio = comprimir_anuncio

    def redimensionar_anuncio(self, redimensionar_anuncio):
        self.redimensionar_anuncio = redimensionar_anuncio


class Video(Anuncio):
    def __init__(self, ancho =1, alto=1, duracion:int, formato="Video", sub_tipos=("instream","outstream")):
        self.formato = formato
        self.sub_tipos = sub_tipos
        self.__ancho = ancho
        self.__alto = alto
        self.__duracion = duracion

    def comprimir_anuncio(self,comprimir_anuncio):
        self.comprimir_anuncio = comprimir_anuncio

    def redimensionar_anuncio(self, redimensionar_anuncio):
        self.redimensionar_anuncio = redimensionar_anuncio

class Display(Anuncio):
    def __init__(self, formato="Display",sub_tipos=("tradicional", "native")):
        self.formato = formato
        self.sub_tipos = sub_tipos

    def comprimir_anuncio(self,comprimir_anuncio):
        self.comprimir_anuncio = comprimir_anuncio

    def redimensionar_anuncio(self, redimensionar_anuncio):
        self.redimensionar_anuncio = redimensionar_anuncio

    class Social(Annuncio):
        def __init__(self, formato="Social", sub_tipos= ("facebook", "linkedin")):
            self.fotmato = formato
            self.sub_tipos = sub_tipos
    
        def comprimir_anuncio(self,comprimir_anuncio):
            self.comprimir_anuncio = comprimir_anuncio

        def redimensionar_anuncio(self, redimensionar_anuncio):
            self.redimensionar_anuncio = redimensionar_anuncio
        
