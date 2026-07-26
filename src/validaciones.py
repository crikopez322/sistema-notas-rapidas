# Validaciones de entrada de datos xd

def validar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:  # Si el texto tiene algo
            return texto  # Devuelve el texto
        print(" No puedes dejar este campo vacío, bro.")


def validar_numero_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(" Error: Debes ingresar un número entero válido.")


def validar_opcion_menu(opcion, minimo, maximo):  # Para ver si opción está dentro del rango
    if opcion.isdigit():  # Primero ve si es número
        numero = int(opcion)  # Si es número lo convierte a entero
        if minimo <= numero <= maximo:  # Checa si está dentro del rango
            return True  # Si está dentro del rango regresa True
    return False  # Si no está dentro del rango regresa False
#me kgo en la validacion xd 
