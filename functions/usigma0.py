from operators.rotr import rotr
from operators.xor import xor


def usigma0(x):
    xrot = xor(rotr(x, 2), rotr(x, 13))
    return xor(xrot, rotr(x, 22))