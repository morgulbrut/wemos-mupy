from machine import Pin
import dht
import neopixel
import time
import network
import urequests

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("UPC36171B1", "vA54mznzkGet")

sensor = dht.DHT11(Pin(2))
pixels = neopixel.NeoPixel(Pin(4, Pin.OUT), 1)


def my_map(val,in_min=0,in_max=100,out_min=0,out_max=255):
	return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
	sensor.measure()
	temp = sensor.temperature()
	humi = sensor.humidity()

	print('TEMP: '+str(temp))
	print('TEM2: '+str(my_map(temp, in_min=-10, in_max=40)))
	print('HUMI: '+str(humi))
	print('HUM2: '+str(my_map(humi)))

	pixels[0] = (int(my_map(temp, in_min=-10, in_max=40)),int(my_map(humi)), 0)
	pixels.write()

	#urequests.get(" http://api.thingspeak.com/update?api_key=EA1SJP1FPTC2JNJC&field1="+str(temp)+"&fiel2"+str(humi))

	time.sleep(30)

