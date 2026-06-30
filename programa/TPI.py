import csv #importamos la clase csv para utilizar las funciones de esta y que python las reconozca

# ==========================
# Funciones de manejo de datos
# ==========================

def guardar_datos_csv(archivo, paises): # en esta funcion le pasamos el parametro de la lista paises porque debe escribir lo que trae dentro de la misma al archivo .csv
    with open(archivo, "w", newline="", encoding="utf-8") as a: #abrimos el archivo (en este caso el .csv) con el parametro w de escribrir, newline para que elimine lineas vacias, con la codificacion utf-8 que acepta las ñ y letras que usamos en castellano, y el as a dice que guarde el archivo abierto con todos estos parametros en la variable a
        campos = ["nombre", "poblacion", "superficie", "continente"] # se crea la lista con los campos de las columnas cuando se crea el archivo, las columnas van a tener estos nombres
        escritor = csv.DictWriter(a, fieldnames=campos) #csv.dictwriter es una clase que permite escribir diccionarios en un archivo csv con los parametros: a donde trae el archivo csv con sus datos y de nombre de campos que use la lista que viene en la variable campos
        escritor.writeheader() # aca ejecuta el dictwriter la variable campos y la escribe en la primer linea para usarlas como nombre de columnas
        escritor.writerows(paises)# aca recorre la lista paises que contiene diccionarios y cada diccionario lo desgloza para escribir en cada linea todos los valores que trae cada uno



