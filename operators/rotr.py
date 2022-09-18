from mod32 import mod32


def rotr(x, bits):
    return mod32((x >> bits) | (x << (32 - bits)))