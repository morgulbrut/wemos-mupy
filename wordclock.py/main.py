from neomatrix import NeoMatrix
#from machine import RTC
import network
import machine
import time
import urandom

sta = network.WLAN(network.STA_IF)
sta.active(True)
#sta.connect("UPC36171B1", "vA54mznzkGet")
sta.connect("mechartlab", "transistor")


apikey = 'YKV0I7RO6J9J'
timezone = 'Europe/Zurich'

url = 'http://api.timezonedb.com/v2/get-time-zone?key=' + \
    apikey+'&format=json&by=zone&zone='+timezone

rtc = machine.RTC()
nm = NeoMatrix(8, 8)

try:
    import usocket as socket
except:
    import socket


def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    ret = ''
    while True:
        data = s.recv(100)
        if data:
            ret += str(data, 'utf8')
        else:
            break
    s.close()
    return ret


def get_time_from_web():
    date_time = http_get(url).split('"')[-2]
    try:
        time = date_time.split()[1].split(':')
        date = date_time.split()[0].split('-')
        date_time = date+time+['0', '0']
    except IndexError:
        print('IndexError')
        date_time = ['0','0','0','0','0','0','0','0']
    d_t = []
    for i in date_time:    
        d_t.append(int(i))
    print(d_t)
    return d_t


def show_time(h, m, rh=0, gh=100, bh=0, rm=100, gm=0, bm=0):
    nm.clear()
    if m < 3:
        pass
    elif m >= 3 and m < 8:
        m_five(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 8 and m < 13:
        m_ten(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 13 and m < 18:
        m_quarter(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 18 and m < 23:
        m_twenty(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 23 and m < 28:
        m_twentyfive(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 28 and m < 33:
        m_half(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 23 and m < 28:
        m_twentyfive(rm, gm, bm)
        m_to(rm, gm, bm)
    elif m >= 28 and m < 33:
        m_half(rm, gm, bm)
        m_past(rm, gm, bm)
    elif m >= 33 and m < 38:
        m_twentyfive(rm, gm, bm)
        m_to(rm, gm, bm)
        h += 1
    elif m >= 38 and m < 43:
        m_twenty(rm, gm, bm)
        m_to(rm, gm, bm)
        h += 1
    elif m >= 43 and m < 48:
        m_quarter(rm, gm, bm)
        m_to(rm, gm, bm)
        h += 1
    elif m >= 48 and m < 53:
        m_ten(rm, gm, bm)
        m_to(rm, gm, bm)
        h += 1
    elif m >= 53 and m < 58:
        m_five(rm, gm, bm)
        m_to(rm, gm, bm)
        h += 1
    elif m >= 58:
        h += 1

    if h == 0 or h == 12 or h == 24:
        h_twelve(rh, gh, bh)
    elif h == 1 or h == 13:
        h_one(rh, gh, bh)
    elif h == 2 or h == 14:
        h_two(rh, gh, bh)
    elif h == 3 or h == 15:
        h_three(rh, gh, bh)
    elif h == 4 or h == 16:
        h_four(rh, gh, bh)
    elif h == 5 or h == 17:
        h_five(rh, gh, bh)
    elif h == 6 or h == 18:
        h_six(rh, gh, bh)
    elif h == 7 or h == 19:
        h_seven(rh, gh, bh)
    elif h == 8 or h == 20:
        h_eight(rh, gh, bh)
    elif h == 9 or h == 21:
        h_nine(rh, gh, bh)
    elif h == 10 or h == 22:
        h_ten(rh, gh, bh)
    else:
        h_eleven(rh, gh, bh)
    nm.update_matrix()


def set_time():
    date_time = get_time_from_web()
    rtc.datetime(date_time)


def m_five(r, g, b):
    nm.line(0, 2, 3, 2, r, g, b)


def m_ten(r, g, b):
    nm.line(3, 0, 4, 0, r, g, b)
    nm.set_pixel(1, 0, r, g, b)


def m_quarter(r, g, b):
    nm.line(0, 1, 6, 1, r, g, b)
    nm.set_pixel(0, 0, r, g, b)


def m_twenty(r, g, b):
    nm.line(1, 0, 6, 0, r, g, b)


def m_twentyfive(r, g, b):
    m_twenty(r, g, b)
    m_five(r, g, b)


def m_half(r, g, b):
    nm.line(4, 2, 7, 2, r, g, b)


def m_past(r, g, b):
    nm.line(1, 3, 4, 3, r, g, b)


def m_to(r, g, b):
    nm.line(4, 3, 5, 3, r, g, b)


def h_one(r, g, b):
    nm.set_pixel(1, 7, r, g, b)
    nm.set_pixel(4, 7, r, g, b)
    nm.set_pixel(7, 7, r, g, b)


def h_two(r, g, b):
    nm.line(0, 6, 1, 6, r, g, b)
    nm.set_pixel(1, 7, r, g, b)


def h_three(r, g, b):
    nm.line(3, 4, 7, 4, r, g, b)


def h_four(r, g, b):
    nm.line(0, 7, 3, 7, r, g, b)


def h_five(r, g, b):
    nm.line(0, 4, 3, 4, r, g, b)


def h_six(r, g, b):
    nm.line(0, 5, 2, 5, r, g, b)


def h_seven(r, g, b):
    nm.set_pixel(0, 5, r, g, b)
    nm.line(4, 6, 7, 6, r, g, b)


def h_eight(r, g, b):
    nm.line(3, 4, 7, 4, r, g, b)


def h_nine(r, g, b):
    nm.line(4, 7, 7, 7, r, g, b)


def h_ten(r, g, b):
    nm.set_pixel(0, 6, r, g, b)
    nm.set_pixel(2, 6, r, g, b)
    nm.set_pixel(7, 6, r, g, b)


def h_eleven(r, g, b):
    nm.line(2, 6, 7, 6, r, g, b)


def h_twelve(r, g, b):
    nm.line(0, 6, 3, 6, r, g, b)
    nm.line(5, 6, 6, 6, r, g, b)

while True:
    t = get_time_from_web()
    try:
        show_time(t[3], t[4], bm=urandom.getrandbits(8), rh=urandom.getrandbits(8))
        time.sleep(60)
    except AttributeError:
        print('AttributeError')