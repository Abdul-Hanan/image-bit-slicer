import numpy as np
import cv2
import os

def generate_synthetic_image(width=256, height=256):
    """
    Generates a simple grayscale image with a horizontal gradient from 0 to 255.
    This image is good for visualizing bit planes as patterns become clear.
    """
    # Create a 1D array representing a gradient from 0 to 255
    gradient_row = np.linspace(0, 255, width, dtype=np.uint8)
    # Tile this row 'height' times to create the 2D image
    img = np.tile(gradient_row, (height, 1))
    return img

def main():
    """
    Main function to generate an image, extract its bit planes,
    and save them as binary images.
    """
    output_dir = "output_bit_planes"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory '{output_dir}' created or already exists.")

    # 1. Generate synthetic grayscale image
    print("Generating synthetic grayscale image (256x256 with horizontal gradient)...")
    original_image = generate_synthetic_image(width=256, height=256)
    original_path = os.path.join(output_dir, "original_grayscale_image.png")
    cv2.imwrite(original_path, original_image)
    print(f"Saved original grayscale image to {original_path}")

    # 2. Extract and save each of the 8 bit planes
    print("\nExtracting and saving 8 bit planes...")
    for i in range(8):  # Iterate through bit planes from 0 (Least Significant Bit) to 7 (Most Significant Bit)
        # Shift the image right by 'i' bits. This moves the i-th bit to the LSB position.
        shifted_image = original_image >> i

        # Perform a bitwise AND with 1 to isolate the LSB (which is now the i-th original bit).
        # This results in a binary image where pixels are either 0 or 1.
        bit_plane = shifted_image & 1

        # Scale the 0/1 values to 0/255 for proper visualization as a binary (black and white) image.
        visual_bit_plane = bit_plane * 255

        plane_path = os.path.join(output_dir, f"bit_plane_{i}.png")
        cv2.imwrite(plane_path, visual_bit_plane)
        print(f"Saved bit plane {i} (0=LSB, 7=MSB) to {plane_path}")

    print("\nBit plane extraction complete. Check the 'output_bit_planes' directory for results.")

if __name__ == "__main__":
    main()