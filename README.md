# Plan de Publicaciones

Esta aplicación web permite cargar múltiples imágenes y textos (copys) para generar un archivo PDF que resume el plan de publicaciones para Instagram.

## Requisitos

- Python 3.10+
- Las dependencias listadas en `requirements.txt`

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
2. Abre un navegador y visita `http://localhost:5000`.
3. Agrega tantas publicaciones como necesites y presiona **Generar PDF** para descargar el plan.

## Estructura

- `app.py`: servidor Flask que genera el PDF.
- `templates/index.html`: formulario para subir imágenes y copys.
- `requirements.txt`: dependencias del proyecto.

