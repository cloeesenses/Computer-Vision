import json
import shutil
from pathlib import Path

from funciones.config import EXTENSIONES_IMAGEN


# Lee información desde un archivo JSON
def leer_json(ruta_archivo):
    if not ruta_archivo.exists():
        return {}

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# Guarda información en un archivo JSON
def guardar_json(ruta_archivo, datos):
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# Crea un identificador limpio a partir del nombre del usuario
def crear_id_usuario(nombre):
    nombre_limpio = nombre.strip().lower()
    nombre_limpio = nombre_limpio.replace(" ", "_")
    return nombre_limpio


# Verifica que el archivo sea una imagen válida
def es_imagen_valida(ruta_imagen):
    ruta = Path(ruta_imagen)
    return ruta.suffix.lower() in EXTENSIONES_IMAGEN


# Copia la foto del usuario a la carpeta de rostros
def copiar_foto_usuario(ruta_origen, carpeta_destino, id_usuario):
    ruta_origen = Path(ruta_origen)

    if not ruta_origen.exists():
        raise FileNotFoundError("La imagen del rostro no existe.")

    if not es_imagen_valida(ruta_origen):
        raise ValueError("El archivo no tiene una extensión de imagen válida.")

    extension = ruta_origen.suffix.lower()
    ruta_destino = carpeta_destino / f"{id_usuario}{extension}"

    shutil.copy(ruta_origen, ruta_destino)

    return ruta_destino