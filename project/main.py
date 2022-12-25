
from machine import Pin, I2C
import network
import time 
import machine
from time import sleep
from machine import Pin,PWM
import dht
import ujson
from umqtt.simple import MQTTClient



sensor = dht.DHT22(Pin(15))
p4 = machine.Pin(14)
freq=50
servo = machine.PWM(p4,freq)
led = Pin(18,Pin.OUT)





prev_temp = 0
prev_humt = 0
prev_weather = " "
while True:
  print("Measuring weather conditions... ", end="")
  sensor.measure() 
  temp = sensor.temperature(),
  humt = sensor.humidity(),
  if temp != prev_temp or humt != prev_humt :

    print("Updated!")
    if temp[0] > 40 :
        print("Turn on AC")
        for duty_cycle in range(0, 1024):
            servo.duty(duty_cycle)
            sleep(4)
    elif temp[0] < 25 :
        print("Turn on heater")
        led.value(1)
        time.sleep(2)

      
    else :
      mes = ""
    print("Temp : ",temp)
    print("Humidity : ",humt)
    
    prev_temp = temp
    prev_humt = humt
  else:
    print("No change")
  time.sleep(1)
