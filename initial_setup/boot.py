import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("UPC36171B1", "vA54mznzkGet")

import webrepl
webrepl.start()

import gc	
gc.collect()
