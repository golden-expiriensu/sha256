from operators.rotr import rotr
from operators.shr import shr
from operators.xor import xor


def sigma0(x):
    xrot = xor(rotr(x, 7), rotr(x, 18))
    return xor(xrot, shr(x, 3))