from machine import UART

def checksum(input):
    b = bytearray(input, "ASCII")
    out = b[0]
    for i in b[1:]:
        out ^= i   # XOR the ints together in base16 then convert to hex

    if out in [0x00, 0x7b, 0x7d]:
        out = 0x55

    return out


class Bogballe:
    def __init__(self, serial, verbose = False):
        self._verbose = verbose
        self._ser = serial
        self._speed = 0
    
    def _send(self, payload):
        cs = checksum(payload)
        frame = b'\x7b'
        frame += bytes(payload, 'ASCII')
        frame += bytes([cs])
        frame += b'\x7d'
        self._ser.write(frame)
        if self._verbose:
            print("tx: ", frame)

        reply = self._ser.read()
        if self._verbose:
            print("rx: ", str(reply))

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed
        payload = "S:SpdKmh:" + f"{self._speed:.1f}" + ":"
        self._send(payload)
