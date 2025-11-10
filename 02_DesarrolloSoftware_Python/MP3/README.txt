Instrucciones Miniproyecto 3
Descripción

En este miniproyecto deberás construir un programa utilizando Programación Orientada a Objetos (POO) que modele el funcionamiento de un restaurante.

En el restaurante trabajan cocineros, quienes preparan platos (bebestibles y comestibles) con distintos niveles de dificultad.
Los cocineros poseen niveles de habilidad que influyen en la calidad final de cada plato.
Los platos son enviados a los clientes mediante repartidores, quienes deben entregar los pedidos dentro de un tiempo determinado.
Tanto cocineros como repartidores poseen energía, la cual disminuye con cada acción; si llega a 0, no pueden seguir trabajando.
Finalmente, los clientes reciben sus pedidos, los evalúan según la calidad recibida y esa evaluación genera una calificación final del restaurante.

Archivos entregados

La carpeta MP3.zip contiene los siguientes archivos:

main.py: archivo principal del programa para probar la simulación.

restaurante.py: contiene la definición inicial de la clase Restaurante.

platos.py: contiene las definiciones iniciales de las clases Plato, Bebestible y Comestible.

personas.py: contiene las definiciones iniciales de las clases Persona, Repartidor, Cocinero y Cliente.

Parte 1: Modelación de platos

En el archivo platos.py, se deben definir las siguientes clases:

1.1 Clase Plato
Atributos:

nombre: str, recibido como parámetro.

calidad: int, inicializado en 0.

1.2 Clase Bebestible (hereda de Plato)
Atributos adicionales:

tamano: str, elegido aleatoriamente entre "Pequeño", "Mediano" y "Grande".

dificultad: int, depende del tamaño:

Pequeño → 3

Mediano → 6

Grande → 9

calidad: int, número entero aleatorio entre 3 y 8.

1.3 Clase Comestible (hereda de Plato)
Atributos adicionales:

dificultad: int, aleatorio entre 1 y 10.

calidad: int, aleatorio entre 5 y 10.

💡 Puedes ejecutar directamente platos.py para probar si las clases están bien definidas.

Parte 2: Modelación de personas

En el archivo personas.py, se deben definir las siguientes clases:

2.1 Clase Persona
Atributo:

nombre: str, recibido como parámetro.

2.2 Clase Repartidor (hereda de Persona)
Atributos adicionales:

tiempo_entrega: int, entre 20 y 30 segundos (se recibe como parámetro).

energia: int, aleatorio entre 75 y 100.

Método:

repartir(pedido):

pedido es una lista de platos.

Reduce la energía según el factor_tamaño:

≤ 2 platos → -5 de energía

≥ 3 platos → -15 de energía

Calcula el tiempo de entrega:

𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
=
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
𝑒
𝑛
𝑡
𝑟
𝑒
𝑔
𝑎
×
𝑓
𝑎
𝑐
𝑡
𝑜
𝑟
_
𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
tiempo=tiempo_entrega×factor_velocidad

Donde:

≤ 2 platos → factor_velocidad = 1.25

≥ 3 platos → factor_velocidad = 0.85

Retorna el tiempo de demora.

2.3 Clase Cocinero (hereda de Persona)
Atributos adicionales:

habilidad: int (entre 1 y 10, recibido como parámetro).

energia: int, aleatorio entre 50 y 80.

Método:

cocinar(informacion_plato):

informacion_plato es una lista con el nombre y tipo del plato ("Bebestible" o "Comestible").

Crea una instancia del tipo de plato correspondiente.

Disminuye energía:

Bebestible → -5 (Pequeño), -8 (Mediano), -10 (Grande)

Comestible → -15

Modifica la calidad del plato según un factor_calidad:

Si dificultad > habilidad → × 0.7

Si no → × 1.5

Retorna la instancia del plato cocinado.

2.4 Clase Cliente (hereda de Persona)
Atributo adicional:

platos_preferidos: lista con entre 1 y 5 nombres de platos (recibida como parámetro).

Método:

recibir_pedido(pedido, demora):

pedido: lista de objetos Bebestible o Comestible.

demora: tiempo de entrega (int).

Comienza con una calificación de 10 puntos.

Si:

el número de platos entregados < número de preferidos, o

la demora ≥ 20,
la calificación se divide por 2.

Por cada plato:

Si calidad ≥ 11 → +1.5

Si calidad ≤ 8 → -3 (mínimo 0)

En otro caso, se mantiene igual.

Retorna la calificación final del cliente.

💡 Puedes ejecutar directamente personas.py para probar tus clases.

Parte 3: Modelación del restaurante

En el archivo restaurante.py, se define la clase Restaurante.

Atributos:

nombre: str, recibido como parámetro.

platos: dict, donde cada llave es el nombre de un plato y su valor una lista [nombre, tipo].

cocineros: lista de objetos Cocinero.

repartidores: lista de objetos Repartidor.

calificacion: int, inicializado en 0.

Método principal:
recibir_pedidos(clientes):

Recibe una lista de objetos Cliente y actualiza la calificación del restaurante siguiendo este proceso:

Por cada cliente:

Obtiene los platos preferidos.

Intenta cocinar cada plato con un cocinero disponible (energía > 0).

Si no hay cocineros disponibles, el plato no se cocina.

Los platos cocinados se agregan a la lista pedido.

Entrega del pedido:

Busca un repartidor disponible (energía > 0).

Si hay, llama a repartir(pedido) para calcular la demora.

Si no hay, se considera pedido = [] y demora = 0.

Evaluación del cliente:

Se llama a recibir_pedido(pedido, demora) y se obtiene una calificación.

Se suma a la calificación total del restaurante.

Calificación final del restaurante:

Se calcula el promedio entre todas las calificaciones de los clientes:

𝑐
𝑎
𝑙
𝑖
𝑓
𝑖
𝑐
𝑎
𝑐
𝑖
𝑜
𝑛
=
𝑠
𝑢
𝑚
𝑎
_
𝑑
𝑒
_
𝑐
𝑎
𝑙
𝑖
𝑓
𝑖
𝑐
𝑎
𝑐
𝑖
𝑜
𝑛
𝑒
𝑠
𝑐
𝑎
𝑛
𝑡
𝑖
𝑑
𝑎
𝑑
_
𝑑
𝑒
_
𝑐
𝑙
𝑖
𝑒
𝑛
𝑡
𝑒
𝑠
calificacion=
cantidad_de_clientes
suma_de_calificaciones
	​


💡 Puedes ejecutar restaurante.py para verificar que la clase esté correctamente definida.

Parte 4: Completar el código principal (main.py)

Debes completar las siguientes funciones:

crear_repartidores():
Crea 2 instancias de Repartidor y retorna la lista.

crear_cocineros():
Crea 5 instancias de Cocinero y retorna la lista.

crear_clientes():
Crea 5 instancias de Cliente con platos preferidos aleatorios y retorna la lista.

crear_restaurante():

Llama a las funciones crear_cocineros() y crear_repartidores().

Crea una instancia de Restaurante con todos los platos de la variable INFO_PLATOS.

Retorna el restaurante creado.

Archivos a entregar

Debes entregar los siguientes archivos:

main.py

platos.py

personas.py

restaurante.py

y cualquier otro archivo utilizado por tu programa.