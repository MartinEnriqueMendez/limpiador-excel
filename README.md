# Limpiador de Planillas de Cálculo

Este proyecto es una herramienta de automatización en Python diseñada para procesar, limpiar y estandarizar múltiples archivos de Excel de forma masiva. Ideal para transformar datos "sucios" en información lista para el análisis.

## Funcionalidades
- Procesamiento Masivo: Escanea la carpeta `data/input/` y procesa todos los archivos `.xlsx`.
- Limpieza Profunda:
  - Elimina filas vacías y duplicados.
  - Estandariza nombres de columnas (minúsculas, sin espacios).
  - Corrige formatos de **fechas** y **montos** numéricos.
  - Normaliza texto (ej: Corrección automática de sucursales como "Sp" a "San Pedro").
- Generación de Reportes: Crea un archivo PDF con el resumen de la limpieza por cada planilla.

## Estructura del Proyecto
```text
limpiador-planillas/
├── data/
│   ├── input/         # Coloca aquí tus archivos .xlsx sucios
│   └── output/        # Aquí aparecerán los archivos pulidos
├── src/
│   ├── main.py        # Orquestador del proceso
│   ├── limpiador.py   # Lógica de limpieza con Pandas
│   └── reporte.py     # Generador de reportes PDF
├── requirements.txt   # Librerías necesarias
└── README.md