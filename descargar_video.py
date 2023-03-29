## Creado por Lucy
## 28-03-2023

# pyinstaller --onefile descargar_video.py

import os
from pytube import YouTube
from tqdm import tqdm


def progress_bar(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    progress = (current / stream.filesize) * 100
    print(f"Progreso: {progress:.2f}%")

# def descargar_video(url, ruta_de_guardado):
#     try:
#         # Crear objeto YouTube con la URL
#         yt = YouTube(url)

#         # Obtener la mejor calidad de video disponible
#         video = yt.streams.get_highest_resolution()

#         # Crear una nueva barra de progreso para este video
#         with tqdm(total=100, ncols=100, unit='%', desc=f"Descargando {yt.title}", bar_format='{l_bar}{bar}') as bar:
#             yt.register_on_progress_callback(progress_bar)

#             # Descargar el video
#             print(f"Descargando: {yt.title}")
#             video.download(ruta_de_guardado)
#             print(f"Video descargado en: {ruta_de_guardado}/{yt.title}")

#     except Exception as e:
#         print(f"Error al descargar el video: {e}")

def descargar_video(url, ruta_personalizada=None):
    try:
        # Crear objeto YouTube con la URL
        yt = YouTube(url)

        # Obtener la mejor calidad de video disponible
        video = yt.streams.get_highest_resolution()

        # Determinar la ruta de la carpeta donde se guardará el video
        if ruta_personalizada is not None:
            ruta_de_guardado = ruta_personalizada
        else:
            ruta_de_guardado = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Crear una nueva barra de progreso para este video
        with tqdm(total=100, ncols=100, unit='%', desc=f"Descargando {yt.title}", bar_format='{l_bar}{bar}') as bar:
            yt.register_on_progress_callback(progress_bar)

            # Descargar el video
            print(f"Descargando: {yt.title}")
            video.download(ruta_de_guardado)
            print(f"Video descargado en: {ruta_de_guardado}/{yt.title}")

    except Exception as e:
        print(f"Error al descargar el video: {e}")


# if __name__ == "__main__":
#     print('Este programita fue creado por Lucy, espero loe encuentres utilidad :3')
#     url_del_video = input("Por favor, ingrese el enlace del video de YouTube que desea descargar: ")

#     # Obtener la ruta donde se encuentra el programa
#     ruta_de_guardado = os.path.dirname(os.path.abspath(__file__))

#     descargar_video(url_del_video, ruta_de_guardado)

if __name__ == "__main__":
    print('Este programita fue creado por Lucy, espero loe encuentres utilidad :3')
    url_del_video = input("Por favor, ingrese el enlace del video de YouTube que desea descargar: ")
    
    ruta_personalizada = input("Ingrese la ruta donde desea guardar el archivo (deje vacío para utilizar la carpeta de descargas del sistema): ")
    if ruta_personalizada == "":
        ruta_personalizada = None

    # Obtener la ruta donde se encuentra el programa
    ruta_de_guardado = os.path.dirname(os.path.abspath(__file__))

    descargar_video(url_del_video, ruta_personalizada)
