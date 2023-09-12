import requests
url="https://api.wallapop.com/api/v3/cars/search?keywords=coches&category_ids=100&filters_source=search_box&longitude=-3.69196&latitude=40.41956"
user_agent = {'User-agent': 'Mozilla/5.0'}
r = requests.get(url=url, headers=user_agent).json()
auto=r['keywords']
busqueda=r['search_objects']
#id=r['id']
#print(id, " ", auto)
lista=[]
for x in busqueda:
    lista.append(x['content'])

lista2=[]
for x in lista:
    lista2.append(x['title'])
print(lista2)

