# ppal
consolas = {} # {sigla:[nombre,fabricante,añoLanzamiento]}
ventas = {} # {sigla: [precio,stock]}

def menu():
    print("="*40)
    print("SISTEMA DE CONSOLAS DE VIDEOJUEGOS")
    print("1. Agregar Consola")
    print("2. Buscar Consola por sigla")
    print("3. Eliminar Consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("="*40)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            return opcion
        except ValueError:
            print("Debe ingresar un número!! ")

#  funciones de validaciones que retornan True o False

def validar_sigla_formato(sigla):
    return sigla.upper() and sigla.isalpha() and len(sigla) >= 2 and len(sigla) <= 5
    # return True

    # len(sigla) >= 2 and len(sigla) <= 5    o    2 <= len(sigla) <= 5

def validar_sigla_no_existe(sigla,consolas):
    if sigla not in consolas:
        return True
    else:
        return False

    # return sigla not in consolas

def validar_nombre(nombre):

    return 3 <= len(nombre.strip()) <= 40

def validar_año(añoStr):
    if not añoStr.isdigit():
        return False
    
    return 1972 <= int(añoStr) <= 2025

def validar_precio(precioStr):
    try:
        return float(precioStr) > 0
    except ValueError:
        return False

def validar_stock(stockStr):
    if not stockStr.isdigit():
        return False
    
    return int(stockStr) >= 0

def validar_fabricante(fabricante):
    return 2 <= len(fabricante.strip()) <= 30

def agregar_consola(consolas,ventas):

    sigla = input("Ingrese sigla (2 a 5 letras mayúsculas)").strip()

    while not validar_sigla_formato(sigla):
        print("Error de sigla, debe tener 2 a 5 letras mayúsculas, vuelva a intentar")
        sigla = input("Sigla: ") .strip()

    if not validar_sigla_no_existe(sigla,consolas):
        print("La sigla ya existe, no se puede agregar")
        return

    nombre = input("Ingrese el nombre: (3 y 40 caracteres) : ").strip()

    while not validar_nombre(nombre):
        print("Error, nombre no válido, intente nuevamente")
        nombre = input("Ingrese el nombre: (3 y 40 caracteres) : ").strip()

    fabricante = input("Fabricante(2 a 30 caracteres): ").strip()

    while not validar_fabricante(fabricante) :
        print("Error, fabricante no válido, intente nuevamente")
        fabricante = input("Fabricante(2 a 30 caracteres): ").strip()

    añoStr = input("Año de lanzamiento(1972-2025): ").strip()

    while not validar_año(añoStr):
        print("Error, año no válido!, intente nuevamente")
        añoStr = input("Año de lanzamiento(1972-2025): ").strip()

    precioStr = input("Ingrese precio: ").strip()

    while not validar_precio(precioStr):
        print("Error, debe ser mayor a cero, intente nuevamente")
        precioStr = input("Ingrese precio: ").strip()

    stockStr = input("Ingrese Stock: ").strip()
    
    while not validar_stock(stockStr):
        print("Error, deber ser mayor a cero, intente nuevamente")
        stockStr = input("Ingrese Stock: ").strip()
    
    consolas[sigla] = [nombre,fabricante,int(añoStr)]
    ventas[sigla] = [float(precioStr),int(stockStr)]

    print("Consola agregada correctamente")

def buscar_consola(consolas,sigla):
    return sigla in consolas

def opcion_buscar(consolas,ventas):
    sigla = input("Ingrese sigla a buscar: ").strip().upper()
    if buscar_consola(consolas,sigla):
        detalle_consola(sigla,consolas,ventas)
    else:
        print("No se encontro consola ",sigla)


def mostrar_todas(consolas,ventas):
    print("="*60)
    print("Listado de consolas")
    print("="*60)

    if len(consolas) == 0 :
        print("No hay datos de consolas")
    else:
        for sigla,datos in consolas.items():
            nombre,fabricante,año = datos
            precio,stock = ventas[sigla]
            print(f"{sigla} | {nombre} | {fabricante} | {año} | ${precio} | {stock}")
    print("=" * 62)
    print(f"Total de consolas: {len(consolas)}")


def detalle_consola(sigla,consolas,ventas):
    nombre,fabricante,año = consolas[sigla]
    precio,stock = ventas[sigla]

    print("Consola Encontrada")
    print("Sigla: ",sigla)
    print("Nombre: ",nombre)
    print("Fabricante: ",fabricante)
    print("Año: ",año)
    print("Precio :$",precio )
    print("Stock: ",stock)

def eliminar_consola(consolas,ventas):
    print("Eliminar consola")
    sigla = input("Ingrese sigla a eliminar").strip().upper()

    if not buscar_consola(consolas,sigla):
        print("No se encuentra la sigla")
        return
    detalle_consola(sigla,consolas,ventas)
    confirmar = input("Seguro desea eliminar? (s/n)").strip().lower()
    if confirmar == "s":
        del consolas[sigla]
        del ventas[sigla]
        print("Eliminado exitosamente")
    else:
        print("Eliminación cancelada!")

#ppal
while True:
    menu()
    op = leer_opcion()
    if op == 1 :
        agregar_consola(consolas,ventas)
    elif op == 2:
        opcion_buscar(consolas,ventas)
    elif op == 3:
        eliminar_consola(consolas,ventas)
    elif op == 4:
        mostrar_todas(consolas,ventas)
    elif op == 5:
        print("Saliendo..")
        break
    else:
        print("las opciones son del 1 al 5, vuelva a ingresar")
    
    
