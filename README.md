# Proyecto final - Procesamiento de datos

## Descripción del proyecto

Proyecto de Procesamiento de Datos con python, utilizando la libreria pandas, yfinance, numpy y matplotlib.
Se utiliza la API de Yahoo Finance para obtener los datos de las acciones de las empresas que se desean analizar. Para posteriormente realizar un analisis exploratorio de los datos, y un analisis de correlacion entre las acciones.
Se le puede pasar una lista con tickers de empresas para que el programa genere los graficos y los reportes de las empresas que se desean analizar o bien utilizar la lista de empresas que se encuentra en el archivo main.py.
## Requisitos del proyecto
Utilice el siguiente comando para instalar las librerias necesarias para correr el proyecto:
```bash
pipenv install -r requirements.txt
```
## Uso del proyecto
Al correr el proyecto se le pedira al usuario que ingrese el nombre de las empresas que desea analizar, una vez ingresado el nombre de las empresas se generaran los graficos y los reportes en la carpeta datos.
Para correr el proyecto tenemos que utilizar el siguiente comando:
```bash
python3 main.py
```
## Estructura del repositorio
El repositorio contiene los siguientes archivos:
- main.py: Archivo principal del proyecto, contiene el codigo fuente.
- requirements.txt: Archivo que contiene las dependencias del proyecto.
- README.md: Archivo que contiene la informacion del proyecto.
- .gitignore: Archivo que contiene los archivos que se ignoran al momento de hacer un commit.
- .git: Carpeta que contiene la informacion del repositorio.
- datos: Carpeta que contiene los datos utilizados para el analisis que a su vez actuan como reportes.
- graficos: Carpeta que contiene los graficos generados por el proyecto.


#### Integrantes:
    -Agustin Piccoli