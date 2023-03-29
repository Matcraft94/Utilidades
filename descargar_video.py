# # ## Creado por Lucy
# # ## 28-03-2023

# # pyinstaller --onefile descargar_video.py

import os
from pytube import YouTube
from tqdm import tqdm
from time import time

def progress_bar(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    progress = (current / stream.filesize) * 100
    speed = (current / (time() - progress_bar.start_time)) / 1000 / 1000
    time_elapsed = time() - progress_bar.start_time
    time_left = bytes_remaining / (speed * 1000 * 1000)
    print(f"Progreso: {progress:.2f}% / Velocidad: {speed:.2f} MB/s / Tiempo transcurrido: {time_elapsed:.0f}s / Tiempo restante: {time_left:.0f}s")

def descargar_video(url, ruta_personalizada=None):
    try:
        # Crear objeto YouTube con la URL
        yt = YouTube(url)

        # Obtener la lista de calidades disponibles
        disponibles = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        # Mostrar la resolución predeterminada
        video = disponibles.first()
        print(f"Descargando video a {video.resolution}p")

        # Mostrar un menú de opciones para seleccionar la calidad de descarga
        print("\nSeleccione una calidad de descarga:\n")
        for i, stream in enumerate(disponibles):
            print(f"{i+1}. {stream.resolution}p")

        seleccion = int(input("\nOpción: "))
        video = disponibles[seleccion - 1]

        # Determinar la ruta de la carpeta donde se guardará el video
        if ruta_personalizada is not None:
            ruta_de_guardado = ruta_personalizada
        else:
            ruta_de_guardado = os.path.join(os.path.expanduser('~'), 'Downloads')

            # Verificar si la carpeta "Downloads" existe, de lo contrario utilizar la carpeta "Descargas"
            if not os.path.isdir(ruta_de_guardado):
                ruta_de_guardado = os.path.join(os.path.expanduser('~'), 'Descargas')

        # Crear una nueva barra de progreso para este video
        progress_bar.start_time = time()
        with tqdm(total=100, ncols=100, unit='%', desc=f"\nDescargando {yt.title}", bar_format='{l_bar}{bar}') as bar:
            yt.register_on_progress_callback(progress_bar)

            # Descargar el video
            print(f"Descargando: {yt.title}\n\n")
            video.download(ruta_de_guardado)
            print(f"\n\nVideo descargado en: {ruta_de_guardado}/{yt.title}")

    except Exception as e:
        print(f"Error al descargar el video: {e}")

if __name__ == "__main__":
    print('Este programita fue creado por Lucy, espero lo encuentres útil :3')
    url_del_video = input("Por favor, ingrese el enlace del video de YouTube que desea descargar: ")
    
    ruta_personalizada = input("Ingrese la ruta donde desea guardar el archivo (deje vacío para utilizar la carpeta de descargas del sistema): ")
    if ruta_personalizada == "":
        ruta_personalizada = None

    # Obtener la ruta donde se encuentra el programa
    ruta_de_guardado = os.path.dirname(os.path.abspath(__file__))

    descargar_video(url_del_video, ruta_personalizada)