def cargar_datos_csv(archivo): #creamos la funcion para majenar el archivo .cvs
    """Lee el archivo CSV y devuelve una lista de diccionarios con los países."""
    paises = [] #creamos una lista para dentro poner cada diccionario que creamos con cada pais con sus respectivos claves y valores
    try:
        with open(archivo, newline='', encoding='utf-8') as archivo: # aca abrimos el archivo, newline controla los saltos de linea, encodig es el codigo que le dice a pytos que utilice el codigo de escritura adecuado para nuestro idioma
            lector = csv.DictReader(archivo) #aca utilizamos una clase de csv que es la dictreader lo que hace es tomar cada fila del archivo y crear un diccionario con cada fila donde utiliza la primera linea del archivo como claves, utiliza el archivo "archivo que tiene el archivo csv" y guarda cada diccionario hecho de cada fila en la variable lector 
            #la primer iteracion guarda los nombres de las claves que es la primer fila del archivo, le pide la primera linea del archivo que son los nombres de cada columna
            for fila in lector: #luego entra al for y recorre el archivo desde la segunda fila del archivo y va guardando en el diccionario cada valor con cada clave(cada clave es la primer fila del archivo) 
                paises.append({ #agrega en la lista paises cada diccionario
                    "nombre": fila["nombre"], #fila es el iterador, la posicion en cada fila y trae cada valor de cada clave y las guarda
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    except FileNotFoundError:
        print("Error: archivo CSV no encontrado.")
    except ValueError:
        print("Error: formato incorrecto en los datos.")
    return paises


def agregar_pais(paises):
    """Agrega un nuevo país validando que no haya campos vacíos."""
    print("\n--- Agregar País ---")
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()
        poblacion = input("Ingrese la población: ").strip()
        superficie = input("Ingrese la superficie en km2: ").strip()
        continente = input("Ingrese el continente: ").strip()

        # Validaciones de campos vacíos
        if not nombre or not poblacion or not superficie or not continente: #aca controlo que si el usuario no pone nada le genera un error y vuelve a pedir los valores
            print("Error: no se permiten campos vacíos. Intente nuevamente.\n")
            continue  # vuelve a pedir todo

        try: #puse el try aca porque si los valores estan correctos ya quiere decir que lo que siga desde aca tiene los valores correctos y no generaran errores
            poblacion = int(poblacion)
            superficie = int(superficie)
        except ValueError:
            print("Error: población y superficie deben ser números enteros. Intente nuevamente.\n")
            continue  # vuelve a pedir todo

        # Si todo salió bien, creamos el diccionario y salimos del bucle
        nuevo_pais = { # aca ingresamos cada clave valor de lo que ingreso el usuario en este diccionario
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(nuevo_pais) #agregamos el diccionario a la lista paises
        print(f"País '{nombre}' agregado correctamente.")
        break  # salimos del while True


def actualizar_pais(paises):
    """Actualiza población y superficie de un país existente."""
    print("\n--- Actualizar País ---")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    # Buscar país (coincidencia parcial)
    encontrado = None #creo esta variable que va a guardar lo que trae la variable nombre en caso que exista ese pais en la lista
    for pais in paises: #recorro la lista el nombre del iterador es pais
        if nombre.lower() in pais["nombre"].lower(): #aca escriba lo que escriba el usuario lo hago minuscula y luego me fijo si en la lista en esa posicion comparo si hay una clave con el valor que puso el usuario (nombre del pais), en caso que la encuentre, en la variable encontrado guardo lo que trae de la clave nombre en el diccionario
            encontrado = pais
            break

    if not encontrado: # a esta variable encontrado si recorrio toda la lista y no encontro el nombre en nigun diccionario muestra que no encontro nada y vuelve al menu
        print(f"Error: no se encontró ningún país con el nombre '{nombre}'.")
        return

    print(f"País encontrado: {encontrado['nombre']}") #si encontro lo muestra y comenzamos a pedir los valores de las otras claves dentro de ese diccionario

    # Reintentar hasta que los valores sean correctos
    while True:
        try:
            nueva_poblacion = int(input("Ingrese la nueva población: ").strip())
            nueva_superficie = int(input("Ingrese la nueva superficie en km2: ").strip())
            break
        except ValueError:
            print("Error: población y superficie deben ser números enteros. Intente nuevamente.\n")

    # Actualizar valores
    encontrado["poblacion"] = nueva_poblacion #aca en cada clave guardamos el nuevo valor que ingreso el usuario en estas variables
    encontrado["superficie"] = nueva_superficie

    print(f"Datos de '{encontrado['nombre']}' actualizados correctamente.")


def buscar_pais(paises):
    """Busca un país por nombre (parcial o exacto)."""
    print("\n--- Buscar País ---")
    while True:
        nombre = input("Ingrese el nombre del país a buscar: ").strip()

        if not nombre:
                print("Error: debe ingresar al menos una letra.\n")
                continue
        
        if nombre.isdigit():
            print("Error: el nombre del país no puede ser solo números.\n")
            continue

        break  # si pasó los controles, salimos del while

    resultados = [] #creamos una lista para guardar el resultado
    for pais in paises: #recorremos la lista 
        if nombre.lower() in pais["nombre"].lower(): #si lo que escribio el usuario esta en la posicion que se esta comparando en cada iteracion se agrega el valor de la clave nombre del diccionario de ese pais en la lista resultados
            #aca comparo tambien si el usuario no escribe completamente el nombre lo compara con lo que hay en cada diccionario, por ejemplo si escribimos arg, compara si arg in argentina y lo trae, y lo guarda en la lista resultados
            resultados.append(pais)

    if resultados: # aca compari si hay valor o valores en la lista, si hay mas de un valor segun como haya buscado puede haber un valor o varios
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for pais in resultados: #aca recorro la lista nueva que cree donde guardo los resultados y los muestro
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
    else:
        print(f"No se encontró ningún país con el nombre '{nombre}'.") #aca muestro este aviso si no se encotro nada


def filtrar_por_continente(paises):
    print("\n--- Filtrar por Continente ---")
    while True:
        try:
            continente = input("Ingrese el continente: ").strip()

            # Control: si no escribe nada
            if not continente:
                print("Error: debe ingresar al menos una letra.\n")
                continue

            # Control: si escribe solo números
            if continente.isdigit():
                print("Error: el continente no puede ser solo números.\n")
                continue

            break  # si pasó los controles, salimos del while

        except Exception as e:
            print("Error inesperado:", type(e).__name__, "-", e)
            continue

    resultados = [] #creamos esta lista para guardar los resultados que encuentre de cada diccionario (busca por clave continente y trae su valor)
    for pais in paises: #recorre la lista de los diccionarios
        if continente.lower() in pais["continente"].lower(): # aca pone en minuscula lo que escribio el usuario y tambien lo que hay en el valor de la clave continente, y compara si lo que escribio el usuario esta en esa clave
            resultados.append(pais)                          #como las palabras son cadenas tambien compara si lo que escribio el usuario esta en cada valor pero si pone solo la letra a en argentia esta la a, en alemania tambien, en japon tambien en cada cadena si encuentra concidencia lo trae y lo guarda en la lista resultados   

    if resultados: #aca mira si hay elementos en la lista 
        print(f"\nSe encontraron {len(resultados)} país(es) en {continente}:") #imprime la cantidad de resultados que encotnro
        for pais in resultados: #recorremos la lista y vamos imprimiendo cada posicion de la lista
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")
    else:
        print(f"No se encontraron países en el continente '{continente}'.") #si no encontro nada imrime este aviso
        #no agregamos try aca porque ya estan controlados los valores en las listas y solo trabajamos con texto

def filtrar_por_poblacion(paises):
    print("\n--- Filtrar por Población ---")

    # Reintentar hasta que el usuario ingrese un número válido
    while True: #usamos una bandera si el usuario ingresa un valor erroneo vuelve a pedir
        try: #usamos el try aca para corroborar que el valor de la variable es correcta
            umbral = int(input("Ingrese la población mínima: ").strip())
            break #si ingresa un entero sale del while
        except ValueError:
            print("Error: debe ingresar un número entero. Intente nuevamente.\n")#
            continue # si no ingresa un entero muestra el avisod e error y le vuelve a pedir

    resultados = [] #aca guardamos los resultados encontrados (creamos esta lista para guardar los diccionarios que tengan coincidencias)
    for pais in paises: #recorremos la lista de los diccionarios
        if pais["poblacion"] >= umbral: #si el valor de cada clave en cada posicion de la lista de diccionarios es menor o igual a lo que ingreso el usuario, guardamos ese diccionario en la lista resultados
            resultados.append(pais)

    if resultados: #si hay valores en la lista
        print(f"\nSe encontraron {len(resultados)} país(es) con población mayor o igual a {umbral}:") #mostramos la cantidad de coincidencias que se encotraron
        for pais in resultados: #recorremos la lista de coincidencias
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}") #mostramos cada diccionario 
    else:
        print(f"No se encontraron países con población mayor o igual a {umbral}.") #mostramos este aviso si no se encontro nada

def filtrar_por_superficie(paises):
    print("\n--- Filtrar por Superficie ---")

    # Reintentar hasta que el usuario ingrese un número válido
    while True:
        try:
            umbral = int(input("Ingrese la superficie mínima en km2: ").strip())
            break #si es un entero sale del while
        except ValueError:
            print("Error: debe ingresar un número entero. Intente nuevamente.\n")
            continue  # vuelve al inicio del while

    resultados = [] #creamos la lista donde vamos a guardar todas las coincidencias que vengan de la clave superficie
    for pais in paises: #recorremos la lista de los paises
        if pais["superficie"] >= umbral: #en cada iteracion comparamos que el valor que trae de la lista sea mayor o igual al humbral que puso el usuario, al revez de poblacion porque aca estamos comparando superficie, en este caso el humbral es la base y no el limite
            resultados.append(pais) #guardamos el diccionario que trae de paises y lo guarda en la lista resutlados

    if resultados: #si hay valores en resultados
        print(f"\nSe encontraron {len(resultados)} país(es) con superficie mayor o igual a {umbral} km2:") #imprimimos cuantos paises se encontraron con ese resultado, o que esten dentro de humbral
        for pais in resultados: #recorremos la lista de las coincidencias
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}") #imprimimos los paises (cada diccionario con sus claves y valores)
    else:
        print(f"No se encontraron países con superficie mayor o igual a {umbral} km2.") #mostramos esto si no hay coincidencias


def ordenar_paises(paises, criterio, descendente=False):
    """Ordena países por nombre, población o superficie."""
    print("\n--- Ordenar Países ---")

    # Pedir criterio de ordenamiento con reintentos
    while True:
        try:
            print("Opciones de criterio: nombre, poblacion, superficie")
            criterio = input("Ingrese el criterio de ordenamiento: ").strip().lower()

            if criterio in ["nombre", "poblacion", "superficie"]: #aca comparamos lo que puso el usuario que coincida con uno de estos criterios, aca no trabaja como las comparaciones de manera parcial como en otras funcioens, aca fuerzo que encuentre esa palabra que esta en la lista de comparacion
                break   # ✅ solo salimos si es correcto
            else:
                print("Error: criterio inválido. Debe ser 'nombre', 'poblacion' o 'superficie'. Intente nuevamente.\n")
                continue #si no encuentra le avisa y le vuelve a pedir la palabra o cadena
        except Exception as e:
            print("Error inesperado:", type(e).__name__)
            continue

    # Pedir sentido de ordenamiento con reintentos si ingresa mal un valor
    while True:
        try:
            sentido = input("Ingrese el sentido (ascendente/descendente): ").strip().lower()

            if sentido in ["ascendente", "descendente"]: #aca comparamos lo que puso el usuario que coincida con uno de estos criterios, aca no trabaja como las comparaciones de manera parcial como en otras funcioens, aca fuerzo que encuentre esa palabra que esta en la lista de comparacion
                
                if sentido == "descendente": # si ingreso correctamente la palabra "descendente" quiere decir que el ordenamiento es de mayor a menor
                    reverse = True #creamos un booleano en true para utilizarla luego
                else: 
                    reverse = False   # si escribio "ascendente" el ordenamiento va de menor a mayor y al booleano lo ponemos como false que vamos a utilizar luego                     
                break   # ✅ solo salimos si es correcto y salimos del while
            else:
                print("Error: el sentido debe ser 'ascendente' o 'descendente'. Intente nuevamente.\n")
                continue #aca si escribio mal la palabra se la volvemos a pedir, vuelve al input
        except Exception as e:
            print("Error inesperado:", type(e).__name__)
            continue #si encuentra un error vuelve al principio del while sin romperse

    # Ordenar la lista según el criterio elegido
    paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=reverse)   #aca creamos una lista (paises_ordenados) y guardamos en esta lista nueva la lista paises ordenada con la funcion sorted. La ordenamos segun los parametros que le pedimos al usuario
                                                                                    #key es un parametro de sorted, que le da el parametro para saber por que valor ordenar los paises (si en key se guarda "nombre" que ordene por nombre)
                                                                                    #lambda es una funcion anonima sin asignarle ningun nombre, se usa para no crear otra funcion de tipo def pero resumida  
                                                                                    #lambda x: x es el parametro que necesita para funcionar esta funcion (lambda), en este caso, sorted le pasa a esta funcion el diccionario (la posicion de la lista) para que la guarde en la variable x
                                                                                    #x[criterio]: esto esta dentro de la funcion (lambda) y se le asigna a x que es un diccionario (una posicion de la lista) con la clave que viene de la variable criterio
                                                                                    #reverse= es una variable interna de sorted() que funciona de esa manera, en reversa
                                                                                    #reverse=reverse lo que hago es decirle a esta funcionalidad de sorted() si reverse es true o false, la variable reverse luego del = es la que hice yo mas arriba cuando el usuario pide que sea ascendente o no
                                                                                    # y las , es porque sorted tiene mas de un parametro y se separa con una ,
    
    print(f"\nPaíses ordenados por {criterio} ({sentido}):") #imprimimos el tipo de clave que vamos a usar de parametro para ordenar y en que sentido                        
    for pais in paises_ordenados: #recorremos la lista nueva que creamos con sorted
        print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}") #imprimimos cada posicion de la lista


