import numpy as np


def calc_npcr(ori_img, enc_img):
    diff = np.array(ori_img) - np.array(enc_img)
    diff = np.abs(diff)
    binary_diff = np.where(diff > 0.5, 1, 0)
    total_sum = 0
    for i in range(ori_img.shape[2]):
        total_sum += np.sum(np.sum(binary_diff[:, :, i]))
    total_sum = total_sum * 100.0 / (ori_img.shape[0] * ori_img.shape[1] * ori_img.shape[2])

    return total_sum


def calc_uaci(ori_img, enc_img):
    diff = np.array(ori_img) - np.array(enc_img)

    total_sum = 0
    for i in range(ori_img.shape[2]):
        total_sum += sum(sum(np.abs(diff)[:, :, i]))
    total_sum = total_sum * 100.0 / (ori_img.shape[0] * ori_img.shape[1] * ori_img.shape[2])

    return total_sum / 255.0
