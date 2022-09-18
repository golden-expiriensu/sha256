import math


primes =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

K = [0] * 64

for i, p in enumerate(primes):
    f, w = math.modf(p ** (1 / 3.0))
    f *= 16
    K[i] |= int(math.modf(f)[1])
    for _ in range(7):
        f *= 16
        x16f_f, x16f_f = math.modf(f)
        K[i] = (K[i] << 4) | int(x16f_f)

H = [0] * 8

for i in range(8):
    f, w = math.modf(primes[i] ** (1 / 2.0))
    f *= 16
    H[i] |= int(math.modf(f)[1])
    for _ in range(7):
        f *= 16
        x16f_f, x16f_f = math.modf(f)
        H[i] = (H[i] << 4) | int(x16f_f)

