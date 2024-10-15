from rembg import remove
from PIL import Image

try:
    input_path = "images\Before.jpg"
    output_path = "images\\delete_output.png"
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    if output.save:
        print("The image is processed and ready")
except:
    print("Don't ready")