from operators.rotr import rotr
from operators.shr import shr
from operators.xor import xor


def sigma1(x):
    xrot = xor(rotr(x, 17), rotr(x, 19))
    return xor(xrot, shr(x, 10))