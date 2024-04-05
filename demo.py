from campaña import Campaña
from anuncio import Anuncio

campaña = Campaña


try:
    pedir_nnuevo_nombre = input("Ingrese un nuevo nombre de Campaña:")
    pedir_nuevo_subtipo = input("Ingrese un nuevo nombre de sub_tipo:")

except Exception as e:
    with open("error.log", "a") as log:
        log.write(str(e) + "\n")

