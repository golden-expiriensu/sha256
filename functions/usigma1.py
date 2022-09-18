from operators.rotr import rotr
from operators.xor import xor


def usigma1(x):
    xrot = xor(rotr(x, 6), rotr(x, 11))
    return xor(xrot, rotr(x, 25))