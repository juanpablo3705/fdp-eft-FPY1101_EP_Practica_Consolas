# funcion mostrar menú:
def mostrar_menu():
    print("Menú Principal")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")

# funcion ingresar opción:
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion > 0 and opcion < 6:
                return opcion
            else:
                print("Error, debe escoger una opción del 1 al 5.")
        except ValueError:
            print("Error, debe ingresar sólo números del 1 al 5, no letras ni espacios en blanco.")

# funcion validar sigla formato:
def validar_sigla_formato(sigla):
    sigla_mayus = sigla.upper() # primero transformar sigla a mayusculas. esto no es una condición y no puede ser evaluada.
    return sigla_mayus.isalpha() and len(sigla_mayus) >= 2 and len(sigla_mayus) <= 5
    # en vez de if/else True/False, cada declaración después del return evalúa una condición y retorna True o False
    # por lo tanto no es necesario poner explícitamente cada evaluación si es que cada declaración después del return
    # es una condición: si todas las condiciones son verdaderas será return True, si no, el retorno será False.
    # el enunciado del ejercicio dice que hay que validar ingresar "solo letras mayusculas", pero acá lo que se hace es 
    # aceptar ingresos en minúsculas pero transformarlos a mayusculas. para hacer una validacion de eso sería entonces:
    # return sigla.isupper() and sigla.isalpha() and len(sigla_mayus) >= 2 and len(sigla_mayus) <= 5
    # porque sigla.upper() es una transformación y sigla.isupper() es una condición.

# funcion validar sigla existe:
def validar_sigla_existe(sigla_mayus, diccionario_consolas): # ingresar el ingreso del usuario en sigla_mayus y el
                                                             # diccionario donde buscará. usar sigla_mayus porque el
                                                             # diccionario ya la registró en mayúsculas y debe ser
                                                             # buscada así, no en minúsculas como en la variable sigla.
    if sigla_mayus in diccionario_consolas:
        return False
    else:
        return True


    

# programa principal:
diccionario_consolas = {}
diccionario_ventas = {}
while True:
    mostrar_menu()
    opcion_elegida = ingresar_opcion()
    match opcion_elegida:
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            print("3")
        case 4:
            print("4")
        case 5:
            print("Saliendo...")
            break