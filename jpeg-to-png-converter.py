import os
from PIL import Image

def convert_jpeg_to_png(input_path):
    # Load the image
    with Image.open(input_path) as img:
        # Check file format
        if img.format == 'JPEG':
            # Create output filename
            output_path = os.path.splitext(input_path)[0] + '.png'
            
            # Convert and save as PNG
            img.save(output_path, 'PNG')
            print(f"Converted {input_path} to {output_path}")
        elif img.format == 'PNG':
            print(f"{input_path} is already a PNG file. No conversion needed.")
        else:
            print(f"{input_path} is neither JPEG nor PNG. Skipping.")

def main():
    # Get input file path from user
    input_path = input("Enter the path to the JPEG image: ").strip()
    
    # Check if file exists
    if not os.path.exists(input_path):
        print("File not found. Please check the path and try again.")
        return
    
    # Perform conversion
    convert_jpeg_to_png(input_path)

if __name__ == "__main__":
    main()
