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
    return sigla.isalpha() and len(sigla) >= 2 and len(sigla) <= 5
    # en vez de if/else True/False, cada declaración después del return evalúa una condición y retorna True o False
    # por lo tanto no es necesario poner explícitamente cada evaluación si es que cada declaración después del return
    # es una condición: si todas las condiciones son verdaderas será return True, si no, el retorno será False.
    # el enunciado del ejercicio dice que hay que validar ingresar "solo letras mayusculas", pero lo que haré después es 
    # aceptar ingresos en minúsculas pero transformarlos a mayusculas. para hacer una validacion de eso sería entonces:
    # return sigla.isupper() and sigla.isalpha() and len(sigla_mayus) >= 2 and len(sigla_mayus) <= 5
    # porque sigla.upper() es una transformación y sigla.isupper() es una condición.

# funcion validar sigla existe:
def validar_sigla_existe(sigla, diccionario_consolas): # ingresar el ingreso del usuario en sigla_mayus y el
                                                             # diccionario donde buscará. usar sigla_mayus porque el
                                                             # diccionario ya la registró en mayúsculas y debe ser
                                                             # buscada así, no en minúsculas como en la variable sigla.
    if sigla in diccionario_consolas:
        return False
    else:
        return True

# funcion validar nombre:
def validar_nombre(nombre):
    if (nombre.strip() == "") or (len(nombre) < 3) or (len(nombre) > 40): # usa or no and porque si cualquiera
                                                                          # falla debe ser False, no todas juntas
        return False
    else:
        return True
    
# funcion validar fabricante:
def validar_fabricante(fabricante):
    if (fabricante.strip() == "") or (len(fabricante) < 2) or (len(fabricante) > 30):
        return False
    else:
        return True
    
# funcion validar año:
def validar_anio(anio):
    return anio >= 1972 and anio <= 2025

# funcion validar precio:
def validar_precio(precio):
    return precio > 0

# funcion validar stock:
def validar_stock(stock):
    return stock >= 0

# funcion opcion 1 agregar consola:
def agregar_consola(diccionario_consolas, diccionario_ventas):
    while True:
        sigla = input("Ingrese sigla de la consola: ").upper().strip() # transformo a mayúsculas y sigla siempre será mayus.
        if validar_sigla_formato(sigla) and validar_sigla_existe(sigla, diccionario_consolas):
            break
        else:
            print("Error, la sigla debe tener entre 2 y 5 caracteres y no existir previamente.")
    while True:
        nombre = input("Ingrese nombre de la consola: ")
        if validar_nombre(nombre):
            break
        else:
            print("Error, el nombre debe tener entre 3 y 40 caracteres y no estar vacío.")
    while True:
        fabricante = input("Ingrese fabricante de la consola: ")
        if validar_fabricante(fabricante):
            break
        else:
            print("Error, el fabricante debe tener entre 2 y 30 caracteres y no estar vacío.")
    while True:
        try:
            anio = int(input("Ingrese año de lanzamiento de la consola: ")) # uso try except int para transformar
                                                                            # a int aquí y no en la validacion porque
                                                                            # el enunciado pide msj de error aquí.
            if validar_anio(anio):
                break
            else:
                print("Error, el año debe estar entre 1972 y 2025.")
        except ValueError:
            print("Error, el año debe ser un número entero.")
    while True:
        try:
            precio = float(input("Ingrese precio de la consola: "))
            if validar_precio(precio):
                break
            else:
                print("Error, el precio debe ser mayor que cero.")
        except ValueError:
            print("Error, el precio debe ser un número decimal.")
    while True:
        try:
            stock = int(input("Ingrese stock de la consola: "))
            if validar_stock(stock):
                break
            else:
                print("Error, el stock debe ser igual o mayor que cero.")
        except ValueError:
            print("Error, el stock debe ser un número entero.")
    # agregar los datos al diccionario no se hace así aquí:
    # diccionario_consolas = {
    #    "sigla": sigla,
    #    ...
    # }
    # porque estaría creando un diccionario nuevo con una estructura distinta a la que exige el enunciado,
    # lo correcto es agregar una nueva entrada al diccionario existente:
    diccionario_consolas[sigla] = [nombre, fabricante, anio]
    diccionario_ventas[sigla] = [precio, stock]
    print("Consola agregada con éxito.")

