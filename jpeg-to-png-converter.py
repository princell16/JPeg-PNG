import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path, adjust_resolution=False, new_resolution=None):
    try:
        # Import JPEG file
        with Image.open(input_path) as img:
            # Resolution Adjustment
            if adjust_resolution and new_resolution:
                img = img.resize(new_resolution)

            # Convert to PNG
            img = img.convert("RGBA")
            
            # Save as PNG
            img.save(output_path, "PNG")
        
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    input_file = input("Enter the path to the JPEG file: ")
    output_file = os.path.splitext(input_file)[0] + ".png"

    adjust_res = input("Do you want to adjust the resolution? (yes/no): ").lower() == 'yes'
    new_res = None

    if adjust_res:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        new_res = (width, height)

    convert_jpeg_to_png(input_file, output_file, adjust_res, new_res)

if __name__ == "__main__":
    main()
