# Sistema de inicio de sesión seguro con verificación facial

Este proyecto corresponde al tema **5. Visión por computadora**.

El sistema simula un inicio de sesión usando verificación facial con **DeepFace**.  
Compara la imagen de un usuario autorizado con la imagen de una persona que intenta entrar.  
Si los rostros coinciden, el acceso se concede. Si no coinciden, el acceso se deniega.

## Instalación

Antes de ejecutar el proyecto, instalar las dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```text
deepface
tf-keras
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

## Estructura del proyecto

```text
Sistema de inicio de sesión seguro con verificación facial/
│
├── README.md
├── requirements.txt
│
└── programa/
    ├── main.py
    │
    ├── funciones/
    │   ├── __init__.py
    │   └── login_facial.py
    │
    ├── usuario_autorizado/
    │   └── Liz_Huerta.png
    │
    └── intento_login/
        └── Miranda_Garcia.png
```

## ¿Qué hace el programa?

1. Lee la imagen de la carpeta `usuario_autorizado`.
2. Lee la imagen de la carpeta `intento_login`.
3. Compara ambos rostros usando DeepFace.
4. Muestra si el acceso fue concedido o denegado.

## Archivos principales

### `main.py`

Es el archivo principal.  
Solo llama a la función que ejecuta el sistema.

### `funciones/login_facial.py`

Contiene las funciones del sistema:

- Obtener imágenes de las carpetas.
- Seleccionar la primera imagen disponible.
- Comparar los rostros con DeepFace.
- Mostrar el resultado del inicio de sesión.

## Resultado esperado: acceso concedido

Si ambas imágenes pertenecen a la misma persona:

```text
Sistema de inicio de sesión seguro con verificación facial
=================================================================

Usuario autorizado: Liz_Huerta.png
Intento de login: Liz_Huerta.png

ACCESO CONCEDIDO
Bienvenido al sistema.
```

## Resultado esperado: acceso denegado

Si las imágenes pertenecen a personas diferentes:

```text
Sistema de inicio de sesión seguro con verificación facial
=================================================================

Usuario autorizado: Liz_Huerta.png
Intento de login: Miranda_Garcia.png

ACCESO DENEGADO
Rostro no autorizado.
```

## Nota

Para evitar errores con DeepFace, se recomienda que los nombres de carpetas y archivos no tengan acentos ni caracteres especiales.

También pueden aparecer advertencias relacionadas con GPU o CUDA.  
Estas advertencias no impiden que el programa funcione.

## Conclusión

Este proyecto muestra cómo aplicar visión por computadora en un sistema básico de seguridad, usando DeepFace para verificar si una persona tiene permiso para iniciar sesión.