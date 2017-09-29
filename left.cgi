
#!/usr/bin/env python


import time
import serial
  

ser = serial.Serial(
  
   port='/dev/serial0',
   baudrate = 2400,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0
  

while 1:
   data = bytearray([255])
   ser.write(data)
