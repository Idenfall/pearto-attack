import os
import random
import threading
from PIL import Image
import time
import pyautogui
import pygame

# Init pygame mixer
pygame.mixer.init()

# current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# paths
folder_path = os.path.join(script_dir, 'data')
sound_path = os.path.join(folder_path, 'sound', 'teto.mp3')

# play music in a separate thread
def play_music():
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # loop forever

music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

# image files
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("No image files found in the 'data' folder.")
else:
    print("Starting in 3 seconds... switch to a text box/window!")
    time.sleep(3)

    while True:
        pyautogui.typewrite("teto supremacy\n", interval=0.05)

        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        img = Image.open(image_path)
        img.show()

        print(f"Opened: {random_image}")

        time.sleep(0.5)
