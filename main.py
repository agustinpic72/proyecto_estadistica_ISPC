import pandas as pd
import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt
from GUI import lista_de_tickers, limpieza_de_archivos


def generar_datasets(tickers, start="2010-01-01", end="2020-12-31", periodo=False):
    """
    Genera un dataset con datos históricos de precios de acciones.

    Parameters
    ----------
    tickers : list
        Diccionario de símbolos de acciones.
    start : str
        Fecha de inicio de los datos.
    end : str
        Fecha de fin de los datos.
    periodo : str
        Periodo de tiempo a analizar.

    Returns
    -------
    df : pandas.DataFrame
        Dataset con datos históricos de precios de acciones.

    """

    for ticker in tickers.keys():
        try:
            df = (
                yf.Ticker(ticker).history(period=periodo)
                if periodo
                else yf.Ticker(ticker).history(start=start, end=end)
            )
            if df.empty:
                print("No hay datos disponibles para el ticker", ticker)
                tickers[ticker] = pd.DataFrame()
                continue
            else:
                tickers[ticker] = df
        except yf.TickerError as e:
            print("Error al obtener información del ticker:", e)
            tickers[ticker] = pd.DataFrame()
    _empty_tickers = {k: v for k, v in tickers.items() if v.empty}
    for ticker in _empty_tickers:
        tickers.pop(ticker)
    if not tickers:
        print("No se pudo obtener información de ningún ticker")
        exit()
    return tickers


def guardar_datasets(datasets):
    """
    Guarda cada dataframe generado en un archivo CSV con el nombre del ticker

    Parameters
    ----------
    datasets : dict
        Diccionario de dataframes de cada accion.
    ----------
    """
    for ticker in datasets.keys():
        datasets[ticker].to_csv("datos/" + ticker + ".csv")


def calculo_volatilidad(
    datasets,
):
    """
    Calcula la volatilidad de cada accion y la devuelve en un dataframe

    Parameters
    ----------
    datasets : dict
        Diccionario de dataframes de cada accion.
    ----------

    Returns
    -------
    volatilidad_df : pandas.DataFrame
        Dataframe con la volatilidad de cada accion.

    """
    volatilidad_df = pd.DataFrame()
    for ticker in datasets.keys():
        volatilidad_df[ticker] = (
            datasets[ticker]["Close"] * 100 / datasets[ticker]["Open"] - 100
        )
    volatilidad_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    volatilidad_df.to_csv("datos/volatilidad.csv")
    return volatilidad_df


def informacion_general_volatilidad():
    """
    Imprime en consola informacion general sobre la volatilidad registrada en el archivo CSV generado
    """
    df = pd.read_csv("datos/volatilidad.csv")
    mensaje = "Analisis de volatilidad"
    columnas = df.columns
    longitud_texto = [len(col) for col in columnas]
    print(mensaje.center(sum(longitud_texto) * 2))
    print(df.describe(), "\n\n")


