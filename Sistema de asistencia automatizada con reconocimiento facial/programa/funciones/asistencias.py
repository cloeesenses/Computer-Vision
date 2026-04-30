from pathlib import Path
from datetime import datetime
import csv
from deepface import DeepFace


BASE_DIR = Path(__file__).resolve().parent.parent

CARPETA_ROSTROS = BASE_DIR / "rostros_registrados"
CARPETA_CAPTURAS = BASE_DIR / "capturas_asistencias"
ARCHIVO_ASISTENCIA = BASE_DIR / "registro_asistencia.csv"

EXTENSIONES_IMAGEN = [".jpg", ".jpeg", ".png"]


# Obtiene todas las imágenes válidas de una carpeta
def obtener_imagenes(carpeta):
    imagenes = []

    for archivo in carpeta.iterdir():
        if archivo.suffix.lower() in EXTENSIONES_IMAGEN:
            imagenes.append(archivo)

    return imagenes


# Convierte el nombre del archivo en nombre de persona
def obtener_nombre_persona(ruta_imagen):
    nombre_archivo = ruta_imagen.stem
    nombre_persona = nombre_archivo.replace("_", " ")
    return nombre_persona


# Guarda la asistencia reconocida en un archivo CSV
def registrar_asistencia(nombre_persona):
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M:%S")

    archivo_existe = ARCHIVO_ASISTENCIA.exists()

    with open(ARCHIVO_ASISTENCIA, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if not archivo_existe:
            escritor.writerow(["Nombre", "Fecha", "Hora"])

        escritor.writerow([nombre_persona, fecha, hora])

    print("Registro guardado en registro_asistencia.csv")


# Compara una captura con un rostro registrado
def verificar_rostro(captura, rostro_registrado):
    resultado = DeepFace.verify(
        img1_path=str(captura),
        img2_path=str(rostro_registrado),
        enforce_detection=False
    )

    return resultado["verified"]


# Busca si una captura coincide con alguna persona registrada
def buscar_persona_registrada(captura, rostros_registrados):
    print(f"\nRevisando captura: {captura.name}")

    for rostro in rostros_registrados:
        nombre_persona = obtener_nombre_persona(rostro)

        print(f"Comparando con: {nombre_persona}")

        try:
            es_la_misma_persona = verificar_rostro(captura, rostro)

            if es_la_misma_persona:
                return nombre_persona

        except Exception as error:
            print(f"No se pudo comparar con {nombre_persona}. Error: {error}")

    return None


# Procesa todas las capturas de asistencia disponibles
def procesar_capturas(capturas_asistencia, rostros_registrados):
    for captura in capturas_asistencia:
        persona_reconocida = buscar_persona_registrada(captura, rostros_registrados)

        if persona_reconocida:
            print("\nASISTENCIA REGISTRADA")
            print(f"Persona reconocida: {persona_reconocida}")
            registrar_asistencia(persona_reconocida)
        else:
            print("\nNo se reconoció a la persona.")
            print("Asistencia no registrada.")


# Ejecuta todo el sistema de asistencia facial
def ejecutar_sistema_asistencia():
    rostros_registrados = obtener_imagenes(CARPETA_ROSTROS)
    capturas_asistencia = obtener_imagenes(CARPETA_CAPTURAS)

    print("Sistema de asistencia automatizada con reconocimiento facial")
    print("=" * 60)

    if not rostros_registrados:
        print("No hay rostros registrados.")
        return

    if not capturas_asistencia:
        print("No hay capturas de asistencia.")
        return

    procesar_capturas(capturas_asistencia, rostros_registrados)