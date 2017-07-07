import network
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("UPC36171B1", "vA54mznzkGet")

import json
import urequests

r = urequests.get("http://duckduckgo.com/?q=micropython&format=json").json()
print(r)
print(r['AbstractText'])
