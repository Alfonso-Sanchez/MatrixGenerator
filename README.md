# MatrixGenerator

MatrixGenerator is a Python application that allows you to create and edit custom icons on an 8x8 matrix. The application consists of two windows: one to display the matrix in hexadecimal format and another to edit the matrix visually. You can copy and paste matrices, and changes are reflected in real-time between both windows.
Once you have your matrix, you can add it to your NDS .c file as follows.
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
## Features

- **8x8 Matrix**: Create and edit icons on an 8x8 pixel grid.
- **Hexadecimal Matrix Window**: Displays the matrix in hexadecimal format (`0x00` for black and `0xFF` for white).
- **Visual Matrix Window**: Edit the matrix by clicking on the squares to toggle between black and white.
- **Copy and Paste**: Copy the current matrix to the clipboard or paste a matrix from the clipboard.
- **Real-Time Updates**: Changes in one window are automatically reflected in the other.

## Requirements

- Python 3.x
- `tkinter` library (included in the standard Python installation)

## Installation

1. Clone this repository or download the `matrixgenerator.py` file.
2. Make sure you have Python installed on your system.

## Usage

1. Run the application:
   ```bash
   python matrixgenerator.py
   ```
- **You can also use the .exe available in the releases of this repository.**
