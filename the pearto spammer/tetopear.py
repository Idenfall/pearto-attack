import os
import random
from PIL import Image
import time

# current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# path to "data" folder
folder_path = os.path.join(script_dir, 'data')

# can add more extensions if needed
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# images in the folder
if not image_files:
    print("No image files found in the 'data' folder.")
else:
    while True:
        # pick image
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)

        # show the image
        img = Image.open(image_path)
        img.show()

        print(f"Opened: {random_image}")

        
        time.sleep(0.5)  # (in seconds) 