def graficar_volatilidad(volatilidad_df, datasets):
    """
    Grafica la volatilidad maxima y la volatilidad minima registrada en un periodo (generalmente un dia)
    Tambien grafica la volatilidad acumulada de cada accion, es decir, las ganancias/perdidas que se obtendrian

    Parameters
    ----------
    volatilidad_df : pandas.DataFrame
        Dataframe con la volatilidad de cada accion.
    datasets : dict
        Diccionario con los dataframes de cada accion.
    ----------
    """
    tickers = (
        volatilidad_df.columns[1:]
        if volatilidad_df.columns[0] == "Date"
        else volatilidad_df.columns
    )
    mayor_alza = []
    mayor_baja = []
    for ticker in tickers:
        mayor_alza.append(volatilidad_df[ticker].max())
        mayor_baja.append(volatilidad_df[ticker].min() * -1)
    fig, ax = plt.subplots()
    ax.set_title("Volatilidad máxima y mínima en un periodo")
    plt.ylabel("Volatilidad en %")
    plt.xlabel("Empresa")
    ax.bar(tickers, mayor_alza, label="Volatilidades")
    ax.bar(tickers, mayor_baja, bottom=mayor_alza)
    labels_alza = [("%.2f" % i) + "%" for i in mayor_alza]
    labels_baja = [("%.2f" % i) + "%" for i in mayor_baja]
    ax.bar_label(ax.containers[0], labels=labels_alza, label_type="center")
    ax.bar_label(ax.containers[1], labels=labels_baja, label_type="center")
    plt.savefig("graficos/picos_de_volatilidad.png")
    # Graficar y calcular volatilidad acumulada
    reset_index = lambda df: df.reset_index(drop=True)
    datasets = {ticker: reset_index(datasets[ticker]) for ticker in tickers}
    calcular_ganancias_acumuladas = lambda dfs: [
        (df.loc[df.index.stop - 1].Close * 100 / df.loc[0].Close) for df in dfs
    ]
    ganancias_acumuladas = {
        ticker: calcular_ganancias_acumuladas([datasets[ticker]])[0]
        for ticker in tickers
    }
    ganancias_acumuladas_df = pd.DataFrame(data=[ganancias_acumuladas])
    mensaje = "Analisis de las ganancias acumuladas en %"
    columnas = ganancias_acumuladas_df.columns
    longitud_texto = [len(col) for col in columnas]
    print(mensaje.center(sum(longitud_texto) * 2))
    print(ganancias_acumuladas_df, "\n\n")
    fig, ax = plt.subplots()
    ax.set_title("Volatilidad de las acciones")
    plt.ylabel("Volatilidad en %")
    plt.xlabel("Empresa")
    ax.set_yscale("log")
    ax.bar(
        tickers,
        ganancias_acumuladas_df.values[0],
        label="ganancias_acumuladas",
        color=["r" if va < 0 else "b" for va in ganancias_acumuladas_df.values[0]],
    )
    label_ganancias_acumuladas = [
        ("%.2f" % i) + "%" for i in ganancias_acumuladas_df.values[0]
    ]

    ax.bar_label(
        ax.containers[0],
        labels=label_ganancias_acumuladas,
        label_type="edge",
        weight="bold",
    )
    ax.axhline(y=0, color="black", linestyle="--")
    plt.savefig("graficos/ganancias_acumuladas.png")


def graficar_correlacion_volatilidad(tickers):
    """
    Grafica la correlacion entre la volatilidad de las acciones, deberiamos ver una correlacion positiva entre acciones del mismo sector

    Parameters
    ----------
    tickers : dict
        Diccionario con los tickers de las acciones.
    ----------
    """
    df = pd.read_csv("datos/volatilidad.csv")
    df = df.drop(columns=["Date"])
    corr_df = df.corr()
    tickers = corr_df.columns
    fig, ax = plt.subplots()
    ax.set_title("Correlación de la volatilidad entre empresas")
    plt.xlabel("Empresas")
    plt.ylabel("Empresas")
    ax.set_xticks(range(len(tickers)))
    ax.set_xticklabels(tickers)
    ax.set_yticks(range(len(tickers)))
    ax.set_yticklabels(tickers)
    scatter = ax.imshow(corr_df, cmap="coolwarm")
    fig.colorbar(scatter, ax=ax)
    plt.savefig("graficos/correlacion_volatilidad.png")


def graficar_desviacion_estandar_de_la_volatilidad():
    """
    Grafica la desviacion estandar de la volatilidad de las acciones
    """
    desv_estandar = pd.read_csv("datos/volatilidad.csv").describe().loc["std"]
    fig, ax = plt.subplots()
    ax.set_title("Desviación estándar de la volatilidad")
    ax.bar(desv_estandar.index, desv_estandar.values)
    label_desv_estandar = [("%.2f" % value) for value in desv_estandar.values]
    ax.bar_label(ax.containers[0], labels=label_desv_estandar)
    plt.xlabel("Variables")
    plt.ylabel("Valor")
    plt.savefig("graficos/desviacion_estandar_de_la_volatilidad.png")


