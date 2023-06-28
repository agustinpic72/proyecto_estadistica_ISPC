# Proyecto final - Procesamiento de datos

## Descripción del proyecto

Proyecto de Procesamiento de Datos con python, utilizando las librerias [pandas](https://pandas.pydata.org/docs/), [yfinance](https://pypi.org/project/yfinance/), [numpy](https://numpy.org/doc/) y [matplotlib](https://matplotlib.org/).  
Se utiliza la API de Yahoo Finance para obtener los datos de las acciones de las empresas que se desean analizar para posteriormente realizar un analisis exploratorio de los datos, y un analisis de correlacion entre las acciones.    
Se le puede pasar una lista con tickers de empresas para que el programa genere los graficos y los reportes de las empresas que se desean analizar o bien utilizar la lista de empresas que se encuentra en el archivo main.py.  
## Requisitos del proyecto y algunos datos utiles
Utilice el siguiente comando para instalar las librerias necesarias para correr el proyecto:  
(*Se recomienda utilizar el entorno virtual de su preferencia*)
```bash
pipenv install -r requirements.txt
```
¿Que es un ticker?  
> Un ticker es un símbolo que representa a una empresa en la bolsa de valores.

¿Donde los puedo encontrar?  
> Los tickers se pueden encontrar en la pagina de [Yahoo Finance](https://finance.yahoo.com/), en la seccion de *'Statistics'* de cada empresa.
> Tambien aparecen en la barra de busquedas como *'Symbol'*, solo deberemos tipear el nombre de la empresa que queremos buscar. 

¿Puedo usar cualquier ticker?  
> Si, siempre y cuando la empresa se encuentre en la bolsa de valores y tenga un ticker asignado.  

Las carpetas '*datos*' y '*graficos*' se generan automaticamente con la primera ejecución del proyecto, en caso de no ser generadas se pueden generar manualmente.
## Uso del proyecto
Para correr el proyecto tenemos que utilizar el siguiente comando:
```bash
python3 main.py
```
Que nos va a mostrar el siguiente menu:
```bash
Los tickers disponibles de manera predeterminada son:
*                          AMZN
*                            KO
*                          AAPL
*                          MSFT
*                          GGAL
*                             F
*                          TSLA
*                          GOOG
*                          NFLX
*                          META

Elija una opcion: 
                         1. Ingresar tickers manualmente
                         2. Ingresar tickers desde un archivo
                         3. Utilizar los tickers por defecto
                         0. Salir
```
Se pueden agregar todos los tickers que se deseen, pero se recomienda no agregar mas de 5 para que el analisis sea mas rapido.  
No se pueden mezclar criptomonedas con acciones tradicionales debido a que existe una diferencia en los periodos de cotizacion entre ambos activos financieros, resultando en un problema al momento de realizar el analisis.  
Si elegimos la opcion 1, nos va a pedir que ingresemos los tickers de las empresas que queremos analizar, separados por una coma.  
Si elegimos la opcion 2, nos va a pedir que ingresemos los tickers de las empresas que queremos analizar, separados por una coma en un archivo que se genera automaticamente en la carpeta del proyecto llamado *'tickers.txt'*.  
Si elegimos la opcion 3, se van a utilizar los tickers por defecto que se encuentran en el archivo main.py.  
Si elegimos la opcion 0, se va a salir del programa.  

Luego de elegir los tickers de las empresas a analizar se va a solicitar que ingrese un periodo de tiempo para analizar los datos, se puede elegir entre varias opciones predeterminadas como vemos en este menu:  
```bash
** La lista de tickers actual es:  ['KO', 'META', 'AAPL'] **


Seleccione el periodo de tiempo a analizar:
                                                1. Máximo
                                                2. 5 años
                                                3. 1 año
                                                4. 6 meses
                                                5. 1 mes
                                                6. 5 días
                                                0. Salir
```  
(*Si elegimos la opcion 1, se va a analizar el periodo maximo de tiempo disponible en la base de datos de yahoo finance.*)  
Una vez seleccionado el periodo de tiempo, se generaran diferentes graficos y reportes en la carpeta *'graficos'* y *'datos'* respectivamente.  
Entre los graficos se encuentran:
- Correlacion de los movimientos entre las acciones.
- Desviacion estandar de la volatilidad.
- Ganancias y perdidas acumuladas en porcentaje.
- Pagos de dividendos acumulados en el periodo de tiempo seleccionado.  
- Evolucion del precio de cierre de las acciones.
- Precios maximos alcanzados en el periodo de tiempo seleccionado.
- Volatilidad maxima y minima en una jornada tipica.

A su vez tambien podemos encontrar los siguientes reportes en formato CSV:  
- Volatilidad detallada en cada jornada tipica.
- Reporte de cada empresa con todos los datos incluidos.
- Dividendos pagados en el periodo de tiempo seleccionado.
- Precios de cierre por jornada.



## Estructura del repositorio
El repositorio contiene los siguientes archivos:
- main.py: Archivo principal del proyecto, contiene el codigo fuente.
- GUI.py: Contiene la interfaz del proyecto.
- datos: Carpeta que contiene los datos utilizados para el analisis que a su vez actuan como reportes.
- graficos: Carpeta que contiene los graficos generados por el proyecto.
- requirements.txt: Contiene las dependencias del proyecto.
- README.md: Contiene la informacion del proyecto.

## Conclusiones
Disfrute y aprendí mucho haciendo este trabajo, el tema de las finanzas es algo que me gusta y me interesa mucho, por lo que me parecio una buena oportunidad para seguir aprendiendo como utilizar las librerias de python para el analisis de datos.  
En un comienzo los objetivos del proyecto eran analizar datos estaticos pero a mitad del desarrollo me decidí por cambiar todo para que sea adaptable en tiempo real y que también se pudiera elegir cualquier empresa de la que se desee obtener información (y que este disponible en la API de Yahoo Finance) en lugar de tener que modificar el código cada vez que se quiera analizar una empresa diferente.
Algunas dificultades que se me presentaron, fueron problemas sobretodo con las librerias y sus metodos, también el hecho de generar estadisticas que sean realmente significativas para el tema a tratar y que no sean solo numeros sin sentido.  
A pesar de que aún haya cosas que retocar y mejorar, estoy conforme con el resultado generado y con lo que aprendi en el proceso.

#### Autor:
    -Agustin Piccoli