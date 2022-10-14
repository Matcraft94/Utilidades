import os

import pandas as pd

# import numpy as np

import time

# Funcion que obtiene los datos
def obtener_datos(file_name):
    data = pd.read_csv(file_name, decimal=',', delimiter='#')
    tmp_colums = list(data.columns)[2:]

    columnas = ['Fecha', 'Hora'] + tmp_colums
    columnas[-1] = 'unnamed'

    data.columns = columnas

    data.drop('unnamed', axis=1, inplace=True)
    data.drop('QF', axis=1, inplace=True)

    return data

# Direccion de los archivos
files_dir = r'C:\Users\USER\Documents\Archivos'


# print(f'La direccion donde esta ubicado el archivo py es')
# print(os.getcwd())

print('Cambiamos la carpeta a la direccion de los archivos')
os.chdir(files_dir)

print(f'La direccion de la carpeta es')
print(os.getcwd())



print('\n\n\n\n')

# Obtenemos la lsita de archivos en el directorio
files_list = os.listdir()

# Seleecionamos el primer nombre del archivo excel
excel_file = list(filter(lambda x: 'xls' in x, files_list))[0]


# Quitamos los archivos
files_list= [archivo for archivo in files_list if not any('xlsx' in archivo for xls in files_list)]

# Creamos una lsita vacia para guardar los nombres de los archivos que no se pueden guardar
files_no_copy = []


with pd.ExcelWriter(excel_file, mode='a') as escritor:
    for file_name in files_list:
        # Se guarda el archivo en la respectiva hoja
        try:
            print(f'\nCopiando lel archivo {file_name}')
            data_tmp = obtener_datos(file_name)
            data_tmp.to_excel(escritor, sheet_name=file_name, index=False)
            print(f'Copiado lel archivo {file_name}\n')

        # SI no se peude se cambia el nombre por minusculas
        except:
            print(f'La hoja {file_name} ya exsite, no se procede a copiarla')
            files_no_copy.append(file_name)

            print(f'\nCopiando el archivo {file_name} como {file_name.lower()}')
            data_tmp = obtener_datos(file_name)
            data_tmp.to_excel(escritor, sheet_name=file_name.lower(), index=False)
            print(f'Copiado el archivo {file_name} como {file_name.lower()}\n')


print(f'\nLos archivos que se copiaron con minusculas son:')
print(list(map(lambda x: x.lower(), files_no_copy)))

