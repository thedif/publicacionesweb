# Plan de Publicaciones

Esta web genera un PDF con tu plan de publicaciones para Instagram. Permite cargar varias imágenes y copys para combinarlos en un solo documento.

## Uso

1. Abre `index.html` en tu navegador (puedes hacer doble clic o servirlo con cualquier servidor estático).
2. Agrega todas las publicaciones que necesites con el botón **Agregar publicación**.
3. Pulsa **Generar PDF** y se descargará el plan con cada imagen y su copy.
   El documento se genera en orientación horizontal colocando la imagen a la
   izquierda y el texto a la derecha.

No se requiere ningún backend ni dependencias adicionales: todo se ejecuta en tu navegador utilizando JavaScript y la biblioteca [jsPDF](https://github.com/parallax/jsPDF).

## Estructura

- `index.html`: página principal con el formulario y la lógica para crear el PDF.
