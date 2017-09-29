
#!/usr/bin/env python

import sys
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

action = sys.argv[1]
print action

if action == "stop":
   speed1 = 0
   speed2 = 0

elif action == "forward":
   speed1 = 1
   speed2 = 128
   
elif action == "right":
   speed1 = 190
   speed2 = 50
   
elif action == "left":
   speed1 = 63
   speed2 = 150
      


while 1:
   data = bytearray([speed1])
   ser.write(data)
   data = bytearray([speed2])
   ser.write(data)
   

