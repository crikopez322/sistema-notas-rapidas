#validaciones de entrada de datos xd
def validar_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto: #si rl texto tiene algo 
            return texto #devuelve el texto
        print("no puedes dejar este campo vacio bro")#por si el usuario deja bacio el camopo

        def validar_numero_entero(mensaje): #valida la entrada de un entero
            while True:
                entrada = input(mensaje).strip() #pde el doto
                if entrada.isdigit(): #checa si es numero 
                    return int(entrada) #devuelve el numero entero lo regresa
                print("introduce un numero valido bro, nada de letras o cosas raras") #por si al usuario le falla xdddd
                #alejandro continua qui brocito xd 

    def validar_opcion_menu(opcion, minimo, maximo):#para ver si opcion esta dentro del ranfo
        if opcion.isdigit():#primero ve si es numero 
            numero = int(opcion) #si es numero lo convierte a entero
            if minimo <= numero <= maximo: #checa si esta dentro del rango  
                return True #si esta dentro del rango regresa true
        return False #si no esta dentro del rango regresa false 
  
   # bociyos usen estas validaciones en el main para que la app no se les caiga xd

    
