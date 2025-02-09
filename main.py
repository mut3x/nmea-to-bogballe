from micropyGPS import MicropyGPS
from bogballe import Bogballe
from machine import UART, Pin

def main():
    input = UART(0, 19200)
    gnss = MicropyGPS()
    spreader = Bogballe(UART(1, 9600, timeout = 1), True)
    led = Pin(25, Pin.OUT)
    speed = 0.0
    while True:
        # Wait for data or timeout
        data = input.read()
        if not data:
            continue

        for b in data.decode('utf-8'):
            sentence = gnss.update(b)
            if sentence:
                led.toggle()
                if speed != gnss.speed[2]:
                    speed = gnss.speed[2]
                    spreader.speed = speed

if __name__ == '__main__':
    main()
