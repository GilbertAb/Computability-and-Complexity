# Universidad de Costa Rica
# Tarea Programada 2: CI-0124 - Computabilidad y Complejidad

## **1. Problema a resolver**

Proponer un problema que no se pueda resolver en tiempo polinomial, es decir de tipo NP-Duro o NP-Completo, para ser resuelto mediante tres técnicas: 

1. Fuerza bruta.
2. Una heurística específica para el problema a resolver.
3. Una metaheurística de las vistas en el curso (búsqueda tabú, simulated annealing, algoritmos genéticos) o alguna existente aprobada por la profesora.

> ### **1.1 Problema propuesto** 

El problema propuesto es la resolución del juego del sudoku mediante fuerza bruta, la heurística y metaheurística propuesta en el documento de especificación inicial, en el lenguaje de programación python. Se tomarán también las medidas del tiempo de los algoritmos de resolución para comparar rendimientos y eficiencia. Además, se van a graficar los resultados obtenidos en las pruebas y mediciones de la solución.

> ### **1.2 ¿En qué consiste el juego del sudoku?**

El sudoku es un juego matemático inventado en la década de 1970. Este juego consiste en rellenar una cuadrícula de 9x9 celdas (81 casillas) dividida en subcuadrículas de 3x3, con números que van del 1 al 9, teniendo ya algunos números asignados en dicha cuadrícula. La regla primordial del juego es que estos números del 1 al 9 no deben repetirse ya sea en una misma fila, columna, o subcuadrícula 3x3 antes mencionada.

## **2. Descripción de las soluciones**

Para cada una de las solcuiones, se tiene un archivo específico *.py* por cada uno de los algoritmos a implementar en esta tarea, excepto en el algoritmo genético, el cual tiene además un archivo *main_ga* que es el encargado de ejecutar el algoritmo.

## **3. Ejecución del programa**

Para poder ejecutar el programa y ver su salida, es necesario tener alguna versión de python instalada en el sistema operativo en el cual va a hacer la ejecución. Además de esto, para poder ver los resultados de la ejecución de los programas, se necesita tener instalado _Power BI_ en el equipo donde va a ser ejecutado el programa (se puede descargar [aquí](https://www.microsoft.com/en-us/download/details.aspx?id=58494)), ya que va a ser el programa que se va a utilizar para mostrar los gráficos y tiempos de ejecución de los algoritmos.

Para la ejecución del programa, hay que ubicarse en la carpeta que contiene los archivos _.py_ y escribir los siguientes comandos, dependiendo del caso a analizar:

+ Fuerza bruta:

`py sudoku_bf.py`

O, su equivalente:

`python sudoku_bf.py`

En el caso del algoritmo de fuerza bruta, en el programa se tiene guardado un sudoku predeterminado que es que el programa se encarga de ejecutar. Después de ejecutarlo, muestra el último sudoku resultante del análisis y un mensaje de si es solución o no. Si el algoritmo encuentra la solución correspondiente, saldrá la solución del sudoku con el mensaje ***IT'S A SOLUTION***.

+ Ramificación y poda:

Originalmente, la ejecución del programa sería igual que la del algoritmo de fuerza bruta, sin embargo, no se pudo implementar correctamente, por lo que al ejecutar el comando lo que va a hacer es mostrar errores de este programa.

+ Algoritmo genético:

Para este algoritmo, como se describió anteriormente, se tienen dos archivos: uno llamado *sudoku_ga*, propiamente con el algoritmo y otro llamado *main_ga* con la creación de una instancia y los valores con los que se desea ejecutar el algoritmo para la resolución del sudoku. Dentro del archivo de *main_ga*, se encuentran tres sudokus de diferente dificultad: uno fácil, uno medio y otro difícil. Para cambiar el que va a ser ejecutado, se tiene que ingresar al archivo mencionado y cambiar el nombre del sudoku que ejecuta el archivo *main*:

+ `sudo_e`: Sudoku dificultad fácil
+ `sudo_m`: Sudoku dificultad medio
+ `sudo_h`: Sudoku dificultad difícil

En el caso de la población, se puede cambiar el tamaño de la misma. Entre más población, mayor el tiempo que va a durar el programa en ejecución. Los demás valores son predefinidos y lo recomendable es dejarlos a como están en el archivo.

Para ejecutar el programa, se necesita ejecutar el archivo *main* con el siguiente comando:

`py main_ga.py`

O, su equivalente:

`python main_ga.py`

En este caso, el algoritmo genético va a analizar el sudoku elegido para su ejecución. Después de efectuar todo el proceso de análisis, muestra la solución del sudoku analizado y el tiempo que duró en hallar una solución. Cabe recalcar que este algoritmo no siempre va a encontrar una solución.

En el caso de los gráficos y tiempos, existe un archivo llamado *Tarea Programada 2.pbix*, el cual tiene los resultados de los programas y sus tiempos, todo en una interfaz gráfica y amigable con el usuario.

# Créditos

Erick Chicas  <erick.chicas@ucr.ac.cr>  
Daniel López <daniel.lopezalvarado@ucr.ac.cr>  
Gilbert Márquez <gilbert.marquez@ucr.ac.cr>