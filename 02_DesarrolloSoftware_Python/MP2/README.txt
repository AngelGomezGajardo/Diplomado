Instrucciones Miniproyecto 2
Descripción

En este miniproyecto deberás construir una simulación del funcionamiento de vehículos utilizando Programación Orientada a Objetos (POO).

Archivos entregados

Se entrega una carpeta MP2.zip que contiene los siguientes archivos:

main.py: archivo principal donde deberás completar el código solicitado.
Es el único archivo que debes modificar.

parametros.py: archivo que contiene valores estáticos a utilizar dentro del código.

Código entregado

El archivo main.py ya incluye implementada la clase Rueda, la cual no debes modificar.
A continuación se describen sus atributos y métodos:

Atributos:

resistencia_actual: resistencia actual de la rueda, inicializada con un valor entero aleatorio tomado de la lista RESISTENCIA del archivo parametros.py.

resistencia_total: resistencia total de la rueda, igual al valor inicial de resistencia_actual.

estado: estado actual de la rueda (string), inicializado como "Perfecto".

Métodos:

gastar(acción, tipo): recibe una acción ("acelerar" o "frenar") y un tipo ("automovil" o "moto").
Disminuye el valor de resistencia_actual dependiendo de los parámetros.
No retorna nada.

actualizar_estado(): actualiza el estado de la rueda según su nivel de desgaste en comparación con su resistencia total.
No retorna nada.

Trabajo a realizar

Deberás implementar el resto del programa en main.py, utilizando POO.
El trabajo se divide en tres partes.

Parte 1: Definición de funciones y clases

Antes de crear tus clases, debes definir la función auxiliar:

1. Función avanzar(velocidad, tiempo)

Recibe:

velocidad (float): velocidad del vehículo en m/s.

tiempo (int): tiempo en segundos.

Debe retornar la cantidad de kilómetros recorridos durante ese tiempo, según la fórmula:

𝑘
𝑖
𝑙
𝑜
𝑚
𝑒
𝑡
𝑟
𝑎
𝑗
𝑒
=
𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
(
𝑚
/
𝑠
)
×
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
(
𝑠
)
1000
kilometraje=
1000
velocidad(m/s)×tiempo(s)
	​

2. Clase Automóvil
Atributos:

kilometraje: kilometraje actual del vehículo (km), se recibe como parámetro.

ano: año de fabricación (int), se recibe como parámetro.

ruedas: lista de 4 objetos de clase Rueda.

aceleracion: aceleración actual (km/h²), inicializada en 0.

velocidad: velocidad actual (km/h), inicializada en 0.

Métodos:

avanzar(tiempo):

Incrementa el kilometraje según la función avanzar().

Convierte la velocidad de km/h a m/s dividiéndola por 3.6 antes de usarla.

𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
_
𝑚
𝑠
=
𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
_
𝑘
𝑚
ℎ
/
3.6
velocidad_ms=velocidad_kmh/3.6

acelerar(tiempo):

Convierte tiempo de segundos a horas.

Aumenta la aceleración según:

𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
+
=
(
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
0.5
)
aceleracion+=(tiempo_horas∗0.5)

Actualiza la velocidad:

𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
+
=
𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
∗
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
velocidad+=aceleracion∗tiempo_horas

Llama a avanzar(tiempo) y al método gastar("acelerar", "automovil") en cada rueda.

Finalmente, reinicia la aceleración a 0.

frenar(tiempo):

Convierte tiempo a horas.

Resta aceleración:

𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
−
=
(
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
0.5
)
aceleracion−=(tiempo_horas∗0.5)

Actualiza la velocidad:

𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
+
=
𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
∗
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
velocidad+=aceleracion∗tiempo_horas

Si la velocidad queda negativa, se ajusta a 0.

Llama a avanzar(tiempo) y a gastar("frenar", "automovil") en cada rueda.

Reinicia aceleración a 0.

obtener_kilometraje(): retorna el kilometraje actual.

reemplazar_rueda():

Busca la rueda con menor resistencia, la elimina y agrega una nueva instancia de Rueda.

Si hay empate, se reemplaza cualquiera de las ruedas con resistencia mínima.

