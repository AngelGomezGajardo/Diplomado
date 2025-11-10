MiniProyecto 3

Usted quiere administrar un laboratorio médico y para ello cuenta con un archivo que indica la disponibilidad de horas para un listado de exámenes descrito en el archivo disponibilidad.txt.
Este archivo puede tener tantos tipos de exámenes como se estime conveniente y una cantidad n de horas para cada tipo de examen.

Deberá cargar esta disponibilidad en formato de diccionarios dentro de su programa, considerando el nombre del examen como llave y la cantidad de horas disponibles como valor (entero).
A continuación, se muestran ejemplos de las posibles combinaciones que se podrían tener:

Ejemplo 1 de archivo disponibilidad.txt:
tac 2
hemograma_completo 7
urianalisis 5
perfil_lipidico 2
perfil_renal 3
pcr 19
perfil_hepatico 3

Ejemplo 2 de archivo disponibilidad.txt:
resonancia_magnetica 1
glucosa 5
pcr 12
hormonas_tiroideas 3


Además, usted tiene un archivo pacientes.csv que contiene, en cada fila, el nombre del paciente y a continuación cada uno de los exámenes que debe realizarse.
Deberá guardar los pacientes en un diccionario, usando como llave el nombre del paciente y como valores una lista con los exámenes que requiere dicho paciente.

Usted debe verificar antes de atender al paciente que posee disponibilidad para hacer todos los exámenes que requiere.
Si esto se cumple, procede a atenderlo descontando una unidad de los exámenes que requiere dicho paciente de la disponibilidad del laboratorio (solo dentro del programa, no en el archivo).

Ejemplo 1 de archivo pacientes.csv (asociado al Ejemplo 1 de disponibilidad.txt):
Fernando,perfil_lipidico,tac,pcr,perfil_renal
Javier,urianalisis,pcr,perfil_hepatico,tac
Amanda,tac,pcr,urianalisis
Valentina,pcr,perfil_lipidico

Ejemplo 2 de archivo pacientes.csv (asociado al Ejemplo 2 de disponibilidad.txt):
Juan,glucosa,pcr
Montserrat,pcr,hormonas_tiroideas,resonancia_magnetica
Eduardo,resonancia_magnetica,glucosa

Interacción con el programa

El programa debe aceptar tres tipos de instrucciones:

1. ATENDER X

Atiende al paciente X si es posible.
Debe verificarse que existe al menos una hora disponible para cada examen que requiere el paciente.
Si todos los exámenes tienen disponibilidad, se debe descontar una unidad de cada examen correspondiente.

Ejemplos de instrucción:

ATENDER Fernando
ATENDER Montserrat

2. AGREGAR examen_1 examen_2 examen_n

Permite agregar disponibilidad horaria de uno o más exámenes.
Se pueden agregar varios exámenes separados por espacio.
Si un examen aparece más de una vez en la instrucción, su disponibilidad aumentará tantas veces como aparezca.

Ejemplos de instrucción:

AGREGAR urianalisis pcr tac perfil_hepatico
AGREGAR resonancia_magnetica resonancia_magnetica resonancia_magnetica pcr pcr
AGREGAR glucosa

3. STOP

Detiene la ejecución del programa.

Comportamiento esperado

Al iniciar el programa y luego de cada instrucción, se deben imprimir las disponibilidades de cada examen.
También deben mostrarse mensajes indicando si el paciente fue atendido con éxito o si no pudo ser atendido, mostrando en ese caso el primer examen sin disponibilidad.

Ejemplo de ejecución:
TAC: 2
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 5
PERFIL_LIPIDICO: 2
PERFIL_RENAL: 3
PCR: 19
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: atender fernando
Se ha atendido con éxito a FERNANDO!

TAC: 1
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 5
PERFIL_LIPIDICO: 1
PERFIL_RENAL: 2
PCR: 18
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: atender amanda
Se ha atendido con éxito a AMANDA!

TAC: 0
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 4
PERFIL_LIPIDICO: 1
PERFIL_RENAL: 2
PCR: 17
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: atender valentina
Se ha atendido con éxito a VALENTINA!

TAC: 0
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 4
PERFIL_LIPIDICO: 0
PERFIL_RENAL: 2
PCR: 16
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: atender javier
No es posible atender a JAVIER porque no existen horas disponibles para el examen TAC.

TAC: 0
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 4
PERFIL_LIPIDICO: 0
PERFIL_RENAL: 2
PCR: 16
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: agregar tac tac pcr tac
TAC: 3
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 4
PERFIL_LIPIDICO: 0
PERFIL_RENAL: 2
PCR: 17
PERFIL_HEPATICO: 3

Bienvenido, ingrese la instrucción a continuación: atender javier
Se ha atendido con éxito a JAVIER!

TAC: 2
HEMOGRAMA_COMPLETO: 7
URIANALISIS: 3
PERFIL_LIPIDICO: 0
PERFIL_RENAL: 2
PCR: 16
PERFIL_HEPATICO: 2

Bienvenido, ingrese la instrucción a continuación: stop