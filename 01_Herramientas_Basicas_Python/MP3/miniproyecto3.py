#variables
ciclo=1
LstExam=list()
Exam=dict()
Pacientes=dict()
NProcedimiento=""

#abre documentos
DocPacientes = open("pacientes.csv", "r")
DocExamenes=open("disponibilidad.txt","r")

for lineas in DocExamenes:
    limpia=lineas.strip().lower()
    datos = limpia.split()
    clave = datos[0]
    valor = int(datos[1])
    Exam[clave] = valor
DocExamenes.close()

for lineas in DocPacientes:
    limpia = lineas.strip().lower()
    datos = limpia.split(',')
    nombre = datos[0]
    examenes = datos[1:]
    Pacientes[nombre] = examenes
DocPacientes.close()

#extra la primera y segunda palabra para ´primero seleccionar el menu y el segundo indica el nombre en caso de ser un paciente
def ExtraePrimeraPalabra(menu):
    CleanM = menu.lstrip().lower()
    CleanM = CleanM.split()
    tamaño = len(CleanM)
    if tamaño > 1:
        return CleanM[0], CleanM[1]
    if tamaño == 1:
        return CleanM[0], "" #las comillas son necesarias ya que al evaluar la funcion se solicitan dos datos y como en este caso no existe se manda un string vacio

#####################################################################################
# evlua si existe o no horas para el examen, recoge el nombre, lo
# lleva a una lista, lo itera, si no existe devuelve un 1 y el nombre del examen
# si existe descuenta un 1 y envia un resultado 2
#####################################################################################
def evaluaAtencion(nombre):
  nombreMin = nombre.lower()
  if nombreMin not in Pacientes:
    return 1, "paciente_no_registrado"
  lista = Pacientes[nombreMin]
  for examenes in lista:
  #evalua si no se encuentra el examen o si alguno es 0, pasa de inmediato a entregar los resultados
  #no se puede hacer el examen y envia el examen que no puede realizarse o que su valor es 0
        if examenes not in Exam or Exam[examenes] == 0:
            resultado=1
            examen=examenes
            return resultado, examen
  for examenes in lista:
        Exam[examenes] = Exam[examenes] - 1
  resultado=2
  examen=""
  return resultado, examen

#ciclo principoal
while ciclo > 0:
    print("\nDisponibilidad actual:")
    for ex in Exam:
        print(ex, ":", Exam[ex])

    Menu = input("Bienvenido, ingrese la instruccion a continuación:\n")
    Instruccion, Nombre = ExtraePrimeraPalabra(Menu)
    nombreMayus=Nombre.upper()
    if Instruccion == 'atender':
        EstadoAtencion, NProcedimiento = evaluaAtencion(Nombre)
        if EstadoAtencion == 2:
            print(f"se ha atendido a {nombreMayus} con éxito")
        elif EstadoAtencion == 1:
            if NProcedimiento == "paciente_no_registrado":
                print(f"el paciente {nombreMayus} no está registrado en el sistema")
            else:
                print(f"no es posible atender a {nombreMayus}, el examen {NProcedimiento} no está disponible")

    elif Instruccion == 'agregar':
        partes = Menu.lower().split()
        for ex in partes[1:]:
            Exam[ex] = Exam.get(ex, 0) + 1  # agrega el examen o lo inicializa en 1, truco
        print("se han agregado correctamente las instrucciones")

    elif Instruccion == 'stop':
        print("se ha presionado \"stop\", el programa se detuvo. ¡Hasta pronto!")
        break

