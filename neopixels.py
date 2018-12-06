# https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 12

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def wheel(pos):
	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos*3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255 - pos*3)
		g = 0
		b = int(pos*3)
	else:
		pos -= 170
		r = 0
		g = int(pos*3)
		b = int(255 - pos*3)
	return (r, g, b)

def rainbow_cycle(wait):
	for j in range(255):
		for i in range(num_pixels):
			pixels[i] = wheel(j)
		pixels.show()
		time.sleep(wait)

while True:
	rainbow_cycle(0.005)
