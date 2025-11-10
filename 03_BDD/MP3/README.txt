Instrucciones Miniproyecto 3
Introducción

Este miniproyecto busca evaluar los contenidos de los módulos 5 y 6.
Se recomienda fuertemente haber visto las clases de estos módulos y la ayudantía de preparación antes de comenzar este trabajo.

Set de datos

En este caso no hay un archivo para descargar, ya que los datos se obtendrán directamente desde una API pública.

La API entrega información de todos los feriados del año 2024.
La URL a utilizar es:

https://www.chia.cl/api/feriados/2024


Para comprender mejor su funcionamiento y estructura, puedes revisar la documentación oficial en:

https://www.chia.cl/api/feriados

Trabajo a realizar

Sigue cuidadosamente los siguientes pasos:

1. Crear el programa

Crea un nuevo archivo de Python llamado:

mp3.py

2. Conectarse a MongoDB

Desde el programa, conéctate a una base de datos MongoDB llamada:

feriados

3. Obtener e importar los datos

Utiliza la API indicada anteriormente para extraer todos los feriados del año 2024 y guárdalos en una colección llamada:

feriados2024

4. Consultas solicitadas

Realiza las siguientes consultas a la colección feriados2024, mostrando los resultados en consola:

a. Obtener todos los feriados presentes en la colección.
b. Obtener solo los feriados de tipo “Religioso”.
c. Obtener solo los feriados irrenunciables.
d. Obtener solo los feriados que incluyan el texto “Santo” en su nombre.
e. Obtener solo los feriados que se celebran entre el 11 de marzo (2024-03-11) y el 31 de agosto (2024-08-31).

💡 Cada consulta debe imprimir el resultado correspondiente en consola con claridad.

5. Insertar un nuevo feriado

Agrega manualmente un nuevo documento en la colección feriados2024 con los siguientes valores:

Campo	Valor
nombre	Unión de los dos paisajes
comentarios	Primera vez que una expedición chilena logró unir la Cordillera de los Andes y la costa del Pacífico en un solo día
fecha	2024-03-11
irrenunciable	0
tipo	Religioso