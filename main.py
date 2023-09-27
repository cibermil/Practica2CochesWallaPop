#La siguiente rutina nos permite conectarnos la base de datos mongo, extraer datos de algunos vehículos del portar wallapop mediante una api

import requests
from mongodb import client
import datetime

url="https://api.wallapop.com/api/v3/cars/search?keywords=coches&category_ids=100&filters_source=search_box&longitude=-3.69196&latitude=40.41956"
user_agent = {'User-agent': 'Mozilla/5.0'}
r = requests.get(url=url, headers=user_agent).json() #Contiene el resultado de la búsqueda, mediante la api

auto=r['keywords'] #El contenido del vehículo contenido en el diccionario las keys keywords
busqueda=r['search_objects'] #Ahora extraemos lo que contiene la búsqueda
lista=[]
for x in busqueda:
    lista.append(x['content']) #En la lista guardamos la key de contenido

#print(lista)
lista2=[]
for x in lista: #Por último extraemos los datos relevantes del vehículo
    lista2.append(x['title'])


print(lista2)
datos_vehiculo={
        "modelo_vehiculo": x['title'],
        "precio": str(['price']) + x['currency'],
        "año":x['year'],
        "transmision":x['gearbox'],
        "motor":x['horsepower'],
        "recorrido":x['km'],
        "ubicacion":x['location']
}

#Lo guardamos en la base de datos
#_ = client.get_database('tratamientodatos').get_collection('trabajo_final').insert_one(document=datos_vehiculo)
