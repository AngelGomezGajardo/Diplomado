import requests
import pymongo
import json



client = pymongo. MongoClient("mongodb://localhost:27017/")
mydb = client['feriados']

try:
    response = requests.get("https://www.chia.cl/api/feriados/2024")
    responseJSON = json.loads(response.text)
    col = mydb['feriados2024']
    col.delete_many({})
    col.insert_many(responseJSON)
    print("registro correcto en bdd")
except:
    print("error al registrar datos")

# a. Imprimir todos los feriados que hay en la colección
print("\nTodos los feriados:")
for j, feriado in enumerate(col.find(),start=1):
    print(f"N°{j}: {feriado['nombre']}, {feriado['fecha']}")

# b. obtener solo los feriados civiles
print("\nSolo feriados civiles")
for feriado in col.find({'tipo':'Civil'}):
    print("El día de", feriado['nombre'], "es un feriado de tipo", feriado['tipo'], "y se celebra el", feriado['fecha'])

# c. obtener todos los feriados irrenunciables
print("\nTodos los Feriados Irrenunciables del 2024")
for feriado in col.find({"irrenunciable":"1"}):
    print("El día de", feriado['nombre'], "es un feriado de tipo", feriado['tipo'], "y se celebra el", feriado['fecha'])

# d. obtener solo los feriados que incluyen el texto "Santo" en el nombre
print("\nTodos los Feriados con la palabra Santo del 2024")
for feriado in col.find({'nombre':{'$regex':'Santo'}}):
    print("El día de", feriado['nombre'], "es un feriado de tipo", feriado['tipo'], "y se celebra el", feriado['fecha'])

# e. Obtener solo los feriados que se celebran entre el 11 de marzo (2024-
# 03-11) y el 31 agosto (2024-08-31)
print("\n feriados entre 11 marzo 2024 y 31 agosto 2024")
for feriado in col.find({ "fecha": { "$gte": "2024-03-11", "$lte": "2024-08-31" } }):
    print(f"el dia {feriado['fecha']}, esta dentro del rango de fechas, y se celebra el {feriado['nombre']}")



dato={
    "nombre": "Unión de los dos paisajes",
    "comentarios": "Primera vez que una expedición chilena logró unir la Cordillera de los Andes y la costa del Pacífico en un solo día ",
    "fecha":"2024-03-11",
    "irrenunciable": "0",
    "tipo":"Religioso",
    }
col.insert_one(dato)

#corroborar informacion
#numero de feriados totales
#print("\nRecueto de registros: ")
#for j, feriado in enumerate(col.find(),start=1):
#    print(f"N°{j}: {feriado['nombre']}, {feriado['fecha']}, {feriado['comentarios']}")
