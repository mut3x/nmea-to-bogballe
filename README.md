# nmea-to-bogballe

# Overview
`nmea-to-bogballe` transcodes NMEA input to the bogballe serial protocol. It reads the NMEA input from UART0, decodes the fields of each received sentence using micropyGPS. When one of the required values changes it is encoded in the bogballe serial protocol and transmitted over UART1.

# Setup
# Hardware
In order to use the provided scripts a Raspberry PI Pico, a UART to RS232 shield and RS232 connectors are required.

Example hardware:
Raspberry PI Pico: https://botland.de/module-und-sets-fuer-raspberry-pi-pico/18767-raspberry-pi-pico-rp2040-arm-cortex-m0--0617588405587.html

RS232 Shield: https://botland.de/raspberry-pi-pico-hat-pin-expander/19716-2-kanal-rs232-modul-sp3232een-transceiver-fur-raspberry-pi-pico-uart-rs232-waveshare-19979-5904422347222.html

# Micropython
Install Micropython on the Rapsberry Pi Pico as described at https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

# File Upload
There are several options to upload the scripts to the Raspberry PI Pico. 

Examples:
- VSCode with `MicroPico` extension
- Python module `mpremote`





