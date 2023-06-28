import os
from pathlib import Path
from time import sleep


def bienvenida():
    """
    Función que imprime un mensaje de bienvenida al usuario en caso de que ejecute este archivo por error
    """
    os.system("clear")
    mensaje = "Bienvenido a mi proyecto, para ejecutar el mismo, ejecute main.py"
    mensaje = mensaje.center(len(mensaje) + 10, " ")
    print("=" * (len(mensaje) + 3), end="\n\n")
    print("|", mensaje, "|\n", "_" * (len(mensaje) + 2))


def periodo():
    """
    Función que permite al usuario seleccionar el periodo de tiempo a analizar
    """
    intentos = 0
    while True:
        try:
            mensaje = "Seleccione el periodo de tiempo a analizar"
            mensaje = mensaje.center(len(mensaje) + 10 + len("1. maximo"), " ")
            if intentos == 0:
                os.system("clear")
                print(" ", "=" * len(mensaje), end="\n")
            eleccion = int(
                input(
                    f"""\n{mensaje.rjust(int(len(mensaje) / 2))}
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
                os.system("clear")
                mensaje = "Saliendo..."
                mensaje = mensaje.center(len(mensaje) + 10, " ")
                print("=" * len(mensaje), end="\n\n")
                print(mensaje, "\n", "_" * len(mensaje), end="\n")
                exit()
            if eleccion in [1, 2, 3, 4, 5, 6]:
                break
            intentos += 1
            if intentos >= 3:
                os.system("clear")
                mensaje = "Demasiados intentos fallidos, saliendo..."
                mensaje = mensaje.center(len(mensaje) + 10, " ")
                print("=" * len(mensaje), end="\n\n")
                print(mensaje, "\n", "_" * len(mensaje), end="\n")
                exit()
            os.system("clear")
            mensaje = 'Numero incorrecto, ingrese un numero entre "0" y "6"'
            mensaje = mensaje.center(len(mensaje) + 10, " ")
            print(" ", "=" * len(mensaje), end="\n")
            print(mensaje)
        except (ValueError, TypeError):
            intentos += 1
            if intentos >= 3:
                os.system("clear")
                mensaje = "Demasiados intentos fallidos, saliendo..."
                mensaje = mensaje.center(len(mensaje) + 10, " ")
                print("=" * len(mensaje), end="\n\n")
                print(mensaje, "\n", "_" * len(mensaje), end="\n")
                exit()
            os.system("clear")
            mensaje = 'Opcion incorrecta, ingrese un numero entre "0" y "6"'
            mensaje = mensaje.center(len(mensaje) + 10, " ")
            print(" ", "=" * len(mensaje), end="\n")
            print(mensaje)

    periodo = {1: "max", 2: "5y", 3: "1y", 4: "6mo", 5: "1mo", 6: "5d"}
    return periodo[eleccion]


def limpieza_de_archivos():
    """
    Función que se encarga de limpiar los archivos de datos y gráficos
    """
    os.system("clear")
    mensaje = "Obteniendo directorio de trabajo... "
    mensaje = mensaje.center(len(mensaje) + 16, " ")
    print(" ", "=" * len(mensaje), end="\n\n")
    print("|", mensaje, "|\n")
    dir_path = os.getcwd()
    sleep(1)
    mensaje = "Generando archivos necesarios... "
    mensaje = mensaje.center(len(mensaje) + 16, " ")
    print(" ", "=" * len(mensaje), end="\n\n")
    print("|", mensaje, "|\n", "_" * len(mensaje))
    try:
        if os.name == "posix":  # for Linux or Mac
            os.system(f"rm -f {dir_path}/datos/*.csv ")
            os.system(f"rm -f {dir_path}/graficos/*.png ")
        elif os.name == "nt":  # for Windows
            os.system(f"del {dir_path}\\datos\\*.csv /Q ")
            os.system(f"del {dir_path}\\graficos\\*.png /Q ")
    finally:
        os.makedirs(f"{dir_path}/datos", exist_ok=True)
        os.makedirs(f"{dir_path}/graficos", exist_ok=True)
    sleep(1)
    os.system("clear")


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

    os.system("clear")
    mensaje = "Los tickers disponibles de manera predeterminada son"
    mensaje = mensaje.center(len(mensaje) + 30, " ")
    print(" ", "=" * len(mensaje), end="\n\n")
    print("|", mensaje, "|\n", "_" * len(mensaje), end="\n\n")
    for ticker in tickers:
        print("*", ticker.rjust(int(len(mensaje) / 2)), end="\n")
    print("_" * len(mensaje), end="\n")

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
            print("_" * len(mensaje), end="\n")
            if eleccion in [0, 1, 2, 3]:
                break
            __intentos += 1
            if __intentos >= 3:
                os.system("clear")
                mensaje = "Demasiados intentos fallidos, saliendo..."
                mensaje = mensaje.center(len(mensaje) + 10, " ")
                print("=" * len(mensaje), end="\n\n")
                print(mensaje, "\n", "_" * len(mensaje), end="\n")
                exit()
            os.system("clear")
            print("\n** Opcion incorrecta **\n")
        except (ValueError, TypeError):
            __intentos += 1
            if __intentos >= 3:
                os.system("clear")
                mensaje = "Demasiados intentos fallidos, saliendo..."
                mensaje = mensaje.center(len(mensaje) + 10, " ")
                print("=" * len(mensaje), end="\n\n")
                print(mensaje, "\n", "_" * len(mensaje), end="\n")
                exit()
            os.system("clear")
            print("\n** Opcion incorrecta **\n")
    if eleccion == 1:
        __intentos = 0
        while True:
            try:
                __tickers = input(
                    "\nPor favor, ingrese los tickers separados por coma: "
                ).split(",")
                __tickers = [ticker.upper().strip() for ticker in __tickers]
                if __tickers[0] == "" and len(__tickers) == 1:
                    os.system("clear")
                    mensaje = "\nDebe ingresar al menos un ticker"
                    mensaje = mensaje.center(len(mensaje) + 10, " ")
                    print("=" * len(mensaje), end="\n")
                    print(mensaje, "\n", "_" * len(mensaje), end="\n")
                else:
                    break
                __intentos += 1
                if __intentos >= 3:
                    os.system("clear")
                    mensaje = "Demasiados intentos fallidos, saliendo..."
                    mensaje = mensaje.center(len(mensaje) + 10, " ")
                    print("=" * len(mensaje), end="\n\n")
                    print(mensaje, "\n", "_" * len(mensaje), end="\n")
                    exit()

            except Exception:
                __intentos += 1
                if __intentos >= 3:
                    os.system("clear")
                    mensaje = "Demasiados intentos fallidos, saliendo..."
                    mensaje = mensaje.center(len(mensaje) + 10, " ")
                    print("=" * len(mensaje), end="\n\n")
                    print(mensaje, "\n", "_" * len(mensaje), end="\n")
                    exit()
                print("=" * len(mensaje), end="\n\n")
                print("\n** Ocurrió un error al procesar el input **\n")

        tickers = {}
        for ticker in __tickers:
            tickers[ticker] = []
        os.system("clear")
        periodo_seleccionado = periodo()
        os.system("clear")
        mensaje = "Comenzando analisis..."
        mensaje = mensaje.center(len(mensaje) + 30, " ")
        print(" ", "=" * len(mensaje), end="\n\n")
        print("|", mensaje, "|\n", "_" * len(mensaje), end="\n\n")
        return tickers, periodo_seleccionado

    elif eleccion == 2:
        tickers = {}
        __intentos = 0
        while True:
            try:
                mensaje = 'debe ingresar los tickers en el archivo "tickers.txt" y presionar "Enter"'
                mensaje = mensaje.center(len(mensaje), " ")
                os.system("clear")
                print(" ", "=" * len(mensaje), end="\n\n")
                print("|", mensaje, "|\n", "_" * len(mensaje), end="\n\n")
                with open(Path("tickers.txt"), "w") as f:
                    f.write("ko,meta")
                input('Presione "Enter" para continuar')
                __tickers = open("tickers.txt", "r").read().split(",")
                __tickers = [ticker.upper().strip() for ticker in __tickers]
                for ticker in __tickers:
                    tickers[ticker] = []
                periodo_seleccionado = periodo()
                os.system("clear")
                mensaje = "Comenzando analisis..."
                mensaje = mensaje.center(len(mensaje) + 30, " ")
                print(" ", "=" * len(mensaje), end="\n\n")
                print("|", mensaje, "|\n", "_" * len(mensaje), end="\n\n")
                return tickers, periodo_seleccionado
            except (FileNotFoundError, IOError):
                __intentos += 1
                if __intentos >= 3:
                    os.system("clear")
                    mensaje = "Demasiados intentos fallidos, saliendo..."
                    mensaje = mensaje.center(len(mensaje) + 10, " ")
                    print("=" * len(mensaje), end="\n\n")
                    print(mensaje, "\n", "_" * len(mensaje), end="\n")
                    exit()
                os.system("clear")
                print("=" * len(mensaje), end="\n\n")
                print("\n** Error al leer el archivo de tickers **\n")
            except Exception:
                __intentos += 1
                if __intentos >= 3 or periodo_seleccionado == 0:
                    os.system("clear")
                    mensaje = "Demasiados intentos fallidos, saliendo..."
                    mensaje = mensaje.center(len(mensaje) + 10, " ")
                    print("=" * len(mensaje), end="\n\n")
                    print(mensaje, "\n", "_" * len(mensaje), end="\n")
                    exit()
                print("\n** Ocurrió un error al procesar los tickers **\n")

    elif eleccion == 3:
        periodo_seleccionado = periodo()
        os.system("clear")
        mensaje = "Comenzando analisis..."
        mensaje = mensaje.center(len(mensaje) + 30, " ")
        print(" ", "=" * len(mensaje), end="\n\n")
        print("|", mensaje, "|\n", "_" * len(mensaje), end="\n\n")
        return tickers, periodo_seleccionado

    elif eleccion == 0:
        exit()


if __name__ == "__main__":
    bienvenida()
