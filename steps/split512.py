def split512(x):
    if (x.bit_length() < 447):
        even_len = x.bit_length() if x.bit_length() % 2 == 0 else x.bit_length() + 1
        shift = 448 - 1 - even_len
        padded_no_len = ((x << 1) | 1) << shift
        return [(padded_no_len << 64) | even_len]
    else:
        raise Exception('text bitlen more than 447, idk what to do...')
