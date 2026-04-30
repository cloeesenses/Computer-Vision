from pathlib import Path


# Contraseña para permitir registrar nuevos perfiles
CONTRASENA_ADMIN = "1234"


# Ruta base de la carpeta programa
BASE_DIR = Path(__file__).resolve().parent.parent


# Carpetas principales del proyecto
CARPETA_DATOS = BASE_DIR / "datos"
CARPETA_ROSTROS = BASE_DIR / "rostros_usuarios"
CARPETA_CANCIONES = BASE_DIR / "canciones_usuarios"
CARPETA_FACE_ID = BASE_DIR / "face_id"


# Archivo donde se guardan los perfiles registrados
ARCHIVO_PERFILES = CARPETA_DATOS / "perfiles.json"


# Extensiones permitidas para imágenes de rostros
EXTENSIONES_IMAGEN = [".jpg", ".jpeg", ".png"]