# funcion solo buscar si está la consola en el diccionario según la sigla:
def buscar_consola(diccionario_consolas, sigla):
    return sigla in diccionario_consolas # retorna True si la sigla existe como clave en el diccionario.

# funcion detalle o print de la consola si la encuentra según su sigla (necesita ambos diccionarios porque
# mostrará datos de ambos diccionarios, además de la sigla de entrada):
def detalle_consola(diccionario_consolas, diccionario_ventas, sigla):
    # desempaquetar la lista almacenada en diccionario_consolas[sigla], asignando el primer elemento a nombre, 
    # el segundo a fabricante y el tercero a anio, la lista debe ser igual de larga que el número de variables:
    nombre, fabricante, anio = diccionario_consolas[sigla] # diccionario_consolas[sigla] corresponde a la lista que
                                                           # viene después de la clave según cual sea la sigla.
    precio, stock = diccionario_ventas[sigla]
    print("=== Consola Encontrada ===")
    print(f"Sigla: {sigla}.")
    print(f"Nombre: {nombre}.")
    print(f"Fabricante: {fabricante}.")
    print(f"Año: {anio}.")
    print(f"Precio: ${precio:.2f}.")
    print(f"Stock: {stock} unidades.")

# funcion opcion 2 buscar consola por sigla:
def opcion_buscar (diccionario_consolas, diccionario_ventas): # no necesita llamar a sigla porque las otras funciones
                                                              # lo harán después.
    sigla = input("Ingrese la sigla a buscar: ").upper().strip()
    if buscar_consola(diccionario_consolas, sigla):
        detalle_consola(diccionario_consolas, diccionario_ventas, sigla)
    else:
        print(f"Error, no se ha encontrado la consola {sigla}.")
    # no es necesario validar si el ingreso de sigla está vacío o es algo raro, porque si lo es, entonces igual
    # dará error porque no se ha encontrado la consola.

# funcion opcion 3 eliminar consola:
def eliminar_consola(diccionario_consolas, diccionario_ventas):
    sigla = input("Ingrese la sigla a eliminar: ").upper().strip()
    # validación de que está o no:
    if not buscar_consola(diccionario_consolas, sigla):
        print("Error, no se encuentra la consola.")
        return
    # si está, salto aca y muestro los detalles de la consola a eliminar:
    detalle_consola(diccionario_consolas, diccionario_ventas, sigla)
    # inicio proceso de confirmación:
    confirmar = input("Seguro desea eliminar la consola? (s/n)").strip().lower()
    if confirmar == "s":
        del diccionario_consolas[sigla]
        del diccionario_ventas[sigla]
        print("Consola eliminada correctamente.")
    else:
        print("Eliminación cancelada.")
    
# funcion opcion 4 mostrar todas las consolas:
def mostrar_todas(diccionario_consolas, diccionario_ventas):
    print("==============================")
    print("LISTADO COMPLETO DE CONSOLAS")
    print("==============================")
    # validar que hayan consolas registradas:
    if len(diccionario_consolas) == 0:
        print("Error, no hay consolas registradas.")
        return
    



# programa principal:
diccionario_consolas = {}
diccionario_ventas = {}
while True:
    mostrar_menu()
    opcion_elegida = ingresar_opcion()
    match opcion_elegida:
        case 1:
            agregar_consola(diccionario_consolas, diccionario_ventas)
        case 2:
            opcion_buscar (diccionario_consolas, diccionario_ventas)
        case 3:
            eliminar_consola(diccionario_consolas, diccionario_ventas)
        case 4:
            print("4")
        case 5:
            print("Saliendo...")
            break