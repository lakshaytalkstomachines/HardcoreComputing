"""
This file is used to generate RGB images using random numbers as pixels values and store them in a file.
"""
import random
import numpy as np
from PIL import Image
import argparse

def generate_image(width, height):
    """
    generates a random image of size width x height in 3 channels.
    """
    image = np.zeros((height, width, 3))
    for i in range(height):
        for j in range(width):
            image[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return image    


def save_image(image, filename):
    """
    saves the image to a file.
    """
    image = Image.fromarray(image.astype(np.uint8)) # convert the image to a PIL image
    image.save(filename)    

def generate_and_save_image(width, height, filename):
    """
    generates a random image of size width x height and saves it to a file.
    """
    image = generate_image(width, height)
    save_image(image, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=10)
    parser.add_argument("--height", type=int, default=10)
    parser.add_argument("--filename", type=str, default="image.png")
    args = parser.parse_args()
    generate_and_save_image(args.width, args.height, args.filename)