import numpy as np


def upshift(a, index, n):
    """
    Shift the column up with index with numpy.roll(column, -n)
    """
    col = a[:, index]
    shift_col = np.roll(col, -n)
    for i in range(len(a)):
        a[i][index] = shift_col[i]
    return a


def downshift(a, index, n):
    """
    Shift the column down with index with numpy.roll(column, n)
    """
    col = a[:, index]
    shift_col = np.roll(col, n)
    for i in range(len(a)):
        a[i][index] = shift_col[i]
    return a


def rotate(n):
    """
    Rotate 180 the binary bit string of n and convert to integer
    """
    bits = "{0:b}".format(n)
    return int(bits[::-1], 2)
