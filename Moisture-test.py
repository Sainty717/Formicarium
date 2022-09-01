from machine import Pin, ADC
from time import sleep
import array
pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v


while True:
    print(pot.read())
    sleep(1)
  
  
