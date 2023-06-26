import pandas as pd
import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt
from GUI import lista_de_tickers


# Generar dataframes con datos históricos de precios de acciones
def generar_datasets(tickers, start="2010-01-01", end="2020-12-31", max=False):
    """
    Genera un dataset con datos históricos de precios de acciones.

    Parameters
    ----------
    tickers : list
        Lista de símbolos de acciones.
    start : str
        Fecha de inicio de los datos.
    end : str
        Fecha de fin de los datos.

    Returns
    -------
    df : pandas.DataFrame
        Dataset con datos históricos de precios de acciones.

    """
    for ticker in tickers.keys():
        df = (
            yf.Ticker(ticker).history(period=max)
            if max
            else yf.Ticker(ticker).history(start=start, end=end)
        )
        tickers[ticker] = df
    return tickers


def guardar_datasets(tickers):
    for ticker in tickers.keys():
        tickers[ticker].to_csv("datos/" + ticker + ".csv")


# Analisis de volatilidad
def calculo_volatilidad(
    tickers,
):  # calcula la volatilidad dia a dia y la devuelve en un dataframe
    volatilidad_df = pd.DataFrame()
    for ticker in tickers.keys():
        volatilidad_df[ticker] = (
            tickers[ticker]["Close"] * 100 / tickers[ticker]["Open"] - 100
        )
    volatilidad_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    volatilidad_df.to_csv("datos/volatilidad.csv")
    return volatilidad_df


def informacion_general_volatilidad():
    df = pd.read_csv("datos/volatilidad.csv")
    mensaje = "Analisis de volatilidad"
    columnas = df.columns
    longitud_texto = [len(col) for col in columnas]
    print(mensaje.center(sum(longitud_texto) * 2))
    print(df.describe(), "\n\n")


def graficar_volatilidad(volatilidad_df, datasets):
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
    plt.savefig("graficos/volatilidad_maxima_y_minima.png")
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
    desv_estandar = pd.read_csv("datos/volatilidad.csv").describe().loc["std"]
    fig, ax = plt.subplots()
    ax.set_title("Desviación estándar")
    ax.bar(desv_estandar.index, desv_estandar.values)
    label_desv_estandar = [("%.2f" % value) for value in desv_estandar.values]
    ax.bar_label(ax.containers[0], labels=label_desv_estandar)
    plt.xlabel("Variables")
    plt.ylabel("Valor")
    plt.savefig("graficos/desviacion_estandar_de_la_volatilidad.png")


# Analisis de precio de cierre


def generar_y_graficar_dataframe_precios_de_cierre(
    tickers,
):  # Esta funcion almacena los datos en un dataframe y los guarda en un archivo csv
    precios_df = pd.DataFrame()
    for ticker in tickers.keys():
        df = tickers[ticker]
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
    ax.set_title("Precios máximos de cierre")
    plt.ylabel("Precio de cierre en USD")
    plt.xlabel("Empresa")
    plt.savefig("graficos/precios_maximos.png")
    return precios_df


def informacion_general_precios_de_cierre():
    df = pd.read_csv("datos/precios_cierre.csv")
    columnas = df.columns
    longitud_texto = [len(col) for col in columnas]
    mensaje = "Analisis de precios de cierre"
    print(mensaje.center(sum(longitud_texto) * 2))
    print(df.describe(), "\n\n")


def plotear_precios_historicos():
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


# Analisis de dividendos


def generar_dataframe_dividendos(
    tickers,
):  # Esta funcion filtra las empresas que pagan dividendos, almacena los datos en un dataframe y los guarda en un archivo csv
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
    plt.savefig("graficos/pagos_acumulados.png")


if __name__ == "__main__":
    periodo = False
    __default = {
        "AMZN": [],
        "KO": [],
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
    datasets = generar_datasets(default, max=periodo)
    volatilidad = calculo_volatilidad(datasets)
    guardar_datasets(datasets)
    generar_y_graficar_dataframe_precios_de_cierre(datasets)
    informacion_general_volatilidad()
    graficar_volatilidad(volatilidad, datasets)
    informacion_general_precios_de_cierre()
    plotear_precios_historicos()
    generar_dataframe_dividendos(default)
    pagos_acumulados()
    graficar_desviacion_estandar_de_la_volatilidad()
    graficar_correlacion_volatilidad(default)
