from funciones.config import (
    CONTRASENA_ADMIN,
    CARPETA_ROSTROS,
    CARPETA_CANCIONES,
    ARCHIVO_PERFILES,
    BASE_DIR
)

from funciones.archivos import (
    leer_json,
    guardar_json,
    crear_id_usuario,
    copiar_foto_usuario
)

from funciones.descarga_youtube import descargar_cancion_youtube
from modelos.perfil_usuario import PerfilUsuario


# Verifica que la contraseña de administrador sea correcta
def validar_contrasena_admin():
    contrasena = input("Ingrese la contraseña de administrador: ")

    if contrasena == CONTRASENA_ADMIN:
        return True

    print("Contraseña incorrecta. No se puede registrar el perfil.")
    return False


# Guarda un nuevo perfil dentro del archivo perfiles.json
def guardar_perfil(id_usuario, perfil):
    perfiles = leer_json(ARCHIVO_PERFILES)

    if id_usuario in perfiles:
        print("Ya existe un perfil registrado con ese nombre.")
        return False

    perfiles[id_usuario] = perfil.convertir_a_diccionario()
    guardar_json(ARCHIVO_PERFILES, perfiles)

    return True


# Registra un nuevo perfil de usuario
def registrar_nuevo_perfil():
    print("\nRegistro de nuevo perfil")
    print("=" * 30)

    if not validar_contrasena_admin():
        return

    nombre = input("Nombre del usuario: ")
    ruta_foto_original = input("Ruta del archivo del rostro: ")
    link_cancion = input("Link de YouTube de su canción favorita: ")

    id_usuario = crear_id_usuario(nombre)

    CARPETA_ROSTROS.mkdir(exist_ok=True)
    CARPETA_CANCIONES.mkdir(exist_ok=True)

    try:
        ruta_foto_guardada = copiar_foto_usuario(
            ruta_origen=ruta_foto_original,
            carpeta_destino=CARPETA_ROSTROS,
            id_usuario=id_usuario
        )

        ruta_cancion_guardada = descargar_cancion_youtube(
            link=link_cancion,
            nombre_archivo=f"{id_usuario}.mp3"
        )

        foto_relativa = str(ruta_foto_guardada.relative_to(BASE_DIR))
        cancion_relativa = str(ruta_cancion_guardada.relative_to(BASE_DIR))

        perfil = PerfilUsuario(
            nombre=nombre,
            foto=foto_relativa,
            cancion=cancion_relativa
        )

        perfil_guardado = guardar_perfil(id_usuario, perfil)

        if perfil_guardado:
            print("\nPerfil registrado correctamente.")
            print(f"Usuario: {nombre}")
            print(f"Foto guardada en: {foto_relativa}")
            print(f"Canción guardada en: {cancion_relativa}")

    except Exception as error:
        print("\nOcurrió un error al registrar el perfil.")
        print(f"Error: {error}")