def generar_y_graficar_dataframe_precios_de_cierre(
    datasets,
):
    """
    Genera un dataframe que posteriormente guarda en un archivo CSV para poder graficar los precios de cierre de las acciones

    Parameters
    ----------
    datasets : dict
        Diccionario con los tickers y dataframes de las acciones.
    ----------
    """
    precios_df = pd.DataFrame()
    for ticker in datasets.keys():
        df = datasets[ticker]
        precios_df[ticker] = df["Close"]
    precios_df.dropna(axis=0, inplace=True)
    precios_df.to_csv("datos/precios_cierre.csv")
    # Graficar dataframe
    fig, ax = plt.subplots()
    tickers = (
        precios_df.columns[1:]
        if precios_df.columns[0] == "Date"
        else precios_df.columns
    )
    for i, ticker in enumerate(tickers):
        precio_maximo = "$%.2f" % precios_df[ticker].max()
        ax.bar(ticker, precios_df[ticker].max())
        ax.bar_label(ax.containers[i], labels=[precio_maximo], padding=3)
    ax.set_title("Maximos Historicos")
    plt.ylabel("Precio de cierre en USD")
    plt.xlabel("Empresa")
    plt.savefig("graficos/maximos_historicos.png")
    return precios_df


def informacion_general_precios_de_cierre():
    """
    Imprime informacion general del archivo generado en la funcion anterior
    """
    df = pd.read_csv("datos/precios_cierre.csv")
    columnas = df.columns
    longitud_texto = [len(col) for col in columnas]
    mensaje = "Analisis de precios de cierre"
    print(mensaje.center(sum(longitud_texto) * 2))
    print(df.describe(), "\n\n")


def plotear_precios_historicos():
    """
    Grafica un grafico de linea de los precios de cierre de las acciones durante el periodo seleccionado
    """
    df = pd.read_csv("datos/precios_cierre.csv")
    fig, ax = plt.subplots()
    ax.set_title("Precios históricos de cierre")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre en USD")
    tickers = df.columns[1:] if df.columns[0] == "Date" else df.columns
    for ticker in tickers:
        ax.plot(df[ticker], label=ticker)
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para que sean más legibles
    ax.legend()
    plt.savefig("graficos/precios_historicos.png")


def generar_dataframe_dividendos(
    tickers,
):
    """
    Genera un dataframe que posteriormente guarda en un archivo CSV para poder graficar los dividendos de las acciones

    Parameters
    ----------
    tickers : dict
        Diccionario con los tickers de las acciones.
    ----------
    """
    dividendos_df = pd.DataFrame()
    for ticker in tickers.keys():
        df = tickers[ticker]
        dividendos_df[ticker] = df["Dividends"]
        if sum(df["Dividends"]) == 0:
            dividendos_df.drop(ticker, axis=1, inplace=True)
    dividendos_df.dropna(axis=0, inplace=True)
    dividendos_df.to_csv("datos/dividendos.csv")
    return dividendos_df


def pagos_acumulados():
    """
    Grafica la suma de todos los dividendos pagados por las empresas en el periodo seleccionado
    """
    df = pd.read_csv("datos/dividendos.csv")
    tickers = df.columns[1:] if df.columns[0] == "Date" else df.columns
    suma_dividendos = []
    for ticker in tickers:
        suma_dividendos.append(sum(df[ticker]))
    fig, ax = plt.subplots()
    ax.set_title("Pagos acumulados de dividendos")
    ax.bar(tickers, suma_dividendos)
    label_dividendos = [("$%.2f" % i) for i in suma_dividendos]
    ax.bar_label(ax.containers[0], labels=label_dividendos)
    plt.xlabel("Empresa")
    plt.ylabel("Pagos acumulados en USD")
    plt.savefig("graficos/dividendos_acumulados.png")


if __name__ == "__main__":
    limpieza_de_archivos()
    periodo = False
    __default = {
        "KO": [],
        "AMZN": [],
        "AAPL": [],
        "MSFT": [],
        "GGAL": [],
        "F": [],
        "TSLA": [],
        "GOOG": [],
        "NFLX": [],
        "META": [],
    }
    default, periodo = lista_de_tickers(__default)
    datasets = generar_datasets(default, periodo=periodo)
    volatilidad_df = calculo_volatilidad(datasets)
    guardar_datasets(datasets)
    generar_y_graficar_dataframe_precios_de_cierre(datasets)
    informacion_general_volatilidad()
    graficar_volatilidad(volatilidad_df, datasets)
    informacion_general_precios_de_cierre()
    plotear_precios_historicos()
    generar_dataframe_dividendos(default)
    pagos_acumulados()
    graficar_desviacion_estandar_de_la_volatilidad()
    graficar_correlacion_volatilidad(default)
