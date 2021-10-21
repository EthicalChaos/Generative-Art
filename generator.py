import time
import os

import yaml
from PIL import Image

from layer import Layer


def load_assets():
    try:
        global assets 
        assets = read_config()
    except:
        print("An exception occured reading the configuration file.")
    else:
        print("Configuration successfully read.")
        count = 1
        for layer in assets:
            count *= layer.variation_count()
        print(f"Generation of {count} entities possible.")

def read_config():
    config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
    return [Layer(**data) for data in config['ASSETS']]

def create():
    collection_name: str = input("Name of collection: ")

    try:
        number_to_create: int = int(input("Number of entities to create: "))
    except ValueError:
        print("Please enter a integer.")
        create()
    generate_collection(collection_name, number_to_create)

def generate_variation_set():
    # will contain a list of paths for different layers
    varation_set = []
    # loop over ever layer type
    for layer in assets:
        # get a random variation of the layer
        varation = layer.get_random_varation()
        varation_set.append(varation)

    return varation_set

def generate_image(variation, file_name= None):
    bg = Image.open(variation[0])

    # stack layers
    for path in variation[1:]:
        img = Image.open(path)
        bg.paste(img, (0,0), img)
    
    # Save the final image into desired location
    if file_name is not None:
        bg.save(os.path.join('out', file_name))
    else:
        # If output filename is not specified, use timestamp to name the image and save it in output/single_images
        if not os.path.exists(os.path.join('output', 'single_images')):
            os.makedirs(os.path.join('output', 'single_images'))
        bg.save(os.path.join('output', 'single_images', str(int(time.time())) + '.png'))

def generate_collection(name: str, amount: int):
    output = os.path.join('out', name)
    if not os.path.exists(output):
        os.makedirs(output)
    
    for i in range(amount+1):
        file_name = f"{i}.png"

        # get a random variation of layers.
        varaition_set = generate_variation_set()
        print(f"varation:{varaition_set}")

        generate_image(varaition_set, file_name)


def main():
    load_assets()
    create()

if __name__ == "__main__":
    main()
