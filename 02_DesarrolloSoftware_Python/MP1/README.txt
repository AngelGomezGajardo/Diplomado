Instrucciones Miniproyecto 1
Descripción

En este miniproyecto deberás completar un código utilizando estructuras de datos adecuadas, que luego se utilizará para realizar una serie de consultas a una base de datos de películas y así obtener la información solicitada.

Objetivo

El objetivo de este miniproyecto es aplicar los conocimientos de tipos de datos, ciclos, condicionales y estructuras de datos secuenciales para procesar y guardar la información entregada.
Una vez hecho esto, se deberán completar diversas consultas que serán las que se utilizarán para obtener la información buscada.

Archivos entregados

Para este trabajo, se entregará una carpeta MP1.zip que contiene dos archivos:

main.py: Corresponde al archivo principal del programa, en el que deberás cargar la información entregada y completar las consultas que se solicitan.
Este es el único archivo que debes modificar.

peliculas.csv: Este archivo contiene información sobre diversas películas.
Cada línea contiene los datos de una película separados por comas (,), de la siguiente forma:

titulo,popularidad,voto_promedio,cantidad_votos,generos


Significado de cada atributo:

titulo: nombre de la película.

popularidad: número que indica la popularidad actual de la película (mayor valor = más popular).

voto_promedio: puntaje promedio de la película.

cantidad_votos: cantidad total de votos recibidos.

generos: lista de géneros a los que pertenece la película, separados por punto y coma (;).
Ejemplo: "Adventure;Action;Science Fiction" indica que la película pertenece a esos tres géneros.

Trabajo a realizar

El código entregado ya contiene el flujo del menú principal, que recibe un input indicando la consulta a realizar, abre el archivo de películas, genera una lista con cada línea y ejecuta la función correspondiente.
Tu tarea será completar las funciones indicadas a continuación.

Parte 1: Cargar los datos

Debes completar la función:

cargar_datos(lineas_archivo)


Esta función recibe una lista de líneas del archivo (cada línea en formato string) y debe crear las siguientes estructuras:

generos_peliculas:
Lista que almacena todos los géneros distintos de películas.
Cada género debe aparecer solo una vez, aunque se repita en varias películas.

peliculas_por_genero:
Lista de tuplas con el formato:

(genero, [peliculas])


El primer elemento es el nombre del género y el segundo es una lista con los nombres de las películas que poseen dicho género.
Una película puede aparecer en más de una tupla si pertenece a varios géneros.

info_peliculas:
Lista de tuplas con el formato:

(titulo, popularidad, voto_promedio, cantidad_votos, [generos])


El último elemento debe ser una lista de strings con los géneros de la película.

La función debe retornar una tupla con las tres estructuras, en este orden:

(generos_peliculas, peliculas_por_genero, info_peliculas)

Parte 2: Completar las consultas

Debes completar las siguientes funciones en el archivo main.py:

1. obtener_puntaje_y_votos(nombre_pelicula)

Recibe el nombre de una película (string) y debe retornar una tupla con:

(puntaje_promedio, cantidad_votos)

2. filtrar_y_ordenar(genero_pelicula)

Recibe el nombre de un género y debe retornar una lista con los nombres de las películas de ese género, ordenadas alfabéticamente en orden inverso (de Z a A).

3. obtener_estadisticas(genero_pelicula, criterio)

Recibe un género y un criterio, que puede ser:

“popularidad” | “voto promedio” | “cantidad votos”


Debe retornar una lista con el formato:

[max, min, promedio]


correspondiente a las películas de ese género según el criterio indicado.

💡 Para procesar la información, utiliza las estructuras creadas en la Parte 1. No es necesario usar todas, pero al menos una de ellas.

Método split()

Deberás usar el método de strings split() para separar elementos de un texto y almacenarlos en una lista:

lista = variable_string.split(separador)


Ejemplo:

variable = "Amarillo-Rojo-Azul"
lista = variable.split("-")
print(lista)


Salida:

['Amarillo', 'Rojo', 'Azul']

Archivos a entregar

Debes entregar únicamente el archivo main.py con las definiciones de las funciones completadas.

Consideraciones generales

La evaluación se realizará solo con los contenidos vistos hasta la semana 2 (tipos de datos, ciclos, condicionales, estructuras de datos secuenciales).
El uso de contenidos o herramientas no vistos en clase será penalizado.

Prohibido el uso de herramientas de generación de código.
Si utilizas material externo (libros, páginas, etc.), debes citar la fuente en el código.
No hacerlo resultará en nota mínima (1.0).

En el archivo main.py ya viene implementado un menú en consola para probar tu código.
Solo ejecútalo una vez completadas las funciones y usando inputs válidos.

La corrección se realizará mediante la ejecución directa del programa, validando los resultados impresos en consola.

El flujo principal ya está implementado, pero debes entenderlo bien, ya que en futuros proyectos deberás implementarlo tú.

El proyecto entregado con una extensión incorrecta o que no se pueda ejecutar, será calificado con nota 1.0 sin derecho a nueva entrega.