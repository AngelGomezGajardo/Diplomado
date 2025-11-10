import random

Name=input("Ingresa tu Nombre: ")
N_Random=random.randint(1,100)
numero=1
intentos=0
Resultado=0

while numero!=0:
    numero = int(input("ingresa el numero que crees que es, (cero para terminar)"))
    Resultado = (N_Random - numero)
    intentos = intentos + 1
    if Resultado<0:
        Resultado=Resultado*-1
    elif numero==0:
        print("process finished with exit code 0")
        break
    elif N_Random==numero:
        print("Felicitaciones ", Name,", lo lograste en ", intentos,"intentos")
        break
    elif (Resultado<=5):
        print("estas a 5 o menos de 5 unidades")
    elif (Resultado>5 and Resultado<=10):
        print("estas a mas de 5 y menos de 10 unidades")
    elif (Resultado>10 and Resultado<=20):
        print("estas a mas de 10 pero menos que 20 unidades")
    elif (Resultado>20):
        print("estas a mas de 20 unidades")
    elif (numero == 0):
        print("No lo lograste a pesar de tratar ",intentos, "veces. Mas suerte para otra vez, el numero era: ", N_Random)
    elif intentos>=20:
        print("No lo lograste a pesar de tratar",intentos," N veces. Mas suerte para otra vez")
        break
