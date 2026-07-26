import datetime  # para manejar fechas y horas
class Nota:  # define la clase de la nota 
    def __init__(
        self, id_nota, titulo, contenido
    ):  # constructor de la clase nota 
        self.id_nota = (
            id_nota  # asigna id de nota 
        )
        self.titulo = (
            titulo  # gurada titulo de nota
        )
        self.contenido = (
            contenido  # guarda contenido de nota
        )
        self.fecha = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )  # guarda fehca de creacion 

    def a_diccionario(
        self,
    ):  # covierte la nota en un diccionario 
        return {  
            "id": self.id_nota,
            "titulo": self.titulo,  
            "contenido": self.contenido, 
            "fecha": self.fecha,  
        }

    @staticmethod  
    def desde_diccionario(
        datos,
    ):  
        nota = Nota(
            datos["id"], datos["titulo"], datos["contenido"] 
        )  
        nota.fecha = datos[
            "fecha"
        ]  
        return nota  
#weyes si van a mover el codigo primero analizenlo y luego lo mueven xd
