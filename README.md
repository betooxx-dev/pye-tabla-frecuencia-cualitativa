# Análisis Estadístico de Equipos de Fútbol

Este proyecto es un examen práctico del primer corte de la asignatura de Probabilidad y Estadística. Utiliza Python para realizar un análisis estadístico básico sobre la frecuencia de aparición de equipos de fútbol en un conjunto de datos.

## Descripción

El programa realiza las siguientes tareas:

1. Crea un DataFrame con datos de equipos de fútbol.
2. Genera una tabla de frecuencia con frecuencias absolutas y relativas.
3. Crea un diagrama de barras para visualizar las frecuencias absolutas.
4. Genera una gráfica circular para representar las frecuencias relativas.

## Requisitos

- Python 3.x
- pandas
- matplotlib

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala las bibliotecas necesarias ejecutando:
   ```
   pip install pandas matplotlib
   ```
3. Descarga el archivo `main.py` de este repositorio.

## Uso

1. Ejecuta el script desde la línea de comandos:
   ```
   python main.py
   ```
2. El programa mostrará la tabla de frecuencia en la consola y generará dos gráficos:
   - Un diagrama de barras
   - Una gráfica circular

## Estructura del código

- El código comienza con la importación de las bibliotecas necesarias y la definición de los datos.
- Se crea un DataFrame de pandas con los datos de los equipos.
- Se genera una tabla de frecuencia utilizando `value_counts()` de pandas.
- Se utilizan funciones de matplotlib para crear las visualizaciones.

## Resultados

El programa genera:
1. Una tabla de frecuencia impresa en la consola.
2. Un diagrama de barras mostrando la frecuencia absoluta de cada equipo.
3. Una gráfica circular representando la frecuencia relativa de cada equipo.

## Notas

- Este proyecto es un ejemplo básico de análisis estadístico y visualización de datos.
- Los datos utilizados son una muestra y pueden ser modificados según sea necesario.