def mostrar_estadisticas(paises):
    """Muestra estadísticas básicas del dataset."""
    print("\n--- Estadísticas de Países ---")

    try: # controlamos todo esto con un try por si hay algun tipo de error de valor o algun error inesperado
        # País con mayor y menor población
        pais_mayor = max(paises, key=lambda x: x["poblacion"]) #guardamos en el diccionario pais_mayor el pais con mayor (funcion max) poblacion, sacamos de la lista paises, utilizando la funcion lambda con parametro x(donde x es un diccionario de la lista paises), dentro de esta funcion traemos la clave poblacion con su valor y a todo esto lo guardamos en la lista mencionada
        pais_menor = min(paises, key=lambda x: x["poblacion"]) #guardamos en el diccionario pais_menor el pais con menor (funcion min) poblacion, sacamos de la lista paises, utilizando la funcion lambda con parametro x(donde x es un diccionario de la lista paises), dentro de esta funcion traemos la clave poblacion con su valor y a todo esto lo guardamos en la lista mencionada 

        print(f"País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})") #mostramos el pais con mayor poblacion (lo que guardamos en el diccionario pais_mayor)
        print(f"País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})") #mostramos el pais con mayor poblacion (lo que guardamos en el diccionario pais_menor) 

        # Promedio de población
        promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises) #aca recorremos la lista paises donde p es un diccionario, la funcion sum, suma la clave valor de cada posicion de la lista, en este caso suma el valor poblacion y lo divide por la cantidad de paises (len(paises))
        print(f"Promedio de población: {promedio_poblacion:.2f}") #aca mostramos lo que se guardo en la variable promedio_poblacion(el calculo que explicamos la linea de arriba)

        # Promedio de superficie
        promedio_superficie = sum(p["superficie"] for p in paises) / len(paises) #aca recorremos la lista paises donde p es un diccionario, la funcion sum, suma la clave valor de cada posicion de la lista, en este caso suma el valor superficie y lo divide por la cantidad de paises (len(paises))
        print(f"Promedio de superficie: {promedio_superficie:.2f} km²") #aca mostramos lo que se guardo en la variable promedio_superficie(el calculo que explicamos la linea de arriba)

        # Cantidad de países por continente
        continentes = {} #creamos un diccionario para guardar la cantidad de paises con la clave continente (la cantidad de paises por continente)
        for p in paises: #recorremos la lista
            cont = p["continente"] #en cada iteracion guardamos en cont el valor que trae de la clave continente (por ej: America, Asia) no guarda la clave, valor completa
            if cont in continentes: # aca comparamos si lo que trae la variable cont (un diccionario de clave valor continente)
                continentes[cont] += 1   # si existe, suma 1 al valor de la clave que traemos en cont (que cont es el valor de la clave de cada diccionario de la lista paises) aca a este valor (por ej: America) lo usamos de clave y el valor es una suma en 1 en caso que encuentre en el diccionario la clave America o Europa
            else:                        # el diccionario se veria asi: continentes = {Asia: 3, Europa: 4, America: 7}   
                continentes[cont] = 1    # si no existe, la creamos con valor inicial 1, aca usamos en este diccionario como clave, el valor que traemos del diccionario de la lista paises, aca el diccionario no es clave contienten, valor America, aca es clave America valor 1

        print("\nCantidad de países por continente:")
        for cont, cantidad in continentes.items(): # aca recorremos con cont, cantidad (esto seria la clave, valor del diccionario) en los items del diccionario, significa por cada clave valor en los items del diccionario continentes
            print(f"- {cont}: {cantidad}") #imprimimos la clave valor en cada iteracion

    except Exception as e:
        print("Error al calcular estadísticas:", type(e).__name__, "-", e)


