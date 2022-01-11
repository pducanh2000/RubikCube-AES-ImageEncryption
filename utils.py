import sys
import random
import json

from PIL import Image
import numpy as np

from Aes import *


def read_image(image_path):
    image = Image.open(image_path)
    image = np.array(image)
    return image


def save_image(image, image_save_path):
    s_image = Image.fromarray(image)
    s_image.save(image_save_path)
    return


def create_key(image, ITER_MAX=2, alpha=8, aes=None):
    # Create vector Kr and Kc
    Kr = [random.randint(0, 2 ** alpha - 1) for i in range(image.shape[0])]
    Kc = [random.randint(0, 2 ** alpha - 1) for i in range(image.shape[1])]

    dict_key = {"Kr": Kr,
                "Kc": Kc,
                "ITER": ITER_MAX
                }
    if aes is not None:
        dict_key = encrypt(dict_key, aes)
    return dict_key


def save_key(dict_key, save_path="./key.json"):
    with open(save_path, "w") as F:
        json.dump(dict_key, F, indent=4)


def load_key(save_path="./key.json", aes=None):
    with open(save_path, "r") as F:
        dict_key = json.load(F)

    if aes is not None:
        dict_key = decrypt(dict_key, aes)

    Kr = dict_key["Kr"]
    Kc = dict_key["Kc"]
    ITER_MAX = dict_key["ITER"]

    return Kr, Kc, ITER_MAX
