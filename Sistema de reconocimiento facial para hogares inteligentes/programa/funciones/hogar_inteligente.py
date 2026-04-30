from funciones.config import ARCHIVO_PERFILES
from funciones.archivos import leer_json
from funciones.reconocimiento_facial import identificar_usuario_por_rostro


# Simula reproducir la canción favorita del usuario
def reproducir_cancion(perfil):
    print(f"Reproduciendo canción favorita: {perfil['cancion']}")


# Permite acceder al hogar inteligente si el rostro está registrado
def acceder_hogar():
    print("\nAcceso al hogar inteligente")
    print("=" * 30)

    print("Leyendo rostro desde face_id...")

    id_usuario = identificar_usuario_por_rostro()

    if id_usuario is None:
        print("\nAcceso denegado.")
        print("Perfil no registrado.")
        return

    perfiles = leer_json(ARCHIVO_PERFILES)
    perfil = perfiles[id_usuario]

    print(f"\nBienvenido, {perfil['nombre']}")
    print("Acceso permitido.")
    print("Puerta abierta.")

    reproducir_cancion(perfil)