def mostrar_paises(paises): #esta funcion no va pero la hice por si el usuario queire ver todo el archivo .csv
    print("\n--- Lista de Países ---")
    if not paises:
        print("No hay países cargados en el sistema.")
        return

    for pais in paises:
        print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2 | Continente: {pais['continente']}")


# ==========================
# Menú principal
# ==========================

def mostrar_menu():
    print("\n--- Gestión de Países ---")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar países")
    print("8. Salir")


def main(): #creamos la funcion main donde trabajan las otras funciones, desde aca llamamos a cada una segun el caso
    #paises = [] #creamos la lista paises dentro de esta funcion principal ya que las funciones utilizan esta lista para trabajar, y no la dejamos por fuera como una variable global
    archivo_csv = r"C:\Users\Nico\OneDrive\Desktop\tec prog\1er cuatri\prog 1\TPI\paises.csv"
    paises = cargar_datos_csv(archivo_csv)

    while True: # encapsulamos todo dentro de un while para que el usuario no salga de el menu de opciones nunca y salga unicamente si utiliza la opcion 8
        mostrar_menu() # aca ejecutamos las opciones del menu (esta funcion imprime el menu)
        try:
            opcion = int(input("Seleccione una opción (1-8): ").strip())
        except ValueError:
            print("Error: debe ingresar un número entre 1 y 8.\n")
            continue  # vuelve al inicio del while

        match opcion:
            case 1:
                agregar_pais(paises)
                guardar_datos_csv(archivo_csv, paises)   # persistir cambios
            case 2:
                if len(paises) == 0:
                    print("Error: no hay países cargados. Primero debe agregar países antes de ordenar.\n")
                    continue  # vuelve al menú principal
                actualizar_pais(paises)
                guardar_datos_csv(archivo_csv, paises)   # persistir cambios
            case 3:
                if len(paises) == 0:
                    print("Error: no hay países cargados. Primero debe agregar países antes de ordenar.\n")
                    continue  # vuelve al menú principal
                buscar_pais(paises)
            case 4:
                if len(paises) == 0:
                    print("Error: no hay países cargados. Primero debe agregar países antes de ordenar.\n")
                    continue  # vuelve al menú principal
                print("\n--- Submenú de Filtros ---")
                print("1. Filtrar por continente")
                print("2. Filtrar por población")
                print("3. Filtrar por superficie")
                try:
                    subopcion = int(input("Seleccione una opción: ").strip())
                except ValueError:
                    print("Error: debe ingresar un número válido.\n")
                    continue

                match subopcion:
                    case 1:
                        filtrar_por_continente(paises)
                    case 2:
                        filtrar_por_poblacion(paises)
                    case 3:
                        filtrar_por_superficie(paises)
                    case _:
                        print("Opción inválida en filtros.\n")

            case 5:
                if len(paises) == 0:
                    print("Error: no hay países cargados. Primero debe agregar países antes de ordenar.\n")
                    continue  # vuelve al menú principal
                print("\n--- Submenú de Ordenamientos ---")
                print("1. Ordenar por nombre")
                print("2. Ordenar por población")
                print("3. Ordenar por superficie")
                try:
                    subopcion = int(input("Seleccione una opción: ").strip())
                except ValueError:
                    print("Error: debe ingresar un número válido.\n")
                    continue

                match subopcion:
                    case 1:
                        ordenar_paises(paises, "nombre")
                    case 2:
                        ordenar_paises(paises, "poblacion")
                    case 3:
                        ordenar_paises(paises, "superficie")
                    case _:
                        print("Opción inválida en ordenamientos.\n")

            case 6:
                mostrar_estadisticas(paises)
            case 7:
                mostrar_paises(paises)
                cargar_datos_csv(archivo_csv)
            case 8:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida, intente nuevamente.\n")


if __name__ == "__main__": #esto funciona como otro control por si se exporta este archivo en otro, en este mismo archivo como esta variable global se le asigna el valor main, se ejecuta el programa, si este archivo contenedor de este programa 
    main()                 #python le asigna el valor __main__ a la variable __name__ cuando el archivo es el que se esta ejecutando, si se importa ya no trabaja como un archivo main y el valor de __name__ cambia al nombre del archivo 
