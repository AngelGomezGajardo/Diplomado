Introducción

Este miniproyecto busca evaluar los contenidos de los módulos 1 y 2.
Se recomienda fuertemente haber visto las clases de ambos módulos y la ayudantía de preparación antes de comenzar este trabajo.

Set de datos

Para este trabajo se usará el archivo sociedades.csv, disponible en la plataforma.

Este archivo es una versión simplificada del historial del Registro de Empresas y Sociedades desde enero hasta mayo del año 2024.
Presenta la siguiente estructura:

Columna	Tipo	Descripción
id	integer	Identificador numérico
rut	text	Rol Único Tributario, identificador de texto
nombre	text	Nombre de la sociedad
registro	datetime	Fecha y hora del registro
comuna	text	Comuna tributaria
capital	integer	Capital (efectivo) inicial

🔗 El dataset completo está disponible en:
https://datos.gob.cl/en/dataset/registro-de-empresas-ysociedades

Trabajo a realizar

Sigue los pasos en el siguiente orden:

1. Crear esquema

En MySQL Workbench, crea un nuevo esquema llamado:

mp1

2. Importar archivo

En MySQL Workbench, importa el archivo sociedades.csv como una nueva tabla llamada:

sociedades

3. Crear programa Python

Crea un nuevo programa llamado:

mp1.py

4. Conectarse a MySQL

Desde el programa Python, conéctate al esquema mp1 utilizando las credenciales de tu servidor local (por ejemplo, con mysql.connector o pymysql).

5. Ejecutar consultas SQL

Desde el programa, ejecuta las siguientes consultas y muestra los resultados por pantalla:

a) Sociedad por RUT

Obtener la información de la sociedad cuyo RUT es:

77886308-1

b) Sociedades con nombre que comienza en “Agencia”

Obtener todas las sociedades cuyo nombre comienza con “Agencia”,
sin importar mayúsculas o minúsculas.

💡 Hint: son 9 sociedades.

c) Sociedades con alto capital

Obtener todas las sociedades cuyo capital es mayor o igual a $400.000.000.

💡 Hint: son 4 sociedades.

En cada caso, imprime los resultados en consola.

6. Insertar una nueva sociedad

Desde el programa Python, inserta una nueva fila en la tabla sociedades con los siguientes datos:

Campo	Valor
id	5156305
rut	77721389-K
nombre	Estrellas SpA
registro	2024-03-11
comuna	PROVIDENCIA
capital	1000000