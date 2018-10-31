from bitarray import bitarray
def checksum(data):
    ssum = 0
    for i in range(0,5):
        b = data[8*i:8*i+8]
        b.reverse()
        ssum += int.from_bytes(b.tobytes(), byteorder='big')
    ssum = 2**8 - ssum % 2**8
    cs = bitarray()
    cs.frombytes(bytes([ssum]))
    cs.reverse()
    return cs
