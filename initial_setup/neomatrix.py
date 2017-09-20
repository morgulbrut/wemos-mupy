from machine import Pin
import neopixel
import time


class NeoMatrix:

    def __init__(self, x, y, pin=4):
        self.colors = []
        self.x = x
        self.y = y
        for i in range(self.x):
            temp = []
            for j in range(self.y):
                temp.append(Color(0, 0, 0))
            self.colors.append(temp)
        self.np = neopixel.NeoPixel(Pin(pin, Pin.OUT), x*y)
        self.np.write()

    def update_matrix(self):
        for i in range(self.x):
            for j in range(self.y):
                c = self.colors[i][j]
                self.np[i+j*self.x] = (c.r, c.g, c.b)
        self.np.write()

    def set_pixel(self, x, y, r=0, g=0, b=0):
        self.colors[x][y] = Color(r, g, b)

    def set_color(self, r=0, g=0, b=0):
        for i in range(self.x):
            for j in range(self.y):
                self.set_pixel(i, j, r, g, b)

    def clear(self):
        self.set_color()
        self.update_matrix()

    def line(self, x0, y0, x1, y1, r=0, g=0, b=0):
        # Bresenham's line algorithm
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.set_pixel(x, y, r, g, b)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.set_pixel(x, y, r, g, b)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.set_pixel(x, y, r, g, b)

    def demo(self):
        for i in range(self.x):
            for j in range(self.y):
                self.set_pixel(i, j, i*8, j*8, 0)
                self.update_matrix()
                time.sleep(0.1)
        for i in range(self.x):
            for j in range(self.y):
                self.set_pixel(i, j, 0, i*8, j*8)
                self.update_matrix()
                time.sleep(0.1)
        for i in range(self.x):
            for j in range(self.y):
                self.set_pixel(i, j, i*8, 0, j*8)
                self.update_matrix()
                time.sleep(0.1)


class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return('(r='+str(self.r)+',g='+str(self.g)+',b='+str(self.b)+')')