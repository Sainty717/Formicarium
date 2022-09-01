from machine import Pin, ADC,  deepsleep
from time import sleep
import dht 
import json
sensor = dht.DHT22(Pin(15))
sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()
print('Temperature: %3.1f C' %temp)
print('Humidity: %3.1f %%' %hum)
