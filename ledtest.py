import time

from neopixel import *

# LED strip configuration:
LED_COUNT = 20    # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

i = 0

while True:
    for(j in range(LED_COUNT))
        i+=1
        strip.setPixelColor(j, Color((j+i)%255, (j*i)%255, (i-j)%255)
    strip.show()
    