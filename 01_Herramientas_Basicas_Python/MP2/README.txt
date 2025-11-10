
Usted quiere comparar dos tiendas y determinar cuál es más conveniente para comprar conjunto de productos. Para esto debe considerar que comparará solamente 2 tiendas y tendrá un contador de costos por cada una de ellas que parte en $0 y va aumentando a medida que se agregan productos y despachos o disminuye al ingresar descuentos.

Primero que todo debe identificar a las tiendas, para esto solicitará el nombre de ambas tiendas y luego utilizará las 3 primeras letras de cada una de ellas (transformándolas a mayúsculas) para identificarlas. Si estas 3 letras son iguales para ambas tiendas, debe agregar un “2” a la segunda, por ejemplo:

Ejemplo 1: Tienda “cordillera” y “volcano” se identifican como COR y VOL respectivamente.
Ejemplo 2: Tienda “marketone” y “marketplus” se identifican como MAR y MAR2 respectivamente.

El programa funciona por rondas. En cada ronda debe ingresar 3 instrucciones por cada tienda (6 en total) y al final de cada ronda imprimir el monto acumulado por cada tienda. Estas instrucciones pueden ser 3, las cuales se explican a continuación:

a) Descuento X

Se ingresa la palabra “descuento” seguida de un valor numérico X (con un espacio de separación). Se debe descontar el valor X del acumulado total de la respectiva tienda.

Ejemplo:

descuento 1000


Este input descontará $1.000 del total de la respectiva tienda.

b) Despacho X

Se ingresa la palabra “despacho” seguida de una categoría. Según la categoría se suma un monto al costo de la respectiva tienda, según la siguiente tabla:

Categoría	Costo
Cerca	1000
Normal	5000
Lejos	10000

Ejemplo:

despacho normal


Este input sumará $5.000 al total de la respectiva tienda.

c) X Z

Corresponde a dos valores numéricos separados por un espacio, el primero (X) representa la cantidad de producto y el segundo (Z) representa el precio unitario de los productos. En este caso se suma el monto resultante de la multiplicación de la cantidad de productos por su precio unitario al costo de la tienda (X*Z).
Si la cantidad de productos es mayor o igual a 10, se considera compra mayorista; por lo tanto, un producto es gratis (**(X-1)Z*).

Ejemplo cantidad menor que 10:

2 5000


Este input sumará $10.000 al total de la respectiva tienda.

Ejemplo cantidad mayor o igual que 10:

12 1000


Este input sumará $11.000 al total de la respectiva tienda, ya que una unidad es gratis por ser compra mayorista.

Finalmente, el programa terminará cuando alguna tienda supere su presupuesto de $100.000 y deberá imprimir el nombre de la tienda que es mejor o anunciar que hubo un empate.

Importante: Si se aplica un descuento y el monto total al final de cada ronda queda negativo, este debe modificarse y dejarse en $0.

Ejemplo de funcionamiento N°1

En blanco lo que imprime el programa, en amarillo el input del usuario.

Ingrese nombre tienda 1: marketone
Ingrese nombre tienda 2: marketplus
MAR: $0
MAR2: $0

Ronda 1:
Ingrese instrucciones tienda 1:
descuento 10000
despacho normal
2 15000

Ingrese instrucciones tienda 2:
descuento 2000
despacho cerca
2 20000

MAR: $25000
MAR2: $39000

Ronda 2:
Ingrese instrucciones tienda 1:
3 3000
2 5000
12 500

Ingrese instrucciones tienda 2:
3 1000
2 4000
12 400

MAR: $49500
MAR2: $54400

Ronda 3:
Ingrese instrucciones tienda 1:
despacho cerca
2 3000
2 25000

Ingrese instrucciones tienda 2:
descuento 5000
2 3000
2 20000

MAR: $106500
MAR2: $95400


marketplus es mejor.

Explicación:

Ronda 1:
Para la tienda 1 se ingresa un descuento de 10.000, despacho normal (5.000) y 2 productos de 15.000 (30.000).
Por lo tanto, la tienda 1 tiene:
−10 000 + 5 000 + 2 × 15 000 = 25 000

Para la tienda 2 se ingresa un descuento de 2.000, despacho cerca (1.000) y 2 productos de 20.000 (40.000).
Por lo tanto, la tienda 2 tiene:
−2 000 + 1 000 + 2 × 20 000 = 39 000

Ronda 2:
Para la tienda 1 se ingresan 3 productos de 3.000, 2 de 5.000 y 12 de 500. Como 12 es mayor a 10, ese producto tiene una unidad gratis quedando:
3 × 3 000 + 2 × 5 000 + (12 − 1) × 500 = 24 500

Para la tienda 2 se ingresan 3 productos de 1.000, 2 de 4.000 y 12 de 400. Como 12 es mayor a 10, ese producto tiene una unidad gratis quedando:
3 × 1 000 + 2 × 4 000 + (12 − 1) × 400 = 15 400

Luego sumando a los valores de la ronda 1:

Tienda 1: 25 000 + 24 500 = 49 500

Tienda 2: 39 000 + 15 400 = 54 400

Ronda 3:
Para la tienda 1 se ingresa un despacho cerca (1.000), 2 productos de 3.000 y 2 de 25.000:
1 000 + 2 × 3 000 + 2 × 25 000 = 57 000

Para la tienda 2 se ingresa un descuento de 5.000, 2 productos de 3.000 y 2 de 20.000:
−5 000 + 2 × 3 000 + 2 × 20 000 = 41 000

Luego sumando a los valores de la ronda 2:

Tienda 1: 49 500 + 57 000 = 106 500

Tienda 2: 54 400 + 41 000 = 95 400

Dado que la tienda 1 supera los $100.000, el programa termina e imprime el mensaje “marketplus es mejor”, porque la segunda tienda tiene mejor precio.