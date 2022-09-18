from operators.add import add
from functions.ch import ch
from functions.maj import maj
from functions.usigma1 import usigma1
from functions.usigma0 import usigma0

def compress(W, K, H):
    a = H[0]
    b = H[1]
    c = H[2]
    d = H[3]
    e = H[4]
    f = H[5]
    g = H[6]
    h = H[7]

    for i in range(64):
        T1 = add(add(add(usigma1(e), ch(e, f, g)), h), add(K[i], W[i]))
        T2 = add(usigma0(a), maj(a, b, c))

        h = g
        g = f
        f = e
        e = add(d, T1)
        d = c
        c = b
        b = a
        a = add(T1, T2)

    a = add(a, H[0]) << 32 * 7
    b = add(b, H[1]) << 32 * 6
    c = add(c, H[2]) << 32 * 5
    d = add(d, H[3]) << 32 * 4
    e = add(e, H[4]) << 32 * 3
    f = add(f, H[5]) << 32 * 2
    g = add(g, H[6]) << 32 * 1
    h = add(h, H[7])

    return a | b | c | d | e | f | g | h
