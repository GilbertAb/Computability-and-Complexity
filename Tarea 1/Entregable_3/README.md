# Tarea Programada 1: Entregable 3

## **Problema a resolver**

Construir una aplicación que muestre información de avistamientos de OVNI'S, tomados desde un archivo de entrada tipo XML. En este archivo se muestran una lista de avistamientos divididos en evento, fecha, hora, descripción, país, entre otros datos. Para la resolución de este problema es necesario un analizador léxico y sintáctico que convierta este archivo en datos de entrada válidos para la aplicación a implementar.

## **Descripción del archivo XML base**

El archivo consta de tres partes divididas claramente:

1. Lista de estados: Consiste en una lista de los estados o lugares donde ha habido al menos un reporte de avistamiento de OVNI.

2. Lista de formas: Consiste en una lista de las formas de los OVNIS que han sido reportadas.

3. Lista de eventos: Es la lista más larga y compleja. Consiste en una lista de cada uno de los eventos (avistamientos) que han sido reportados. Se divide en diversos tipos de datos del reporte como lugar, hora, entre otros. Además provee un link donde se puede ver la descripción completa del suceso.

> Cada una de las etiquetas que están en el archivo XML tienen una etiqueta de apertura **_<ejemplo\>_** y una etiqueta de cierre **_</ejemplo\>_**.

## **Descripción de la solución**

La solución consta de dos analizadores: uno léxico y otro sintáctico. El analizador léxico recibe como entrada el archivo XML y se encarga de leerlo línea por línea mientras va separándolo en tokens que ya fueron especificados en el programa, mediante expresiones regulares establecidas. Además, genera una salida la cual es la entrada del analizador sintáctico correspondiente. Este analizador sintáctico es el encargado de revisar cada uno de los tokens y darse cuenta de si cumplen o no las reglas que de igual forma se establecieron en el mismo programa. 

Esta solución se divide en 5 etapas, en las cuales se van agregando funcionalidades escaladamente. Para esta tercera etapa, se cuenta con archivo en código python, llamado ***lexical_analyzer.py*** en el que se cuenta con el siguiente formato y funcionalidades:

+ A) Formato:
  + Lista de tokens: Una lista de cada uno de los tokens que se van a desprender de las etiquetas y de los datos contenidos en el archivo XML. 

    ![Tokens_list](Imagenes/Tokens_list.png)

  + Expresiones regulares simples: Son aquellas expresiones regulares que no pasan de una línea de extensión, las cuales analizan cada una de las etiquetas del archivo XML.

    ![Simple_regular_expressions](Imagenes/Simple_regular_expressions.png)

  + Expresiones regulares complejas: Son expresiones regulares que tienen una densidad de análisis más amplia, usadas para extraer los datos contenidos en el interior de cada etiqueta de apertura y de cierre.

    ![Complex_regular_expressions](Imagenes/Complex_regular_expressions.png)

  + Lectura del archivo XML: Esta parte consta de una función para la apertura del archivo XML y su respectiva lectura línea por línea para su respectivo análisis.

    ![XML_Reading](Imagenes/XML_Reading.png)

  + Separar e imprimir: Se separa cada etiqueta y su contenido en los tokens respectivos y se muestra en la salida estándar su lectura y respectivo contenido de cada uno de ellos.

    ![Tokenizing&Printing](Imagenes/Tokenizing&Printing.png)

## **Ejecución del programa**

Para poder ejecutar el programa y ver la respectiva salida, es necesario tener alguna versión de python instalada en el sistema operativo en el cual va a hacer la ejecución. Además, es necesario hacer la respectiva inclusión de la biblioteca _ply_ de python, la cual contiene los respectivos analizadores léxico (lexer) y sintáctico a utilizar.

Para la respectiva ejecución, hay que ubicarse en la carpeta que contiene el archivo _.py_ y simplemente hay que escribir el siguiente comando:

`py lexical_analyzer.py`

O, su equivalente:

`python lexical_analyzer.py`

Esto va a mostrar en la salida estándar la respectiva salida del programa.