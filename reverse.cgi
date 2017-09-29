
#!/usr/bin/env python


import time
import serial
  

ser = serial.Serial(
  
   port='/dev/serial0',
   baudrate = 38400,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)



while 1:
   data = bytearray([100])
   ser.write(data)
   data = bytearray([228])
   ser.write(data)
