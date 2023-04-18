from machine import Pin, Timer
led=Pin(25, Pin.OUT)
t=Timer()

def blink(t):
    led.toggle()
    
t.init(freq=1, mode=Timer.PERIODIC, callback=blink) 