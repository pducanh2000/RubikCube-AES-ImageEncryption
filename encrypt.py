import matplotlib.pyplot as plt
import numpy as np

from Aes import *
from rubik_function import *
from utils import *


def encrypt_image(image, key_path="./key.json", aes=None):
    # Load Key
    Kr, Kc, ITER_MAX = load_key(save_path=key_path, aes=aes)

    # Split channels
    r = np.array(image[:, :, 0])
    g = np.array(image[:, :, 1])
    b = np.array(image[:, :, 2])

    for iter in range(ITER_MAX):
        # For each row
        for i in range(image.shape[0]):
            r_modulus = sum(r[i]) % 2
            g_modulus = sum(g[i]) % 2
            b_modulus = sum(b[i]) % 2
            r[i] = np.roll(r[i], -Kr[i]) if r_modulus else np.roll(r[i], Kr[i])
            g[i] = np.roll(g[i], -Kr[i]) if g_modulus else np.roll(g[i], Kr[i])
            b[i] = np.roll(b[i], -Kr[i]) if b_modulus else np.roll(b[i], Kr[i])

        # For each column
        for i in range(image.shape[1]):
            r_modulus = sum(r[:, i]) % 2
            g_modulus = sum(g[:, i]) % 2
            b_modulus = sum(b[:, i]) % 2
            r = downshift(r, i, Kc[i]) if r_modulus else upshift(r, i, Kc[i])
            g = downshift(g, i, Kc[i]) if g_modulus else upshift(g, i, Kc[i])
            b = downshift(b, i, Kc[i]) if b_modulus else upshift(b, i, Kc[i])

        # For each row
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if (i % 2 == 1):
                    r[i][j] = r[i][j] ^ Kc[j]
                    g[i][j] = g[i][j] ^ Kc[j]
                    b[i][j] = b[i][j] ^ Kc[j]
                else:
                    r[i][j] = r[i][j] ^ rotate(Kc[j])
                    g[i][j] = g[i][j] ^ rotate(Kc[j])
                    b[i][j] = b[i][j] ^ rotate(Kc[j])

        # For each column
        for j in range(image.shape[1]):
            for i in range(image.shape[0]):
                if (j % 2 == 0):
                    r[i][j] = r[i][j] ^ Kr[i]
                    g[i][j] = g[i][j] ^ Kr[i]
                    b[i][j] = b[i][j] ^ Kr[i]
                else:
                    r[i][j] = r[i][j] ^ rotate(Kr[i])
                    g[i][j] = g[i][j] ^ rotate(Kr[i])
                    b[i][j] = b[i][j] ^ rotate(Kr[i])

    encrypted_img = np.stack((r, g, b), axis=2)
    return encrypted_img


if __name__ == "__main__":
    image_path = "/content/drive/MyDrive/LTMM/iris-flower-5995009_1280.jpg"
    key_path = "./key.json"
    encrypted_path = "/content/drive/MyDrive/LTMM/encrypted_image.jpg"
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    aes = AES(master_key)

    image = read_image(image_path)

    dict_key = create_key(image, ITER_MAX=2, aes=aes)
    save_key(dict_key, save_path=key_path)

    en_image = encrypt_image(image, key_path, aes=aes)
    save_image(en_image, encrypted_path)

    fig, ax = plt.subplots(1, 2, figsize=(20, 20))
    ax[0].imshow(image)
    ax[0].set_title("Original Image")

    ax[1].imshow(en_image)
    ax[1].set_title("Encrypted Image")
    fig.show()
