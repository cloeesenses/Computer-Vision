# Sistema de reconocimiento facial para hogares inteligentes

Este proyecto corresponde al tema **5. Visión por computadora**.

El sistema simula un hogar inteligente que reconoce perfiles registrados mediante reconocimiento facial.  
Cuando identifica a un usuario, permite el acceso, abre la puerta y reproduce su canción favorita previamente registrada.

## Instalación

Antes de ejecutar el proyecto, instalar las dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```text
deepface
tf-keras
yt-dlp
```

Para convertir canciones de YouTube a MP3 también se necesita `ffmpeg`.

En Ubuntu/WSL se puede instalar con:

```bash
sudo apt install ffmpeg
```

## Cómo ejecutar el proyecto

Entrar a la carpeta `programa`:

```bash
cd programa
```

Ejecutar el archivo principal:

```bash
python main.py
```

También se puede ejecutar desde la carpeta principal del proyecto:

```bash
python programa/main.py
```

## Menú del sistema

Al ejecutar el programa aparece este menú:

```text
1. Registrar nuevo perfil
2. Acceder al hogar
3. Salir
```

## Opción 1: Registrar nuevo perfil

Esta opción permite registrar un usuario nuevo en el hogar inteligente.

Primero pide la contraseña de administrador:

```text
1234
```

Después solicita:

```text
Nombre del usuario
Ruta del archivo del rostro
Link de YouTube de su canción favorita
```

El sistema hace lo siguiente:

1. Guarda la foto del usuario en `rostros_usuarios/`.
2. Descarga la canción favorita en formato MP3 dentro de `canciones_usuarios/`.
3. Guarda los datos del perfil en `datos/perfiles.json`.

## Opción 2: Acceder al hogar

Esta opción simula el acceso al hogar inteligente.

Antes de elegir esta opción, se debe colocar manualmente una imagen dentro de la carpeta:

```text
face_id/
```

La carpeta `face_id/` simula ser la cámara del sistema.  
Es decir, la imagen que se coloque ahí representa a la persona que está frente a la puerta intentando entrar.

Por ejemplo:

```text
face_id/
└── miranda.png
```

Después de colocar la imagen en `face_id/`, se ejecuta el programa y se selecciona:

```text
2. Acceder al hogar
```

El sistema toma automáticamente la primera imagen encontrada en `face_id/` y la compara contra los rostros registrados en:

```text
rostros_usuarios/
```

Si el rostro coincide con un perfil registrado, el sistema permite el acceso, saluda al usuario y reproduce su canción favorita.

Si el rostro no coincide con ningún perfil registrado, el sistema niega el acceso.

> Importante: para probar diferentes accesos, cambia manualmente la imagen dentro de `face_id/`. Esa imagen funciona como si fuera la captura de la cámara.

## Estructura del proyecto

```text
Sistema de reconocimiento facial para hogares inteligentes/
│
├── README.md
├── requirements.txt
│
└── programa/
    ├── main.py
    │
    ├── datos/
    │   └── perfiles.json
    │
    ├── face_id/
    │   └── miranda.png
    │
    ├── funciones/
    │   ├── __init__.py
    │   ├── archivos.py
    │   ├── config.py
    │   ├── descarga_youtube.py
    │   ├── hogar_inteligente.py
    │   ├── perfiles.py
    │   └── reconocimiento_facial.py
    │
    ├── modelos/
    │   ├── __init__.py
    │   └── perfil_usuario.py
    │
    ├── rostros_usuarios/
    │   └── miranda.png
    │
    └── canciones_usuarios/
        └── miranda.mp3
```

## Archivos principales

### `main.py`

Es el archivo principal del programa.  
Muestra el menú y llama a las funciones correspondientes.

### `funciones/perfiles.py`

Contiene la lógica para registrar nuevos perfiles.

### `funciones/reconocimiento_facial.py`

Contiene la lógica para comparar la imagen de `face_id/` contra los rostros registrados.

### `funciones/hogar_inteligente.py`

Contiene la lógica para permitir o negar el acceso al hogar.

### `funciones/descarga_youtube.py`

Contiene la función para descargar la canción favorita desde YouTube y guardarla como MP3.

### `modelos/perfil_usuario.py`

Contiene la clase `PerfilUsuario`, que representa cada perfil registrado con nombre, foto y canción.

## Resultado esperado: perfil reconocido

Si la imagen en `face_id/` coincide con un perfil registrado, el programa mostrará algo parecido a esto:

```text
Acceso al hogar inteligente
==============================
Leyendo rostro desde face_id...
Imagen detectada por face_id: miranda.png
Comparando con: Miranda

Bienvenido, Miranda
Acceso permitido.
Puerta abierta.
Reproduciendo canción favorita: canciones_usuarios/miranda.mp3
```

## Resultado esperado: perfil no registrado

Si la imagen en `face_id/` no coincide con ningún perfil registrado, el programa mostrará algo parecido a esto:

```text
Acceso al hogar inteligente
==============================
Leyendo rostro desde face_id...
Imagen detectada por face_id: persona_no_registrada.png
Comparando con: Miranda

Acceso denegado.
Perfil no registrado.
```

## Nota sobre advertencias de GPU

Durante la ejecución pueden aparecer mensajes relacionados con CUDA, GPU o TensorFlow.

Estos mensajes no impiden que el programa funcione. Solamente indican que el programa está usando el procesador de la computadora en lugar de una tarjeta gráfica.

## Conclusión

Este proyecto demuestra cómo se puede aplicar visión por computadora en un hogar inteligente.  
El sistema registra perfiles, guarda un rostro, descarga una canción favorita, reconoce usuarios registrados y simula acciones automáticas como abrir la puerta y reproducir música personalizada.