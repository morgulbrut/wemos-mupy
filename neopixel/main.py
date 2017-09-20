from machine import Pin
import neopixel
import time


class NeoMatrix:

	def __init__(self, x, y):
		self.colors = []
			for i in range(x):
				for j in range(x):
					colors[i][j] = Color(0,0,0)
		self.np = neopixel.NeoPixel(Pin(4, Pin.OUT),x*y)
		self.np.write()

	def set_pixel(self,x,y,r=0,g=0,b=0):
		self.colors[x][y] = Color(r,g,b)
		self.np.write()

class Color:

	def __init__(self,r,g,b):
		self.r = r
		self.g = g
		self.b = b

# def clear(np):
# 	set(np)

# def cycle(np,r=0,g=0,b=0,delay=25,cycles=1,invert=False):
# 	for i in range(cycles):
# 		bounce(np,r,g,b,delay,1,invert)

# def bounce(np,r=0,g=0,b=0,delay=25,cycles=2,invert=False):
# 	for i in range(cycles * np.n):
# 		if invert:
# 			for j in range(np.n):
# 				np[j] = (r, g, b)
# 			if (i // np.n) % 2 == 0:
# 				np[i % np.n] = (0, 0, 0)
# 			else:
# 				np[np.n - 1 - (i % np.n)] = (0, 0, 0)
# 		else:
# 			for j in range(np.n):
# 				np[j] = (0, 0, 0)
# 			if (i // np.n) % 2 == 0:
# 				np[i % np.n] = (r, g, b)
# 			else:
# 				np[np.n - 1 - (i % np.n)] = (r, g, b)

# 		np.write()
# 		time.sleep_ms(delay)
# 	clear(np)

# def fade_in(np,r=0,g=0,b=0,delay=25,cycles=1):
# 	for i in range(0,256,8):
# 		rn = my_map(r,in_max=i,out_max=r)
# 		gn = my_map(g,in_max=i,out_max=g)
# 		bn = my_map(b,in_max=i,out_max=b)
# 		set(np,rn,gn,bn)
# 		print(rn)

# def my_map(val,in_min=0,in_max=255,out_min=0,out_max=255):
# 	try:
# 		return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
# 	except ZeroDivisionError:
# 		return 0



# def demo(np):
# 	n = np.n
# 	# fade in/out
# 	for i in range(0, 4 * 256, 8):
# 		for j in range(n):
# 			if (i // 256) % 2 == 0:
# 				val = i & 0xff
# 			else:
# 				val = 255 - (i & 0xff)
# 			np[j] = (val, 0, 0)
# 		np.write()

# 	# clear
# 	clear(np)
