Instrucciones Miniproyecto 2
Introducción

Este miniproyecto busca evaluar los contenidos de los módulos 3 y 4.
Se recomienda fuertemente haber visto las clases de los módulos y la ayudantía de preparación antes de comenzar este trabajo.

Set de datos

Para este trabajo se usarán 4 datasets distintos, pertenecientes al esquema de una tienda en línea (e-commerce).
Los archivos son:

1. productos.csv

Productos que la tienda vende.

Columna	Descripción	Tipo	Otros detalles
id	Identificador numérico	INTEGER	Llave primaria
nombre	Nombre del producto	VARCHAR(255)	—
descripcion	Descripción del producto	VARCHAR(255)	—
precio	Precio en CLP	INTEGER	—
2. clientes.csv

Clientes que han comprado en la tienda.

Columna	Descripción	Tipo	Otros detalles
id	Identificador numérico	INTEGER	Llave primaria
nombre	Nombre del cliente	VARCHAR(255)	—
email	Correo electrónico	VARCHAR(255)	—
3. pedidos.csv

Historial de pedidos hechos a la tienda.

Columna	Descripción	Tipo	Otros detalles
id	Identificador numérico	INTEGER	Llave primaria
fecha	Fecha del pedido	DATE	—
direccion	Dirección de envío	VARCHAR(255)	—
id_cliente	Cliente que lo solicitó	INTEGER	Referencia a clientes(id)
detalle	Detalles del pedido	VARCHAR(255)	—
4. productos_pedidos.csv

Contiene una relación N-N entre productos y pedidos.
Permite saber todos los productos incluidos en un pedido y todos los pedidos donde aparece un producto.

Columna	Tipo	Detalles
id_producto	INTEGER	Parte de la llave primaria compuesta. Referencia a productos(id)
id_pedido	INTEGER	Parte de la llave primaria compuesta. Referencia a pedidos(id)
cantidad	INTEGER	—

💡 La llave primaria de esta tabla es la combinación (id_producto, id_pedido).
Esto evita duplicados del mismo producto dentro del mismo pedido.

Esquema de la base de datos

Para entender la relación entre tablas, se entrega un diagrama UML (mostrado en el enunciado original).
Cada tabla está conectada según las relaciones descritas arriba.

Proyecto base – vista general

El miniproyecto cuenta con una carpeta base.zip, disponible en la plataforma.
Al descomprimirla obtendrás la siguiente estructura:

base/
├── carga.py
├── consultas.py
└── data/
    ├── productos.csv
    ├── clientes.csv
    ├── pedidos.csv
    └── productos_pedidos.csv

Reglas:

Solo se deben modificar los archivos carga.py y consultas.py.

No se debe cambiar sus nombres.

Solo puedes usar las librerías ya importadas en los archivos.
El uso de librerías externas no autorizadas resultará en nota mínima (1.0).

Trabajo a realizar
1. Crear esquema

En MySQL Workbench, crear un nuevo esquema llamado:

mp2

2. Crear tablas (en carga.py)

Debes crear las tablas:

productos
clientes
pedidos
productos_pedidos


Usando sentencias CREATE TABLE.
Asegúrate de incluir correctamente las llaves primarias y foráneas según lo indicado en la sección “Set de datos”.

3. Importar los datos (en carga.py)

Desde los archivos .csv en la carpeta data, importa los registros a las tablas correspondientes.

Usa la librería csv (ya importada).

Utiliza rutas relativas, no absolutas.
Por ejemplo:

❌ Incorrecto:

open("C:/Users/.../data/productos.csv")


✅ Correcto:

open("data/productos.csv")

Se espera que:
Tabla	Filas esperadas
clientes	468
productos	15
pedidos	1964
productos_pedidos	5842
4. Realizar consultas (en consultas.py)

Usando la librería mysql.connector, realiza las siguientes consultas al esquema mp2.

a) Consulta 1

Obtener el número de pedidos realizados por el cliente con email:

jessicaflores@example.com

b) Consulta 2

Obtener el id, nombre, precio y cantidad de cada producto solicitado en el pedido con id = 2,
ordenado por id de producto en orden ascendente.

c) Consulta 3

Obtener el id, direccion, detalle y fecha de los pedidos hechos entre el 2024-01-05 y el 2024-01-07 (inclusive)
que incluyen el producto “Tablet”, ordenando los resultados por fecha descendente.

⚠️ Cada consulta debe hacerse en una sola query SQL y debe devolver solo las columnas solicitadas, en el orden indicado.

Proyecto base – carga.py

Este script se usa para los puntos 2 y 3 del trabajo.
Su objetivo es crear las tablas e importar los datos.

Solo utiliza las librerías ya importadas.
Si se usan otras librerías, se asignará nota mínima.

Proyecto base – consultas.py

Este script se usa para el punto 4.
Ya incluye código base; no se deben modificar otras partes más que las indicadas.

Solo debes modificar:

Línea 8 → contraseña de conexión MySQL

Línea 32 → completar consulta_1

Línea 41 → completar consulta_2

Línea 50 → completar consulta_3

Si todas las consultas son correctas, el output mostrado en consola coincidirá con el resultado esperado (entregado en la guía original).