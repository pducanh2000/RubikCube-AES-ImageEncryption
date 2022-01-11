import matplotlib.pyplot as plt
import numpy as np

from Aes import *
from rubik_function import *
from utils import *


def decrypt_image(encrypted_image, key_path="./key.json", aes=None):
    # Load key
    Kr, Kc, ITER_MAX = load_key(save_path=key_path, aes=aes)

    # Split channels
    r = np.array(encrypted_image[:, :, 0])
    g = np.array(encrypted_image[:, :, 1])
    b = np.array(encrypted_image[:, :, 2])

    for iteration in range(ITER_MAX):
        # For each column
        for j in range(encrypted_image.shape[1]):
            for i in range(encrypted_image.shape[0]):
                if (j % 2 == 0):
                    r[i][j] = r[i][j] ^ Kr[i]
                    g[i][j] = g[i][j] ^ Kr[i]
                    b[i][j] = b[i][j] ^ Kr[i]
                else:
                    r[i][j] = r[i][j] ^ rotate(Kr[i])
                    g[i][j] = g[i][j] ^ rotate(Kr[i])
                    b[i][j] = b[i][j] ^ rotate(Kr[i])

        # For each row
        for i in range(encrypted_image.shape[0]):
            for j in range(encrypted_image.shape[1]):
                if (i % 2 == 1):
                    r[i][j] = r[i][j] ^ Kc[j]
                    g[i][j] = g[i][j] ^ Kc[j]
                    b[i][j] = b[i][j] ^ Kc[j]
                else:
                    r[i][j] = r[i][j] ^ rotate(Kc[j])
                    g[i][j] = g[i][j] ^ rotate(Kc[j])
                    b[i][j] = b[i][j] ^ rotate(Kc[j])

    # For each column
    for i in range(encrypted_image.shape[1]):
        r_modulus = sum(r[:, i]) % 2
        g_modulus = sum(g[:, i]) % 2
        b_modulus = sum(b[:, i]) % 2
        r = upshift(r, i, Kc[i]) if r_modulus else downshift(r, i, Kc[i])
        g = upshift(g, i, Kc[i]) if g_modulus else downshift(g, i, Kc[i])
        b = upshift(b, i, Kc[i]) if b_modulus else downshift(b, i, Kc[i])

    # For each row
    for i in range(encrypted_image.shape[0]):
        r_modulus = sum(r[i]) % 2
        g_modulus = sum(g[i]) % 2
        b_modulus = sum(b[i]) % 2
        r[i] = np.roll(r[i], Kr[i]) if r_modulus else np.roll(r[i], -Kr[i])
        g[i] = np.roll(g[i], Kr[i]) if g_modulus else np.roll(g[i], -Kr[i])
        b[i] = np.roll(b[i], Kr[i]) if b_modulus else np.roll(b[i], -Kr[i])

    decrypted_img = np.stack((r, g, b), axis=2)
    return decrypted_img


if __name__ == "__main__":
    key_path = "./key.json"
    decrypted_path = "./decrypted_image.jpg"
    encrypted_path = "./encrypted_image.jpg"
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c

    aes = AES(master_key)
    encrypted_image = read_image(encrypted_path)
    # encrypted_image = en_image
    de_img = decrypt_image(encrypted_image, key_path, aes)
    save_image(de_img, decrypted_path)

    fig, ax = plt.subplots(1, 2, figsize=(20, 20))
    ax[0].imshow(encrypted_image)
    ax[0].set_title("Encrypted Image")

    ax[1].imshow(de_img)
    ax[1].set_title("Decrypted Image")
    fig.show()