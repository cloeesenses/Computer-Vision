from pathlib import Path
from yt_dlp import YoutubeDL

from funciones.config import CARPETA_CANCIONES


# Descarga una canción de YouTube y la guarda como MP3
def descargar_cancion_youtube(link, nombre_archivo):
    CARPETA_CANCIONES.mkdir(exist_ok=True)

    nombre_sin_extension = Path(nombre_archivo).stem
    ruta_salida = CARPETA_CANCIONES / nombre_sin_extension

    opciones = {
        "format": "bestaudio/best",
        "outtmpl": str(ruta_salida) + ".%(ext)s",
        "noplaylist": True,
        "quiet": False,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with YoutubeDL(opciones) as ydl:
        ydl.download([link])

    ruta_mp3 = CARPETA_CANCIONES / f"{nombre_sin_extension}.mp3"
    return ruta_mp3