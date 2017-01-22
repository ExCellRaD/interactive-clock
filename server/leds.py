from collections import namedtuple
from datetime import datetime, timedelta
from dateutil.parser import parse
import time
# from neopixel import *

# LED strip configuration:
LED_COUNT = 48  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)

LedEvent = namedtuple("LedEvent", "start end color")

def timeToLed(time): # fractioneel getal
    t = (time.hour + time.minute / 60.0) % 12 # kommagetal van 0 tot 12
    return (t / 12) * LED_COUNT # de dichstbijzijnde led

def timeToLedInt(time): # natuurlijk getal
    return int(round(timeToLed(time)))

class Leds:
    events = [] # hierin zit de kalender (start tijd, eind tijd, kleur RGB)
    running = True # zet op false om te stoppen

    def __init__(self):
        self.setBrightness(255)

    def setEvents(self, events):
        now = datetime.utcnow()
        in12h = now + timedelta(hours=12)
        self.events = []
        for event in events:
            # omzetten van string tijden naar datetime objecten
            start = parse(event["start"]["datetime"])
            end = parse(event["end"]["datetime"])

            # omzetten van html kleur naar RGB waarden
            hex = event["color"].lstrip('#')
            color = tuple(ord(c) for c in hex.decode('hex'))
            self.events.append(LedEvent(start = start, end = end, color = color))


    def setBrightness(self, value):
        #self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, 0, value)
        #self.strip.begin()
        self.brightness = value


    def main(self):
        while(self.running):
            now = datetime.utcnow()
            in12h = now + timedelta(hours=12) #laatste tijd die we kunnen weergeven
            # kalender display
            for event in (self.events):
                start = event.start
                end = event.end
                # afsnijden van onzichtbare delen
                if(start < now): 
                    start = now
                if(end > in12h): 
                    end = in12h
                if(start < end): # events kunnen onzichtbaar zijn (buiten 12 uur)
                    startled = timeToLedInt(start)
                    endled = timeToLedInt(end)
                    for led in range(startled, endled):
                        self.setColor(led, event.color)
            # klok display
            hour = timeToLedInt(now)
            self.setColor(hour, (255,255,255)) # uur is wit
            minute = int(round((now.minute() / 60.0) * LED_COUNT))
            self.setColor(minute, (255,100,100)) # minuut is blauw

    def setColor(self, led, kleur):
        print led,kleur