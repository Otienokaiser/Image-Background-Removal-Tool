from rembg import remove
from PIL import Image

# Load the input image
input_path = 'patinahorsebits.jpeg'
output_path = 'output_image.png'
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image
output_image.save(output_path)

print(f"Background removed and saved to {output_path}")
