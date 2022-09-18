from mod32 import mod32


def shr(x, bits):
    return mod32(x >> bits)