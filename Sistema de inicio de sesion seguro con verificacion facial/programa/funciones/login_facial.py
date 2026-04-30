from pathlib import Path
from deepface import DeepFace


BASE_DIR = Path(__file__).resolve().parent.parent

CARPETA_USUARIO_AUTORIZADO = BASE_DIR / "usuario_autorizado"
CARPETA_INTENTO_LOGIN = BASE_DIR / "intento_login"

EXTENSIONES_IMAGEN = [".jpg", ".jpeg", ".png"]


# Obtiene todas las imágenes válidas de una carpeta
def obtener_imagenes(carpeta):
    imagenes = []

    for archivo in carpeta.iterdir():
        if archivo.suffix.lower() in EXTENSIONES_IMAGEN:
            imagenes.append(archivo)

    return imagenes


# Obtiene la primera imagen encontrada en una carpeta
def obtener_primera_imagen(carpeta):
    imagenes = obtener_imagenes(carpeta)

    if imagenes:
        return imagenes[0]

    return None


# Verifica si el rostro del intento coincide con el usuario autorizado
def verificar_identidad(imagen_usuario, imagen_intento):
    resultado = DeepFace.verify(
        img1_path=str(imagen_usuario),
        img2_path=str(imagen_intento),
        enforce_detection=False
    )

    return resultado["verified"]


# Muestra el resultado del inicio de sesión
def mostrar_resultado_login(acceso_permitido):
    if acceso_permitido:
        print("\nACCESO CONCEDIDO")
        print("Bienvenido al sistema.")
    else:
        print("\nACCESO DENEGADO")
        print("Rostro no autorizado.")


# Ejecuta todo el sistema de inicio de sesión facial
def ejecutar_sistema_login():
    imagen_usuario = obtener_primera_imagen(CARPETA_USUARIO_AUTORIZADO)
    imagen_intento = obtener_primera_imagen(CARPETA_INTENTO_LOGIN)

    print("Sistema de inicio de sesión seguro con verificación facial")
    print("=" * 65)

    if imagen_usuario is None:
        print("No hay imagen de usuario autorizado.")
        return

    if imagen_intento is None:
        print("No hay imagen de intento de login.")
        return

    print(f"Usuario autorizado: {imagen_usuario.name}")
    print(f"Intento de login: {imagen_intento.name}")

    try:
        acceso_permitido = verificar_identidad(imagen_usuario, imagen_intento)
        mostrar_resultado_login(acceso_permitido)

    except Exception as error:
        print("\nOcurrió un error al verificar el rostro.")
        print(f"Error: {error}")