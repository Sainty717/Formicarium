
from machine import Pin, ADC,  deepsleep
from time import sleep

pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
import dht 
import json
sensor = dht.DHT22(Pin(15))
#sensor = dht.DHT11(Pin(14))

import array
pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
def Average(l): 
    avg = sum(l) / len(l) 
    return avg



def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')



def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, topic_sub2, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_password)
  client.connect()
  client.set_callback(sub_cb)
  client.subscribe(topic_sub)
  client.subscribe(topic_sub2)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()



class LDR:
    """This class read a value from a light dependent resistor (LDR)"""

    def __init__(self, pin, min_value=0, max_value=100):
        """
        Initializes a new instance.
        :parameter pin A pin that's connected to an LDR.
        :parameter min_value A min value that can be returned by value() method.
        :parameter max_value A max value that can be returned by value() method.
        """

        if min_value >= max_value:
            raise Exception('Min value is greater or equal to max value')

        # initialize ADC (analog to digital conversion)
        self.adc = ADC(Pin(pin))

        # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
        self.adc.atten(ADC.ATTN_11DB)

        self.min_value = min_value
        self.max_value = max_value

    def read(self):
        """
        Read a raw value from the LDR.
        :return A value from 0 to 4095.
        """
        return self.adc.read()

    def value(self):
        """
        Read a value from the LDR in the specified range.
        :return A value from the specified [min, max] range.
        """
        return (self.max_value - self.min_value) * self.read() / 4095


# initialize an LDR
ldr = LDR(33)

high = 3150
low = 950

while True:
  
  try:
    print('start')
    
    led = machine.Pin(2, machine.Pin.OUT)
    led.value(1)
    sleep(.2)
    led.value(0)
    pot_value = 100 * (pot.read() - high) / (low - high)
    print(pot_value)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    value = ldr.value()
    print('Light: {}'.format(value) + '%')
    print('Mosture Level: ' + str(pot_value))
    client.check_msg()
    dictionary = {'Temperature': str(temp),'Humidity': str(hum),'Light': str(int(value)),'Moisture':  str(pot_value),'Node': str(client_id)}
    jsonString = json.dumps(dictionary)
    print(jsonString)  
    print('submit')
    client.publish('Ant', jsonString )
    last_message = time.time()
    counter += 1
    print('submitted message')
    led.value(1)
    sleep(.5)
    led.value(0)
    sleep(.5)
    led.value(1)
    sleep(.5)
    led.value(0)
    deepsleep(900000)
    print('sleep started')
  except OSError as e:
    print(e)


