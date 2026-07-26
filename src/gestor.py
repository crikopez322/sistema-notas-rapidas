import json  # para manejar los archivos jSON🥀🥀🥀
import os  # para revisar si el archivo de datos existe en la compu
from nota import Nota  # jalamos la clase nota que acabamos de hacer


class GestorNotas:  # clase para manejar el guardado y lectura de notas

    def __init__(
        self, ruta_archivo="datos/notas.json"
    ):  # constructor con la ruta por defecto del jSON🥀🥀
        self.ruta_archivo = (
            ruta_archivo  # guarda la ruta donde se van a almacenar los datos
        )
        self.asegurar_archivo()  # se asegura de que la carpeta y el archivo existan desde el inicio

    def asegurar_archivo(
        self,
    ):  # funcion para evitar que truene si no existe la carpeta o el json
        directorio = os.path.dirname(
            self.ruta_archivo
        )  # obtiene la carpeta datos
        if (
            directorio and not os.path.exists(directorio)
        ):  # si no existe la carpeta
            os.makedirs(directorio)  # crea la carpeta datos

        if not os.path.exists(
            self.ruta_archivo
        ):  # si el archivo notas.json no existe
            with open(
                self.ruta_archivo, "w", encoding="utf-8"
            ) as f:  # lo crea desde cero
                json.dump([], f)  # le mete una lista vacia inicial

    def cargar_notas(self):  # lee las notas guardadas en el json
        try:
            with open(
                self.ruta_archivo, "r", encoding="utf-8"
            ) as f:  # abre el json en modo lectura
                datos = json.load(f)  # convierte el json a lista de python
                return [
                    Nota.desde_diccionario(d) for d in datos
                ]  # ni idea pero esto convierte cada diccionario en un objeto nota
        except Exception:  # por si ocurre un errir al leer 
            return []  # devuelve lista vacia para que no truene el programa

    def guardar_notas(
        self, lista_notas
    ):  # guarda listas notas en jSON 
        datos = [
            n.a_diccionario() for n in lista_notas
        ]  # covierte nota en diccionario
        with open(
            self.ruta_archivo, "w", encoding="utf-8"
        ) as f:  # abre el jSON en modo escritura
            json.dump(
                datos, f, indent=4, ensure_ascii=False
            )  # guarda datos ordenados 


# brocitos no vayan a mover la ruta del jSON o va a empezar a crear archivos por todos lados xd🥀🥀🥀