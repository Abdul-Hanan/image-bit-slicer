# image-bit-slicer

This project extracts and visualizes individual bit planes from a grayscale image. It demonstrates how pixel intensity values (0-255) are composed by their underlying 8 bits.

## Features

- Generates a simple grayscale image with a gradient for self-contained demonstration.
- Extracts each of the 8 bit planes from the grayscale image.
- Saves each bit plane as a separate binary (black and white) image file.
- Designed to run on headless servers without any display or GUI.

## How to Run

1.  **Save the files**: Ensure `main.py`, `requirements.txt`, and this `README.md` are in the same directory.
2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the script**:
    ```bash
    python main.py
    ```

After execution, a new directory named `output_bit_planes` will be created. Inside, you will find `original_grayscale_image.png` and 8 binary images named `bit_plane_0.png` through `bit_plane_7.png`. `bit_plane_0.png` represents the Least Significant Bit (LSB), and `bit_plane_7.png` represents the Most Significant Bit (MSB).