def convert(text):
    byte_array = text.encode()
    return int.from_bytes(byte_array, "big")