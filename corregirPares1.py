import csv

def leer_camion(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            header=next(rows)
            camion=[]
            for row in rows:
                item={}
                item['nombre']=row[0]
                item['cajones']=int(row[1])
                item['precio']=float(row[2])
                camion.append(item)
            return camion
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')
#%%
def leer_precios(nombre_archivo):
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            precios={}
            for row in rows:
                try:
                    precios[row[0]] = float(row[1])
                except IndexError:
                    pass
            return precios
    except:
        print(f'Warning: {nombre_archivo} no es una ruta válida')

#%%

camion = leer_camion('Data/camion.csv') #cuidado, para que funcione hay que ejecutarlo desde ejercicios_python
precios= leer_precios('Data/precios.csv')

# para imprimir los resultados:
# from pprint import pprint
# pprint(camion)
# pprint(precios)

# calculo del costo para versión anterior, con camion como lista de tuplas:
# costo=0
# for nombre, cajones, precio in camion:
#     costo+=cajones*precio
# print(costo)

valorCamion=0.0
for s in camion:
        valorCamion+= s['cajones']*s['precio']

valorVenta=0.0
for s in camion:
    if s['nombre'] in precios:
        valorVenta+=precios[s['nombre']]*s['cajones']
    else:
        print('no está en la lista de precios')

diferencia=valorVenta-valorCamion

print(f'El camión costó {valorCamion}, con la venta se recaudó {valorVenta} y la diferencia fue de {diferencia:.2f}.')
if diferencia>0:
    print('Hubo ganancia.')
elif diferencia==0:
    print('El balance es cero.')
else:
    print('Hubo pérdida.')
