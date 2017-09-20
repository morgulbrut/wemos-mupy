import machine, ssd1306, network, time

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

sta_if = network.WLAN(network.STA_IF) 
sta_if.active(True)

oled.fill(0) 
oled.text('Wifi-Scanner on', 0, 0)
oled.text('an ESP32 done', 0, 10)
oled.text('in MicroPython', 0, 20)
oled.show()

time.sleep(2)

while True:
	oled.fill(0)
	oled.text('scanning...',0,0)
	oled.show()
	ssids = sta_if.scan()
	ssids.sort()
	for ssid in ssids:
		oled.fill(0)
		oled.text(ssid[0].decode('utf-8'),0,0)
		hex_string = "".join("%02x" % b for b in ssid[1])
		oled.text(hex_string,0,10)
		oled.text('ch: '+str(ssid[2]),0,20)
		oled.text('lq: '+str(ssid[3]),0,30)
		authmode = ssid[4]
		if(authmode == network.AUTH_OPEN):
			oled.text('Open (yay)',0,40)
		elif(authmode == network.AUTH_WEP):
			oled.text('WEP',0,40)
		elif(authmode == network.AUTH_WPA_PSK):
			oled.text('WPA PSK',0,40)
		elif(authmode == network.AUTH_WPA2_PSK):
			oled.text('WPA2 PSK',0,40)
		elif(authmode == network.AUTH_WPA_WPA2_PSK):
			oled.text('WPA/WPA2 PSK',0,40)
		else:
			oled.text('dunno',0,40)
		oled.show()
		time.sleep(1)
