
from machine import Pin,I2C
from pico_i2c_lcd import I2cLcd
import time
import utime
from dht import  DHT11

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

#=================================================================

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000) #100kHz
lcd = I2cLcd(i2c ,DEFAULT_I2C_ADDR, 2, 16)
lcd.move_to(5,0)
lcd.putstr("DHT11")

pin = Pin(15,Pin.IN,Pin.PULL_UP)
dht11 = DHT11(pin,None,dht11=True)

while True:
        T,H = dht11.read()
        if T is None:
            #print(" sensor error")
            lcd.move_to(5,0)
            lcd.putstr("DHT11")
        else:
            #print("{:3.1f}'C  {:3.1f}%".format(T,H))        
            lcd.move_to(0,1)
            lcd.putstr("T=" + str(T) + "C   "+ "H="+ str(H) +"%")

        utime.sleep_ms(500)



