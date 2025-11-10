MiniProyecto 1

El objetivo de este proyecto es que puedas poner en práctica lo aprendido sobre control de flujo, manejo de strings y recepción de input.

Instrucciones para realizar la actividad

Este proyecto consiste en escribir un programa que implemente un juego de adivinar el número contra el computador.
Los detalles son los siguientes:

El programa debe generar un número entero entre 1 y 100 en forma aleatoria y guardarlo.

El programa solicita el nombre del jugador y lo guarda.

El jugador ingresa un número que representa un intento de adivinar el número.
Si el jugador ingresa el número cero (0), el juego termina inmediatamente imprimiendo el siguiente mensaje:

“No lo lograste a pesar de tratar N veces. Más suerte para otra vez.”

El programa lee el número ingresado y genera una de las siguientes respuestas:

Sorry <nombre>, ese no es pero estás a una distancia menor a 5.

Sorry <nombre>, ese no es pero estás a una distancia mayor que 5 y menor que 10.

Sorry <nombre>, ese no es pero estás a una distancia mayor que 10 y menor que 20.

Sorry <nombre>, ese no es pero estás a una distancia mayor que 20.

Felicitaciones <nombre>, lo lograste en N intentos.

En cualquiera de los primeros cuatro casos, el programa debe volver a pedir un nuevo intento de adivinar.

Debes mantener el registro de los intentos para poder mostrarlo correctamente cuando el juego termine.

💡 Recuerda que puedes generar el número aleatorio con la función
randint(desde, hasta) de la librería random, la cual debes importar al inicio del programa.

Ejemplo de uso
Ejemplo 1
Ingresa tu nombre: Jaime
Ingresa el número que crees que es (0 para parar): 50
Sorry Jaime ese no es pero estás a más de 20 de distancia

Ingresa el número que crees que es (0 para parar): 75
Sorry Jaime ese no es pero estás a una distancia mayor que 10 pero menor que 20

Ingresa el número que crees que es (0 para parar): 80
Sorry Jaime ese no es pero estás a una distancia mayor que 5 pero menor que 10

Ingresa el número que crees que es (0 para parar): 85
Felicitaciones Jaime lo lograste en 3 intentos


Process finished with exit code 0

Ejemplo 2
Ingresa tu nombre: Sergio
Ingresa el número que crees que es (0 para parar): 60
Sorry Sergio ese no es pero estás a más de 20 de distancia

Ingresa el número que crees que es (0 para parar): 40
Sorry Sergio ese no es pero estás a más de 20 de distancia

Ingresa el número que crees que es (0 para parar): 0
No lo lograste Sergio a pesar de tratar 2 veces. Más suerte para otra vez


Process finished with exit code 0