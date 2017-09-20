from neomatrix import NeoMatrix

import network
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("UPC36171B1", "vA54mznzkGet")

import webrepl
webrepl.start()

nm = NeoMatrix(8, 8)

def heart():
    nm.set_color()
    nm.line(1,1,2,1,r=100)
    nm.line(5,1,6,1,r=100)
    nm.line(0,2,7,2,r=100)
    nm.line(0,3,7,3,r=100)
    nm.line(1,4,6,4,r=100)
    nm.line(2,5,5,5,r=100)
    nm.line(3,6,4,6,r=100)
    nm.set_pixel(1,2,r=33,g=33,b=33)
    nm.set_pixel(1,3,r=33,g=33,b=33)
    nm.set_pixel(2,2,r=33,g=33,b=33)
    nm.update_matrix()