# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'your wifi'
password = 'your wifi password'
mqtt_server = 'your mqtt server IP '
mqtt_user = 'your mqtt user name'
mqtt_password = 'your mqtt user password'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification' #test Sub
topic_sub2 = b'Ant' # real Sub
topic_pub = b'hello' # message test

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())






