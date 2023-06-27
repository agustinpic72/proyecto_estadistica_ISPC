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
    __intentos = 0
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
        except ValueError:
            if __intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")
            __intentos += 1
            periodo(__intentos)

    if eleccion == 1:
        periodo = "max"
        return periodo
    elif eleccion == 2:
        periodo = "5y"
        return periodo
    elif eleccion == 3:
        periodo = "1y"
        return periodo
    elif eleccion == 4:
        periodo = "6mo"
        return periodo
    elif eleccion == 5:
        periodo = "1mo"
        return periodo
    elif eleccion == 6:
        periodo = "5d"
        return periodo
    elif eleccion == 0:
        exit()


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
        except ValueError:
            if __intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                exit()
            print("\n** Opcion incorrecta **\n")
            __intentos += 1
    if eleccion == 1:
        __tickers = input(
            "\nPor favor, ingrese los tickers separados por coma: "
        ).split(",")
        __tickers = [ticker.upper().strip() for ticker in __tickers]
        tickers = {}
        for ticker in __tickers:
            tickers[ticker] = []
        print("\n** La lista de tickers actual es: ", __tickers, "**\n")
        periodo_seleccionado = periodo()
        print("\nComenzando analisis...")

        return tickers, periodo_seleccionado

    elif eleccion == 2:
        tickers = {}
        print(
            'Deberá ingresar la lista de tickers en un archivo de texto, separados por coma y sin espacios, para su conveniencia el archivo ya ha sido generado, con el nombre de "tickers.txt".'
        )
        system("touch tickers.txt")
        input('una vez que haya ingresado los tickers, presione "Enter"')
        __tickers = open("tickers.txt", "r").read().split(",")
        __tickers = [ticker.upper().strip() for ticker in __tickers]
        print("Los tickers ingresados son: ", __tickers)
        for ticker in __tickers:
            tickers[ticker] = []
        periodo_seleccionado = periodo()
        print("Comenzando analisis...")
        return tickers, periodo_seleccionado

    elif eleccion == 3:
        print("La lista de tickers actual es: ", tickers.keys())
        periodo_seleccionado = periodo()
        print("\nComenzando analisis...")
        return tickers, periodo_seleccionado

    elif eleccion == 0:
        exit()


if __name__ == "__main__":
    bienvenida()
