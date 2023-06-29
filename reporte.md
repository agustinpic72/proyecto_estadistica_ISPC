# Graficos  
## Correlacion_volatilidad.png
Este grafico se realiza con el fin de analizar la correlacion entre los movimientos de las acciones, para reconocer patrones en el comportamiento de las mismas basandose en el tipo de acción que se analiza, utilizando los datos por defecto podemos ver como se forma un patrón similar a una cruz azul representando la poca correlación que tiene **GGAL** *Grupo financiero Galicia* con el resto de tickers dispuestos en el analisis.  
Esto evidentemente se dá porque es una empresa que poco tiene que ver con el resto, reflejado a su vez en la volatilidad.  
Algunos grupos tipicos que podemos reconocer serían  industriales, tecnologicas, bancarias, etc.  

## desviacion_estandar_de_la_volatilidad.png
Representa la desviación estandar de la volatilidad de cada acción, en el caso de **GGAL** *Grupo financiero Galicia* podemos ver como otra vez es la que mayores cifras representa, aunque no deja atras otras tecnologicas de alto crecimiento como **Amazon, Tesla y Netflix**.  
Mas adelante veremos los picos de volatilidad de cada empresa, representado en porcentajes y comparando la diferencia entre subas y bajas, es decir los maximos días positivos y negativos respectivamente.  

## dividendos_acumulados.png
Se grafica la acumulación de los dividendos en el periodo de tiempo seleccionado, cabe aclarar que en este grafico no podemos ver todas las empresas de la lista ya que no todas pagan dividendos.   
Explicado esto, podemos ver como **Microsoft** es la que mas ha pagado, seguida por **Coca-Cola** y **Ford**.  
Es importante entender dos cosas:  
    -*Coca-Cola* paga dividendos desde **1962** y *Microsoft* desde **2005**.  
    -Por mas que *Microsoft* y *Coca-Cola* esten en el top de dividendos, esto no significa que sean las mas rentables, ya que el precio de la acción es mucho mas alto que el de Ford, por lo que el porcentaje de dividendos que paga Ford es mucho mayor.  

## ganancias_acumuladas.png
En esta imagen podemos ver el rendimiento acumulado en forma porcentual de cada empresa, en el periodo seleccionado, podemos deducir que todas las empresas han tenido un crecimiento positivo, aunque algunas mas que otras.  

## maximos_historicos.png
Este reporte se genera para visualizar el precio mas alto alcanzado por cada empresa en el periodo seleccionado, la idea es a futuro poder utilizar estos datos para realizar una estadistica pensando en medir que porcentaje de su maximo historico ha sido retribuido en forma de dividendos a los inversores.  

## picos_de_volatilidad.png
Esta estadistica es importante para comprender los picos que se pueden alcanzar en una jornada tipica, para valorar el riesgo que representa tener una empresa en la cartera, se plotea como porcentaje al alza en *azul* y a la baja en *naranja*, sabiendo esto podemos tener una idea clara de cuanto puede subir/bajar nuestra inversion en el corto periodo de **1 dia** siendo la peor de las perdidas un *65.79%* para **GGAL** .  

## precios_históricos.png
Podemos ver la evolución historica del precio de cada acción, comenzando desde el periodo de cotización mas tardió, es decir que si una empresa cotiza desde **1990** y otra desde **2000** el grafico comenzará desde el año **2000**.  

### Conclusiones
Cada uno de los graficos conforma una parte de todo el analisis aclarando un poco la visión del inversor a la hora de elegir una compañia para invertir.  

# Datos  
## dividendos.csv
Dentro de este archivo nos encontramos con la siguiente estructura:  
    | fecha | tickers |  
Dando un rapido vistazo nos damos cuenta que los datos estan ordenados por fecha, y que cada fila representa un pago de dividendos de una empresa en particular, los datos muchas veces son simplemente un **0.00**, esto sucede porque los dividendos se pagan 4 veces al año, llevando a este patrón que mezcla 0's y datos.  
Decidí dejar los 0's dentro del excel porque a futuro se pueden utilizar estadisticas como el espacio de tiempo entre un pago y otro, la cantidad de pagos en un año, si se respetaron las fechas, si se pagaron todos los dividendos correspondientes, etc.  

## precios_cierre.csv
Dentro de este archivo nos encontramos con la misma estructura ya mencionada en el caso anterior.  
    | fecha | tickers |  
En este caso los datos representan el precio de cierre de cada acción en el periodo de tiempo seleccionado.
Este reporte se genera desde la fecha de inicio de cotización mas **tardía**.  

## volatilidad.csv
Dentro de este archivo nos encontramos con la misma estructura ya mencionada en el caso anterior.  
    | fecha | tickers |  
En este caso los datos representan la volatilidad de cada acción en el periodo de tiempo seleccionado.
Este reporte se genera desde la fecha de inicio de cotización mas **temprana** a diferencia de la estadistica anterior, esto nos da un mayor nivel de precisión a la hora de calcular estadisticas referidas a la *volatilidad* teniendo los datos desde el principio hasta el momento actual de la misma.  

## Archivos especificos de cada empresa
Estos son los archivos que mas información contienen siendo los datasets en crudo descargados desde la API de Yahoo Finance, los mismos contienen los datos de cada empresa desde su fecha de inicio de cotización hasta el momento actual, estos archivos se utilizan para generar los graficos de precios historicos, volatilidad y dividendos acumulados.  
Podemos encontrar los datos representados con la siguiente estructura:  
    | fecha | apertura | cierre | maximo | minimo | volumen | dividendos | splits |  
Teniendo disponible toda la información necesaria para realizar cualquier tipo de analisis.



