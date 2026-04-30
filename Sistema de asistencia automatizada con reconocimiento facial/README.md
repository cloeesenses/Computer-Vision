# Sistema de asistencia automatizada con reconocimiento facial

Este proyecto corresponde al tema **5. Visión por computadora**.

El objetivo es crear un sistema sencillo de asistencia automatizada usando reconocimiento facial con la librería **DeepFace**. El programa compara una imagen de entrada contra una carpeta de rostros registrados y, si encuentra una coincidencia, registra la asistencia de la persona en un archivo CSV.

## Instalación de dependencias

Antes de ejecutar el proyecto, es necesario instalar las librerías incluidas en el archivo `requirements.txt`.

Desde la carpeta principal de este proyecto, ejecutar:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene las dependencias necesarias para que el programa funcione correctamente, incluyendo DeepFace y las librerías relacionadas con visión por computadora.

## Cómo ejecutar el proyecto

Una vez instaladas las dependencias, entrar a la carpeta `programa`:

```bash
cd programa
```

Después ejecutar el archivo principal:

```bash
python main.py
```

También se puede ejecutar directamente desde la carpeta principal del proyecto con:

```bash
python programa/main.py
```

## ¿Qué hace el proyecto?

El sistema simula un escenario donde una persona llega a una clase u oficina y su asistencia se registra automáticamente usando su rostro.

El programa realiza los siguientes pasos:

1. Lee las imágenes guardadas en la carpeta `rostros_registrados`.
2. Lee las imágenes guardadas en la carpeta `capturas_asistencias`.
3. Compara cada captura contra los rostros registrados usando DeepFace.
4. Si encuentra una coincidencia, muestra el nombre de la persona reconocida.
5. Guarda la asistencia en el archivo `registro_asistencia.csv`.

## Estructura del proyecto

```text
Sistema de asistencia automatizada con reconocimiento facial/
│
├── README.md
├── requirements.txt
│
└── programa/
    ├── main.py
    │
    ├── funciones/
    │   ├── __init__.py
    │   └── asistencias.py
    │
    ├── rostros_registrados/
    │   ├── Javier_Solis.png
    │   ├── Liz_Huerta.png
    │   └── Miranda_Garcia.png
    │
    ├── capturas_asistencias/
    │   └── entrada_1.png
    │
    └── registro_asistencia.csv
```

## Explicación de carpetas y archivos

### `programa/main.py`

Es el archivo principal del programa. Su función es iniciar el sistema llamando a las funciones necesarias.

### `programa/funciones/asistencias.py`

Contiene la lógica principal del proyecto:

- Obtener las imágenes de las carpetas.
- Convertir nombres de archivos en nombres de personas.
- Comparar rostros usando DeepFace.
- Registrar la asistencia en un archivo CSV.
- Ejecutar el flujo completo del sistema.

### `rostros_registrados/`

Aquí se guardan las imágenes de las personas que el sistema ya conoce.

El nombre del archivo se usa para identificar a la persona. Por ejemplo:

```text
Liz_Huerta.png
```

Se mostrará como:

```text
Liz Huerta
```

### `capturas_asistencias/`

Aquí se coloca la imagen de la persona que desea registrar su asistencia.

Ejemplo:

```text
entrada_1.png
```

### `registro_asistencia.csv`

Este archivo se crea o actualiza automáticamente cuando el sistema reconoce a una persona.

Guarda el nombre, la fecha y la hora de asistencia.

Ejemplo:

```text
Nombre,Fecha,Hora
Liz Huerta,2026-04-29,19:04:20
```

## Resultado esperado

Si la imagen de entrada coincide con una persona registrada, el programa mostrará algo parecido a esto:

```text
Sistema de asistencia automatizada con reconocimiento facial
============================================================

Revisando captura: entrada_1.png
Comparando con: Liz Huerta

ASISTENCIA REGISTRADA
Persona reconocida: Liz Huerta
Registro guardado en registro_asistencia.csv
```

Si la persona no es reconocida, el sistema mostrará:

```text
No se reconoció a la persona.
Asistencia no registrada.
```

## Nota sobre advertencias de GPU

Durante la ejecución pueden aparecer mensajes relacionados con CUDA, GPU o TensorFlow.

Estos mensajes no impiden que el programa funcione. Solamente indican que el programa está usando el procesador de la computadora en lugar de una tarjeta gráfica.

## Conclusión

Este proyecto demuestra cómo se puede aplicar visión por computadora en un caso real: registrar asistencia automáticamente mediante reconocimiento facial.

Aunque es una simulación sencilla, cumple con las funcionalidades principales solicitadas: usar DeepFace, comparar rostros, reconocer una persona registrada y guardar su asistencia en un archivo.