#punto de entrada principal del programa weyxd
print("sistemas de notas rapidas")

# Este archivo se encarga de ejecutar para usar el programa.

# Traemos las herramientas que ya construimos en otros archivos
from gestor import GestorNotas          # esta clase se encarga de guardar y leer las notas del archivo json
from nota import Nota                   # esta clase representa una nota individual (con su id, título, etc.)
from validaciones import (              # traemos funciones que revisan que lo que escribe el usuario esté bien
    validar_numero_entero,              # revisa que lo que se escribió sea un número entero válido
    validar_opcion_menu,                # revisa que la opción elegida esté dentro del rango permitido
    validar_texto_no_vacio,             # revisa que el usuario no haya dejado un texto vacío
)


def mostrar_menu():
    # esta función solo imprime en pantalla las opciones del menú
    print("\n" + "=" * 35)                        # línea decorativa de arriba
    print(" 📝 SISTEMA DE NOTAS RÁPIDAS XD")     # título del programa
    print("=" * 35)                                # otra línea decorativa
    print("1. Crear nueva nota")                   # opción 1
    print("2. Ver todas las notas")                # opción 2
    print("3. Eliminar una nota")                  # opción 3
    print("4. Salir")                              # opción 4
    print("=" * 35)                                # línea decorativa final


def main():
    # esta es la función principal, aquí corre todo el programa

    gestor = GestorNotas()   # creamos el encargado que va a leer y guardar las notas en el archivo json

    while True:  # este ciclo se repite una y otra vez hasta que el usuario decida salir
        mostrar_menu()                                       # muestra las opciones en pantalla
        opcion = input("Selecciona una opción (1-4): ").strip()  # guarda lo que escribió el usuario, sin espacios de sobra

        # antes de hacer algo, revisamos que la opción escrita sea válida (entre 1 y 4)
        if not validar_opcion_menu(opcion, 1, 4):
            print("opcion no valida pa, elige del 1 al 4 xd")  # avisa que se equivocó
            continue   # regresamos al inicio del ciclo y no hace nada más

        
        # Crea una nota nueva
    
        if opcion == "1":
            print("\n--- Nueva Nota ---")                          # avisamos que vamos a crear una nota
            titulo = validar_texto_no_vacio("Título de la nota: ")     # pedimos el título y revisamos que no esté vacío
            contenido = validar_texto_no_vacio("Contenido de la nota: ")  # pedimos el contenido y revisamos que no esté vacío

            notas = gestor.cargar_notas()   # trae todas las notas que ya existen guardadas

            # aquí sacamos el id más alto que exista y le sumamos 1, para que cada nota tenga un número distinto
            nuevo_id = max([n.id_nota for n in notas], default=0) + 1

            nueva_nota = Nota(nuevo_id, titulo, contenido)   # creamos la nota nueva con esos datos
            notas.append(nueva_nota)                         # la agregamos a la lista de notas
            gestor.guardar_notas(notas)                      # guarda la lista actualizada en el archivo json

            print(f" ¡Nota '{titulo}' guardada con éxito!")   # ve que todo salió bien

        # Mira todas las notas guardadas
        elif opcion == "2":
            print("\n--- Tus Notas Guardadas ---")   # avisa que vamos a enseñar las notas
            notas = gestor.cargar_notas()             # traemos todas las notas guardadas

            if not notas:
                print("No hay notas guardadas todavía compa.")   # si la lista está vacía se avisa
            else:
                for n in notas:   #se ve una por una todas las notas guardadas
                    print(
                        f"\n [ID: {n.id_nota}] {n.titulo} (Creada: {n.fecha})"
                    )   # mostramos el id, el título y la fecha en que se creó
                    print(f"   {n.contenido}")   # se muetra que hay en esa nota

        # Elimnar una nota
       
        elif opcion == "3":
            print("\n--- Eliminar Nota ---")     # avisa que vamos a eliminar una nota
            notas = gestor.cargar_notas()        # traemos las notas guardadas

            if not notas:
                print("No hay notas para eliminar.")   # si no hay notas, no hay nada que borrar
            else:
                id_eliminar = validar_numero_entero(
                    "Ingresa el ID de la nota a eliminar: "
                )   # pedimos el id de la nota que se quiere borrar y revisamos que sea un número válido

                # armamos una nueva lista dejando solo las notas que NO tienen ese id
                notas_nuevas = [n for n in notas if n.id_nota != id_eliminar]

                if len(notas_nuevas) < len(notas):
                    # si la nueva lista tiene menos notas que la original, quiere decir que se va a borrar algo
                    gestor.guardar_notas(notas_nuevas)   #se guarda la lista ya sin esa nota
                    print(f"🗑️ Nota con ID {id_eliminar} eliminada.")
                else:
                    # si el tamaño no cambió, es porque ese id no existe
                    print(" No se encontró ninguna nota con ese ID.")

    
        # OPCIÓN 4: Salida del programa
        elif opcion == "4":
            print("\n¡Hasta la vista Bayby!")   # mensaje de despedida
            break   # rompemos el ciclo "while True" y programa termina


# Esto mira que el archivo se esté ejecutando directamente y no usando otro archivo
# si se cumple la condición, arranca el programa llamando a la función principal
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Programa interrumpido por el usuario. ¡Hasta luego!")