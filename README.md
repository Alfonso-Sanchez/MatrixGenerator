# MatrixGenerator

MatrixGenerator es una aplicación en Python que te permite crear y editar iconos personalizados en una matriz 8x8. La aplicación consta de dos ventanas: una para visualizar la matriz en formato hexadecimal y otra para editar la matriz de manera visual. Puedes copiar y pegar matrices, y los cambios se reflejan en tiempo real entre ambas ventanas.
Una vez tienes tu matriz puedes añadirla en tu archivo .c de la NDS de la siguiente manera.
```c
unsigned char ok_face_bitmap[64] = {
    0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00,
    0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00,
    0xFF, 0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00, 0xFF,
    0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF,
    0xFF, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0xFF,
    0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF,
    0x00, 0xFF, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00,
    0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00
};
```
## Características

- **Matriz 8x8**: Crea y edita iconos en una cuadrícula de 8x8 píxeles.
- **Ventana de Matriz Hexadecimal**: Muestra la matriz en formato hexadecimal (`0x00` para negro y `0xFF` para blanco).
- **Ventana de Matriz Visual**: Edita la matriz haciendo clic en los cuadrados para cambiar entre blanco y negro.
- **Copiar y Pegar**: Copia la matriz actual al portapapeles o pega una matriz desde el portapapeles.
- **Actualización en Tiempo Real**: Los cambios en una ventana se reflejan automáticamente en la otra.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (incluida en la instalación estándar de Python)

## Instalación

1. Clona este repositorio o descarga el archivo `matrixgenerator.py`.
2. Asegúrate de tener Python instalado en tu sistema.

## Uso

1. Ejecuta la aplicación:
   ```bash
   python matrixgenerator.py
- **También puedes usar el .exe disponible en las releases de este repositorio.**
