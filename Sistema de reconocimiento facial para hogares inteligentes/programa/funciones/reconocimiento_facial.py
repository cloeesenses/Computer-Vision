from deepface import DeepFace

from funciones.config import (
    BASE_DIR,
    ARCHIVO_PERFILES,
    CARPETA_FACE_ID,
    EXTENSIONES_IMAGEN
)

from funciones.archivos import leer_json


# Obtiene la imagen que simula la cámara dentro de face_id
def obtener_imagen_face_id():
    if not CARPETA_FACE_ID.exists():
        print("No existe la carpeta face_id.")
        return None

    for archivo in sorted(CARPETA_FACE_ID.iterdir()):
        if archivo.suffix.lower() in EXTENSIONES_IMAGEN:
            return archivo

    print("No hay ninguna imagen en la carpeta face_id.")
    return None


# Verifica si dos imágenes pertenecen a la misma persona
def verificar_rostro(imagen_entrada, imagen_registrada):
    resultado = DeepFace.verify(
        img1_path=str(imagen_entrada),
        img2_path=str(imagen_registrada),
        enforce_detection=False
    )

    return resultado["verified"]


# Busca qué perfil registrado coincide con la imagen de face_id
def identificar_usuario_por_rostro():
    perfiles = leer_json(ARCHIVO_PERFILES)
    imagen_face_id = obtener_imagen_face_id()

    if imagen_face_id is None:
        return None

    if not perfiles:
        print("No hay perfiles registrados.")
        return None

    print(f"Imagen detectada por face_id: {imagen_face_id.name}")

    for id_usuario, perfil in perfiles.items():
        ruta_rostro_registrado = BASE_DIR / perfil["foto"]

        print(f"Comparando con: {perfil['nombre']}")

        try:
            rostro_coincide = verificar_rostro(
                imagen_entrada=imagen_face_id,
                imagen_registrada=ruta_rostro_registrado
            )

            if rostro_coincide:
                return id_usuario

        except Exception as error:
            print(f"No se pudo comparar con {perfil['nombre']}. Error: {error}")

    return None