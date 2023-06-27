from os import system, getcwd


def bienvenida():
    """
    Función que imprime un mensaje de bienvenida al usuario en caso de que ejecute este archivo por error
    """
    print("Bienvenido a mi proyecto, para ejecutar el mismo, ejecute main.py")


def periodo():
    """
    Función que permite al usuario seleccionar el periodo de tiempo a analizar
    """
    intentos = 0
    while True:
        try:
            eleccion = int(
                input(
                    """\nSeleccione el periodo de tiempo a analizar:
                                                        1. Máximo
                                                        2. 5 años
                                                        3. 1 año
                                                        4. 6 meses
                                                        5. 1 mes
                                                        6. 5 días
                                                        0. Salir

                                                        Seleccion: """
                )
            )
            if eleccion == 0:
                print("Saliendo...")
                exit()
            if eleccion in [1, 2, 3, 4, 5, 6]:
                break
            intentos += 1
            if intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")
        except (ValueError, TypeError):
            intentos += 1
            if intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")

    periodo = {1: "max", 2: "5y", 3: "1y", 4: "6mo", 5: "1mo", 6: "5d"}
    return periodo[eleccion]


def limpieza_de_archivos():
    """
    Función que se encarga de limpiar los archivos de datos y gráficos
    """
    dir_path = getcwd()
    try:
        system(f"rm -f {dir_path}/datos/*.csv ")
        system(f"rm -f {dir_path}/graficos/*.png ")
    finally:
        system(f"mkdir -p {dir_path}/datos")
        system(f"mkdir -p {dir_path}/graficos")


def lista_de_tickers(tickers, intentos=0):
    """
    Función que permite al usuario seleccionar los tickers a analizar

    Parameters
    ----------
    tickers : dict
        Diccionario que contiene los tickers a analizar

    Returns
    ----------
    tickers : dict
        Diccionario que contiene los tickers a analizar
    periodo_seleccionado : str
        String que contiene el periodo de tiempo a analizar
    """
    __intentos = 0

    print("Los tickers disponibles de manera predeterminada son")
    for ticker in tickers:
        print("*", ticker.rjust(len("\nLos tickers disponibles son:")))

    while True:
        try:
            eleccion = int(
                input(
                    """\nElija una opcion: 
                                1. Ingresar tickers manualmente
                                2. Ingresar tickers desde un archivo
                                3. Utilizar los tickers por defecto
                                0. Salir
                                
                                Seleccion: """
                )
            )
            if eleccion in [0, 1, 2, 3]:
                break
            __intentos += 1
            if __intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")
        except (ValueError, TypeError):
            __intentos += 1
            if __intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")
    if eleccion == 1:
        __intentos = 0
        while True:
            try:
                __tickers = input(
                    "\nPor favor, ingrese los tickers separados por coma: "
                ).split(",")
                __tickers = [ticker.upper().strip() for ticker in __tickers]
                if len(__tickers) > 0:
                    break
                __intentos += 1
                if __intentos >= 3:
                    print("Demasiados intentos fallidos, saliendo...")
                    exit()
                print("\n** Debe ingresar al menos un ticker **\n")
            except Exception:
                __intentos += 1
                if __intentos >= 3:
                    print("Demasiados intentos fallidos, saliendo...")
                    exit()
                print("\n** Ocurrió un error al procesar el input **\n")

        tickers = {}
        for ticker in __tickers:
            tickers[ticker] = []
        print("\n** La lista de tickers actual es:", __tickers, "**\n")
        periodo_seleccionado = periodo()
        print("\nComenzando análisis...")
        return tickers, periodo_seleccionado

    elif eleccion == 2:
        tickers = {}
        __intentos = 0
        while True:
            try:
                print(
                    'Debe ingresar la lista de tickers en un archivo de texto, separados por coma y sin espacios, para su conveniencia el archivo ya ha sido generado, con el nombre de "tickers.txt".'
                )
                system("touch tickers.txt")
                system("echo 'ko,meta' > tickers.txt")
                input('Una vez que haya ingresado los tickers, presione "Enter"')
                __tickers = open("tickers.txt", "r").read().split(",")
                __tickers = [ticker.upper().strip() for ticker in __tickers]
                print("Los tickers ingresados son: ", __tickers)
                for ticker in __tickers:
                    tickers[ticker] = []
                periodo_seleccionado = periodo()
                print("Comenzando analisis...")
                return tickers, periodo_seleccionado
            except (FileNotFoundError, IOError):
                __intentos += 1
                if __intentos >= 3:
                    print("Demasiados intentos fallidos, saliendo...")
                    exit()
                print("\n** Error al leer el archivo de tickers **\n")
            except Exception:
                __intentos += 1
                if __intentos >= 3 or periodo_seleccionado == 0:
                    print("Demasiados intentos fallidos, saliendo...")
                    exit()
                print("\n** Ocurrió un error al procesar los tickers **\n")

    elif eleccion == 3:
        print("La lista de tickers actual es: ", tickers.keys())
        periodo_seleccionado = periodo()
        print("\nComenzando analisis...")
        return tickers, periodo_seleccionado

    elif eleccion == 0:
        exit()


if __name__ == "__main__":
    bienvenida()
