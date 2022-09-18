from distutils.command.build_scripts import first_line_re
from operators.add import add
from functions.sigma0 import sigma0
from functions.sigma1 import sigma1

def schedule(x):
    res = [0] * 64

    for i in range(15, -1, -1):
        res[i] = x[0] & 0xFFFFFFFF
        x[0] >>= 32

    for i in range(16, 64):
        first = add(sigma1(res[i - 2]), res[i - 7])
        second = add(sigma0(res[i - 15]), res[i - 16])
        res[i] = add(first, second)

    return res