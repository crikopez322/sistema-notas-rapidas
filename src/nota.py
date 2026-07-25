import datetime #esto es una libreria que nos permite trabajar con fechas y horas xd 

class Nota: 
    def __init__(self, id_nota, titulo, contenido):
        self.id_nota = id_nota
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_creacion = datetime.datetime.now().strftime("%Y-%m- %d %H:%M")