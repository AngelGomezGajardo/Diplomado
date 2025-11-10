# variables de despacho
Cerca = 1000
Normal = 5000
Lejos = 10000
#########################################################################
#extrae las 3 primeras letras del nombre de la tienda y los convierte en mayusculas
def NombreTiendas(var1):
    X = var1.upper()
    PtresLetras = X[0:3]
    return PtresLetras
#########################################################################
#comparamos lo snombres de las tiendas y si son iguales devuelve la segunda con un 2
def compara(x, y):
    if x == y:
        y = y + "2"
    return y
#########################################################################
#calculamos el total por tienda ingresada en la instruccion
def CalcXtienda(dcto, dspcho, ctdd, prc):
    descuento=int(dcto)
    despacho=int(dspcho)
    cantidad=int(ctdd)
    precio=int(prc)
    if cantidad >= 10:
        total = -descuento + despacho + ((cantidad - 1) * precio)
    else:
        total = -descuento + despacho + (cantidad * precio)
    return total
#########################################################################
#separa las instrucciones que se ingresan, segun el tipo de contenido y la guarda en una lista
def separa(instr):

    descuento=0
    despacho=0
    unidades=0
    precio=0

    _convierte = instr.lower()
    _separa=_convierte.split()
    #print(_separa[0])
    if (_separa[0])=="descuento":
        descuento=_separa[1]
        #print("descuento",descuento)
    elif (_separa[0])=="despacho":
        if _separa[1]=="cerca":
            despacho = Cerca
            #print("despacho", Cerca)
        if _separa[1]=="normal":
            despacho = Normal
            #print("despacho", Normal)
        if _separa[1]=="lejos":
            despacho = Lejos
            #print("despacho", Lejos)
    else:
        unidades=_separa[0]
        precio=_separa[1]

    return descuento,despacho, unidades, precio

#########################################################################

TotalT=[0,0]
TotalT[0]=0
TotalT[1]=0


NombreT1=input("ingrese el nombre de la tienda 1: ")
NombreT2=input("ingrese el nombre de la tienda 2: ")
nt1=NombreTiendas(NombreT1)
nt2=NombreTiendas(NombreT2)

nt22=compara(nt1,nt2)
nombres=(nt1,nt22)

T1="$"+str(TotalT[0])
T2="$"+str(TotalT[1])
print(nt1,T1)
print(nt22,T2)

while TotalT[0]<=100000 or TotalT[1]<=100000:
    p=("1","2")
    for i in p:
        Ntienda=i
        print("ingrese instrucciones para tienda", Ntienda)
        #######################################
        inst1 = input("")
        desc, desp, unid, pre=separa(inst1)
        costoT1=CalcXtienda(desc, desp, unid, pre)
        #######################################
        inst2 = input("")
        desc, desp, unid, pre=separa(inst2)
        costoT2=CalcXtienda(desc, desp, unid, pre)
        #######################################
        inst3 = input("")
        desc, desp, unid, pre=separa(inst3)
        costoT3=CalcXtienda(desc, desp, unid, pre)

        #######################################
        totalC=costoT1+costoT2+costoT3
        if totalC < 0:
            totalC = 0

        j=int(i)-1
        print(nombres[j],totalC)
        TotalT[j]=TotalT[j]+totalC

    if TotalT[0] > 100000 or TotalT[1] > 100000:
        break
    else:
        i=1

RF1="$"+str(TotalT[0])
RF2="$"+str(TotalT[1])
print(nombres[0]+":",RF1)
print(nombres[1]+":",RF2)

if TotalT[0] > 100000 and TotalT[1] > 100000:
    print("Empate")
elif TotalT[0] > 100000:
    print(NombreT2, "es mejor.")
else:
    print(NombreT1, "es mejor.")
