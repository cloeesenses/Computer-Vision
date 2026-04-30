# Clase que representa un perfil registrado en el hogar inteligente
class PerfilUsuario:
    def __init__(self, nombre, foto, cancion):
        self.nombre = nombre
        self.foto = foto
        self.cancion = cancion


    # Convierte el perfil en diccionario para guardarlo en JSON
    def convertir_a_diccionario(self):
        return {
            "nombre": self.nombre,
            "foto": self.foto,
            "cancion": self.cancion
        }