3. Clase Moto

Hereda la estructura general de Automovil, con las siguientes diferencias:

Atributos adicionales:

cilindrada: parámetro adicional (int ≥ 0).

ruedas: lista de 2 objetos Rueda en lugar de 4.

Métodos:

avanzar(tiempo): igual que en automóvil, usando la conversión de velocidad a m/s.

acelerar(tiempo):

𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
+
=
(
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
0.8
)
+
(
𝑐
𝑖
𝑙
𝑖
𝑛
𝑑
𝑟
𝑎
𝑑
𝑎
∗
0.2
)
aceleracion+=(tiempo_horas∗0.8)+(cilindrada∗0.2)
𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
+
=
𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
∗
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
3
velocidad+=aceleracion∗tiempo_horas∗3

Luego ejecuta avanzar(tiempo) y gastar("acelerar", "moto") en cada rueda.
Reinicia aceleración a 0.

frenar(tiempo):

𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
−
=
(
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
0.8
)
+
(
𝑐
𝑖
𝑙
𝑖
𝑛
𝑑
𝑟
𝑎
𝑑
𝑎
∗
0.2
)
aceleracion−=(tiempo_horas∗0.8)+(cilindrada∗0.2)
𝑣
𝑒
𝑙
𝑜
𝑐
𝑖
𝑑
𝑎
𝑑
+
=
𝑎
𝑐
𝑒
𝑙
𝑒
𝑟
𝑎
𝑐
𝑖
𝑜
𝑛
∗
𝑡
𝑖
𝑒
𝑚
𝑝
𝑜
_
ℎ
𝑜
𝑟
𝑎
𝑠
∗
2
velocidad+=aceleracion∗tiempo_horas∗2

Luego ejecuta avanzar(tiempo) y gastar("frenar", "moto") en cada rueda.
Reinicia aceleración a 0.

obtener_kilometraje(): retorna el kilometraje actual.

reemplazar_rueda():
Elimina todas las ruedas cuya resistencia_actual < resistencia_total * 0.5, y por cada una crea una nueva instancia de Rueda.

Parte 2: Completar acciones

Debes completar la función:

accion(vehiculo, opcion)


Esta función recibe una instancia de un vehículo y un entero con la acción a realizar.

Acciones disponibles:

2 – Acelerar:

Solicita al usuario el tiempo en segundos.

Ejecuta vehiculo.acelerar(tiempo).

Imprime:

Se ha acelerado por X segundos, llegando a una velocidad de Y km/h


3 – Frenar:

Solicita tiempo en segundos.

Ejecuta vehiculo.frenar(tiempo).

Imprime:

Se ha frenado por X segundos, llegando a una velocidad de Y km/h


4 – Avanzar:

Solicita tiempo en segundos.

Ejecuta vehiculo.avanzar(tiempo).

Imprime:

Se ha avanzado por X segundos a una velocidad de Y km/h


5 – Cambiar rueda:

Ejecuta vehiculo.reemplazar_rueda().

Imprime:

Se han reemplazado las ruedas con éxito


6 – Mostrar estado:
Imprime:

Año: XXXX
Velocidad: YY km/h
Kilometraje: ZZ km
Estado de las ruedas:
Perfecto
Usada
Usada
Gastada

Parte 3: Completar código principal

En el main.py deberás instanciar:

Un objeto de clase Moto

Un objeto de clase Automóvil

Luego, agrégalos a la lista de vehículos existente (que comienza vacía).
Los valores iniciales son definidos libremente por ti, pero deben respetar los tipos y restricciones establecidas.

Archivos a entregar

main.py: código completo y funcional.

parametros.py: con los valores de parámetros utilizados.

Consideraciones generales

La corrección se hará ejecutando el programa e interactuando con el menú.

Solo puedes usar contenidos vistos hasta la semana 4.

Prohibido el uso de herramientas de generación de código.

Si usas material externo, debes citarlo en el código.
De lo contrario, la calificación será 1.0.

Un archivo que no cumpla con el formato o no pueda ejecutarse obtendrá nota mínima.

Este ejercicio tiene un propósito formativo sobre POO, no busca simular vehículos reales con precisión física.