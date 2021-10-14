from machine import Pin, PWM
import utime

CLOSE=3000000
OPEN=2000000

led = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

pwm=PWM(Pin(16))
pwm.freq(50)
pwm.duty_ns(CLOSE)

while True:
    if button.value():
        led.high()
        pwm.duty_ns(OPEN)
        utime.sleep(0.5)
        pwm.duty_ns(CLOSE)
        utime.sleep(0.5)
        led.low()
        
        
