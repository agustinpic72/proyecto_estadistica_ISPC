from os import system


def bienvenida():
    print("Bienvenido a mi proyecto, para ejecutar el mismo, ejecute main.py")


def periodo():
    __intentos = 0
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


def lista_de_tickers(tickers):
    __intentos = 0
    print("Los tickers disponibles de manera predeterminada son")
    for ticker in tickers:
        print("*", ticker.rjust(len("\nLos tickers disponibles son:")))
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
    else:
        if __intentos >= 3:
            print("Demasiados intentos, saliendo...")
            exit()
        print("Opcion incorrecta")


if __name__ == "__main__":
    bienvenida()